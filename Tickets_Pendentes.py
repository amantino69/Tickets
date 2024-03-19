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
# Clicar na opção FECHADO da lista 
# Aguarda até que o elemento esteja visível e possa ser clicado
elemento = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Tickets Pendentes"]')))

# Clica no elemento
elemento.click()

sleep(20) 



# Lista para armazenar os DataFrames de cada página
dfs = []

# Obter o número total de páginas
num_paginas = len(driver.find_elements(By.CSS_SELECTOR, 'div.js-pager div.js-page'))

# Iterar sobre cada página
for i in range(num_paginas):
    # Localizar o elemento da página novamente
    pagina = driver.find_elements(By.CSS_SELECTOR, 'div.js-pager div.js-page')[i]

    # Clicar na página para carregar a tabela correspondente
    pagina.click()

    # Aguardar até que a tabela esteja visível
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]/div[2]/div[2]/div')))

    # Obter o HTML da tabela
    tabela_html = driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]/div[2]/div[2]/div').get_attribute('outerHTML')

    # Ler a tabela HTML para um DataFrame
    df = read_html(tabela_html, header=0)[0]

    # Adicionar o DataFrame à lista
    dfs.append(df)

# Concatenar todos os DataFrames na lista em um único DataFrame
df_final = concat(dfs)

# Substituir o cabeçalho de nome "#" por "ticket"
df_final.rename(columns={'#': 'ticket'}, inplace=True)

# Excluir qualquer conteúdo literal da coluna 'ticket'
df_final['ticket'] = df_final['ticket'].str.extract('(\d+)')


# Preencher os valores NaN com um valor padrão (por exemplo, 0)
df_final['ticket'] = df_final['ticket'].fillna(0)

# Converter a coluna 'ticket' para inteiros
df_final['ticket'] = df_final['ticket'].astype(int)

# Adicionar uma coluna de nome Pendente e atribuir o valor Pendente em todas as linhas
df_final['Status'] = 'Pendente'



# Salvar o DataFrame final para um arquivo Excel com o número da iteração no nome do arquivo
df_final.to_excel(r'C:\Users\Regina Casoti\Documents\Vivver\Tickets_Pendentes.xlsx', index=False)