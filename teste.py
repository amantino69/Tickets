from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd
import datetime
import pdb 
import re
from selenium.webdriver.support.ui import Select
from pandas import read_html
from pandas import read_html, concat
from datetime import datetime, timedelta
from fuzzywuzzy import process
from io import StringIO




iteracao = 1

# Configura as opções do Chrome
webdriver_options = Options()
webdriver_options.add_experimental_option('detach', True)

# Desativa as notificações
prefs = {"profile.default_content_setting_values.notifications" : 2}
webdriver_options.add_experimental_option("prefs", prefs)

# Inicializa o driver do navegador (neste caso, Chrome)
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
df = pd.read_excel(r'C:\Users\Regina Casoti\Documents\Vivver\Tickets_Vivver.xlsx', skiprows=6)
lista = df['Ticket'].tolist()

# excluir ".0" dos elementos da lista
for i in range(len(lista)):
    lista[i] = str(lista[i]).replace('.0', '')


for i in lista:
    sleep(5)
    
    try:
        # Clique no elemento "//*[@id="navigation"]/div[1]/form/div[2]/svg"
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[1]/form/div[2]')
        elemento.click()
    except:
        pass    
    
    # Encontre o elemento '//*[@id="navigation"]/div[2]/a[1]/span' e clique nele
    try:
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[2]/a[1]/span')
        elemento.click()
    except:
        pass    

    
    # Limpa o campo de busca
    elemento = driver.find_element(By.XPATH, '//*[@id="global-search"]')
    elemento.clear()

    sleep(5)
    elemento = driver.find_element(By.XPATH, '//*[@id="global-search"]')
    
    elemento.send_keys(i)
    sleep(40)

    # Localizar o elemento
    elemento = driver.find_element(By.XPATH, f'//div[@class="global-search-menu"]//span[contains(text(), "{i}")]')

    # Clicar no elemento
    elemento.click()
    
    sleep(30)
    
    ##################################################

    # Encontre todos os elementos com a classe 'ticket-article-item system' e pegue o último
    elementos_sistema = driver.find_elements(By.CSS_SELECTOR, '.ticket-article-item.system .richtext-content')
    ultimo_comentario_sistema = elementos_sistema[-1].text if elementos_sistema else None

    # Encontre todos os elementos com a classe 'ticket-article-item customer' e pegue o último
    elementos_vivver = driver.find_elements(By.CSS_SELECTOR, '.ticket-article-item.customer .richtext-content')
    ultimo_comentario_vivver = elementos_vivver[-1].text if elementos_vivver else None

    # Encontre todos os elementos com a classe 'ticket-article-item agent' e pegue o último
    elementos_cresce = driver.find_elements(By.CSS_SELECTOR, '.ticket-article-item.agent .richtext-content')
    ultimo_comentario_cresce = elementos_cresce[-1].text if elementos_cresce else None
    
    
    # print do último comentário agent e customer e system
    print(f'Último comentário do sistema: {ultimo_comentario_sistema}')
    print(f'Último comentário do cliente: {ultimo_comentario_vivver}')
    print(f'Último comentário do agente: {ultimo_comentario_cresce}')
    
    

    
   # Abrir a planilha Excel r'C:\Users\Regina Casoti\Documents\Vivver\Tickets_Vivver.xlsx e criar 3 colunas: 'Último comentário do sistema', 'Último comentário do cliente' e 'Último comentário do agente' e salvar os respectivos comentários.  
    df.loc[df['Ticket'] == i, 'Último comentário do sistema'] = ultimo_comentario_sistema
    df.loc[df['Ticket'] == i, 'Último comentário do cliente'] = ultimo_comentario_vivver
    df.loc[df['Ticket'] == i, 'Último comentário do agente'] = ultimo_comentario_cresce
    
    
    ##################################################
        
        
              
    # Salvar a planilha
    df.to_excel(r'C:\Users\Regina Casoti\Documents\Vivver\Tickets_Vivver.xlsx', index=False)

    
  
