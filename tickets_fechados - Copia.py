from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
elemento = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Fechados"]')))

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

# Criar uma coluna de nome munípcio com o conteúdo que está na coluna Título entre colchetes
df_final['Município'] = df_final['Título'].str.extract(r'\[(.*?)\]')


def converter_data(horario_fechamento):
    # Se o horário de fechamento já está no formato "dd/mm/aaaa"
    if re.match(r'\d{2}/\d{2}/\d{4}', horario_fechamento):
        return horario_fechamento
    # Se o horário de fechamento está no formato "x minutos atrás" ou "x horas atrás"
    elif re.match(r'\d+ minutos atrás', horario_fechamento) or re.match(r'\d+ horas atrás', horario_fechamento):
        return datetime.now().strftime('%d/%m/%Y')
    # Se o horário de fechamento está no formato "x dias atrás"
    elif re.match(r'\d+ dias atrás', horario_fechamento):
        dias = int(re.findall(r'\d+', horario_fechamento)[0])
        data = datetime.now() - timedelta(days=dias)
        return data.strftime('%d/%m/%Y')
    # Se o horário de fechamento está no formato "x dias y horas atrás"
    elif re.match(r'\d+ dias \d+ horas atrás', horario_fechamento):
        dias, horas = map(int, re.findall(r'\d+', horario_fechamento))
        data = datetime.now() - timedelta(days=dias, hours=horas)
        return data.strftime('%d/%m/%Y')
    # Se o horário de fechamento está no formato "x horas y minutos atrás"
    elif re.match(r'\d+ horas \d+ minutos atrás', horario_fechamento):
        horas, minutos = map(int, re.findall(r'\d+', horario_fechamento))
        data = datetime.now() - timedelta(hours=horas, minutes=minutos)
        return data.strftime('%d/%m/%Y')

# Aplicar a função à coluna "Horário de Fechamento" para criar a nova coluna
df_final['Data de Fechamento'] = df_final['Horário de Fechamento'].apply(converter_data)


# Copiar df para uma planilha Excel de nome fechados.xlsx
df_final.to_excel('fechados.xlsx', index=False)


pdb.set_trace()

# Obter o HTML interno do elemento
elemento = driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]/div[2]/div[2]/div')
html_interior = elemento.get_attribute('innerHTML')

# Criar um DataFrame com as linhas e colunas da tabela
df = pd.read_html(html_interior, index_col=0)

# Copias para um df os dados da tabela
df = df[0].copy()
print("Tabela com tickets fechados", df)




# Altera o nome da coluna "#" por ticket
df.rename(columns={'#': 'ticket'}, inplace=True)

# Altera o nome da primeira coluna pora Status
df.rename(columns={'Unnamed: 1': 'Status'}, inplace=True)




# Cria uma lista para ser utilizada em um loop com as linhas da coluna ticket
lista = df['ticket'].tolist()
# Remove linhas cujo conteúdo não seja somente algarismos
lista = [x for x in lista if x.isdigit()]


# Cria um loop com a lista e a cada rodada colalize o elemento "//*[@id="global-search"]" e atribua o conteudo da lista para esse campo

# pdb.set_trace() isso

prioridade = 0
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
    sleep(10)

    # Encontre o índice da linha que contém o valor de 'i' na coluna 'ticket'
    index = df[df['ticket'] == i].index[0]
    
    sleep(5)
    # Espera até que o elemento esteja presente na página
    elementos = driver.find_elements(By.XPATH, '//*[contains(@id, "content_permanent_Ticket-")]')

    for index, elemento in enumerate(elementos):
        # Verifique se o elemento é interativo antes de clicar
        if elemento.is_displayed() and elemento.is_enabled():
            elemento.click()
            sleep(5)

            # Salva o texto do elemento na coluna 'descrição' na linha 'i'
            df.loc[index, 'descrição'] = elemento.text

    
    
    
    
    # Encontre todos os elementos que contêm 'Ticket-' em seu ID
    elementos = driver.find_elements(By.XPATH, '//*[contains(@id, "content_permanent_Ticket-")]')

    for elemento in elementos:
        # Extraia o número após 'Ticket-' no ID do elemento
        ticket_number = elemento.get_attribute('id').split('-')[-1]
        
        # Use o número do ticket no XPath
        xpath = f'//*[@id="content_permanent_Ticket-{ticket_number}"]/div/div[2]/div/div[2]/div/div[3]/small/time'
        
        # Espera até que o elemento esteja presente na página
        wait = WebDriverWait(driver, 10)
        elemento = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        
        # Extrai o valor do atributo 'title' do elemento
        title = elemento.get_attribute('title')
        
        # Salva o valor do atributo 'title' na coluna 'descrição' na linha correspondente ao número do ticket
        df.loc[int(ticket_number), ''] = title
    

   

        # Cria um objeto WebDriverWait com um tempo limite de 10 segundos
        wait = WebDriverWait(driver, 10)

        # Use o método until do objeto WebDriverWait para esperar até que o elemento esteja presente
        elemento = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="Ticket_{i}_priorizada"]')))

        # Cria uma instância da classe Select
        select = Select(elemento)

        # Seleciona a opção pelo valor
        select.select_by_value(str(prioridade))

        prioridade += 1

    # Adicionar as colunas Data_atual e hora_atual
    df['Data_atual'] = datetime.date.today()
    df['hora_atual'] = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Crie uma coluna chamada 'Município' e atribua a ela a primeira ocorrência  entre "[]" da coluna 'Título'
    df['Município'] = df['Título'].str.extract(r'\[(.*?)\]')
       
    # Se Proprietário for = a '-'  preencha com o valor de Proprietário da linha anterior
    df['Proprietário'] = df['Proprietário'].replace('-', method='ffill')

    # Remova as linha em que Ticket é igual a NaN
    df = df.dropna(subset=['ticket'])
    
    # Lê a planilha existente em um DataFrame
    try:
        df_existente = pd.read_excel('priorizadas_semana.xlsx')
    except FileNotFoundError:
        df_existente = pd.DataFrame()
        

# Adiciona os novos registros ao DataFrame existente
df_final = pd.concat([df_existente, df])

# Escreve o DataFrame de volta para a planilha
df_final.to_excel('priorizadas_semana.xlsx', index=False)