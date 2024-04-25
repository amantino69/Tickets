from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from pandas import read_html
import numpy as np
from a_pandas_ex_css_selector_from_html import pd_add_css_selector_from_html
from bs4 import BeautifulSoup


iteracao = 1

# Configura as opções do Chrome
webdriver_options = Options()
webdriver_options.add_experimental_option('detach', True)

# Desativa as notificações
prefs = {"profile.default_content_setting_values.notifications" : 2}
webdriver_options.add_experimental_option("prefs", prefs)

# Inicializa o driver do navegador (neste caso, Chrome)
driver = webdriver.Chrome(service=Service('venv\\chromedriver.exe'), options=webdriver_options)
from selenium import webdriver

driver = webdriver.Chrome(service=Service('venv\\chromedriver.exe'), options=webdriver_options)

# Espera até que a página tenha terminado de carregar
wait = WebDriverWait(driver, 20)  # Aumenta o tempo limite para 20 segundos


print("Abrindo o site...")
# Abre o site
driver.get("https://ticket.crescer.net")

print("Encontrando os campos de login e senha...")
# Encontra os campos de login e senha
campo_email = driver.find_element(By.XPATH, "//*[@id='username']")
campo_senha = driver.find_element(By.XPATH, "//*[@id='password']")

print("Preenchendo os campos de login e senha...")
# Preenche os campos de login e senha
campo_email.send_keys("claudio.vieira@vivver.com.br")
campo_senha.send_keys("ticket#2023")

print("Clicando no botão de novo ticket...")
# Espera até que o elemento esteja visível na página
elemento = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/button')))
elemento.click()

sleep(10)

# maximizar a janela
driver.maximize_window()
 
sleep(10)   

import pandas as pd

# pdb.set_trace()

# Abra a planilha
df = pd.read_excel(r'planilhas\Tickets_Vivver.xlsx', skiprows=6)
lista = df['Ticket'].tolist()

# excluir ".0" dos elementos da lista
for i in range(len(lista)):
    lista[i] = str(lista[i]).replace('.0', '')


for i in lista:
    sleep(5)
    
    try:
        # Clique no elemento Campo de pesquisa do Ticket opção 1
        print("Clicando no campo de pesquisa do Ticket opção 1 ...")
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[1]/form/div[2]')
        # Adicione um contorno ao elemento para destacá-lo
        driver.execute_script("arguments[0].style.border='3px solid red'", elemento)
        elemento.click()
    except:
        pass    
    
    try:
        # Clique no elemento Campo de pesquisa do Ticket opção 2
        print("Clicando no campo de pesquisa do Ticket opção 2...")
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[2]/a[1]/span')
        # Adicione um contorno ao elemento para destacá-lo
        driver.execute_script("arguments[0].style.border='3px solid blue'", elemento)
        elemento.click()
    except:
        pass    

    
    # Limpa o campo de busca
    print("Limpando o campo de busca...")
    elemento = driver.find_element(By.XPATH, '//*[@id="global-search"]')
    # Adicione um contorno ao elemento para destacá-lo
    driver.execute_script("arguments[0].style.border='3px solid green '", elemento)
    elemento.clear()
 
    sleep(5)
    print("Preenchendo o campo de busca...")
    elemento = driver.find_element(By.XPATH, '//*[@id="global-search"]')
    driver.execute_script("arguments[0].style.border='3px solid white '", elemento)

    elemento.send_keys(i)
    sleep(10)

    # Localizar o elemento
    print("Localizando o elemento...")
    elemento = driver.find_element(By.XPATH, f'//div[@class="global-search-menu"]//span[contains(text(), "{i}")]')
    driver.execute_script("arguments[0].style.border='3px solid yellow'", elemento) 
    # black, blue, green, red, white, yellow = (0, 0, 0), (0, 0, 255), (0, 128, 0), (255, 0, 0), (255, 255, 255), (255, 255, 0)
    # Clicar no elemento
    elemento.click()
    driver.execute_script("arguments[0].style.border='3px solid red'", elemento) 
    
    sleep(30)
    
    ##################################################

    # Encontre todos os elementos com a classe 'ticket-article-item system'
    elementos_sistema = driver.find_elements(By.CSS_SELECTOR, '.ticket-article-item.system .richtext-content')
    # Destaque cada elemento com uma borda verde comentários do SYSTEM
    for elemento in elementos_sistema:
        driver.execute_script("arguments[0].style.border='3px solid green'", elemento)
    ultimo_comentario_sistema = elementos_sistema[-1].text if elementos_sistema else None

    
    # Encontre todos os elementos com a classe 'ticket-article-item customer' e pegue o último
    elementos_vivver = driver.find_elements(By.CSS_SELECTOR, '.ticket-article-item.customer .richtext-content')
    # Destaque cada elemento com uma borda amarela
    for elemento in elementos_vivver:
        driver.execute_script("arguments[0].style.border='3px solid yellow'", elemento)
    ultimo_comentario_vivver = elementos_vivver[-1].text if elementos_vivver else None

    # Encontre todos os elementos com a classe 'ticket-article-item agent' e pegue o último
    elementos_crescer = driver.find_elements(By.CSS_SELECTOR, '.ticket-article-item.agent .richtext-content')
    # Destaque cada elemento com uma borda vermelha
    for elemento in elementos_crescer:
        driver.execute_script("arguments[0].style.border='3px solid red'", elemento)
    ultimo_comentario_crescer = elementos_crescer[-1].text if elementos_crescer else None
   
   
    # print do último comentário agent e customer e system
    print(f'Último comentário do sistema: {ultimo_comentario_sistema}')
    print(f'Último comentário do cliente: {ultimo_comentario_vivver}')
    print(f'Último comentário do agente: {ultimo_comentario_crescer}')
    



    # Arredonde a coluna 'Ticket' para um número inteiro
    df['Ticket'] = df['Ticket'].round(0)

    # Converta 'i' para float e arredonde para um número inteiro
    i = round(float(i))

    # Encontre a linha correspondente ao valor de 'i' na coluna 'Ticket'
    matching_rows = df[df['Ticket'] == i]

    if not matching_rows.empty:
        row_index = matching_rows.index[0]

        # Adicione os comentários nas colunas correspondentes na linha encontrada
        df.at[row_index, 'agente'] = ultimo_comentario_crescer
        df.at[row_index, 'cliente'] = ultimo_comentario_vivver
        df.at[row_index, 'sistema'] = ultimo_comentario_sistema
    else:
        print(f"Não foi encontrada nenhuma linha onde 'Ticket' é igual a {i}")

    # Salve a planilha
    df.to_excel(r'planilhas\Tickets_Vivver.xlsx', index=False)
