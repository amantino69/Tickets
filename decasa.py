from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import datetime
import pdb 
import re
from selenium.webdriver.support.ui import Select
from fuzzywuzzy import process

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

# print("Clicando no botão Logar")
# Espera até que o elemento esteja visível na página
elemento = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/button')))

elemento.click()

sleep(5)

# Vá para a página de Prioridades Samanais nessa hpra clica no geral e não em um ticket específico
elemento = driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]/div[1]/div[1]/div/a[2]/span[1]')

tabela = elemento
elemento.click()

# sleep(3)

# Atribua à variável html_interno todo conteúdo html da página
elemento = driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]')
html_interior = elemento.get_attribute('innerHTML')


# # Criar um DataFrame com as linhas e colunas da tabela
dfs = pd.read_html(html_interior)
df = dfs[0]

#Mostre o conteúdo do DataFrame
print(df)

# # Altera o nome da coluna "#" por ticket
df.rename(columns={'#': 'ticket'}, inplace=True)

# Cria uma lista para ser utilizada em um loop com as linhas da coluna ticket
lista = df['ticket'].tolist()
# mostra o conteúdo da lista
print(lista)

# Remove linhas cujo conteúdo não seja somente algarismos
lista = [x for x in lista if x.isdigit()]

print(lista)

# Cria um loop com a lista e a cada rodada localize o elemento "//*[@id="global-search"]" e atribua o conteudo da lista para esse campo


prioridade = 0
for i in lista:
    
    # se prioridade for igual a 10, atribui o valor 10 a prioridade
    if prioridade > 9:
        prioridade = 9

    try:
        # Clique no elemento "//*[@id="navigation"]/div[1]/form/div[2]/svg"
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[1]/form/div[2]/svg')
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

    # Copia para o campo de busca o conteúdo da lista
    elemento.send_keys(i)
   
    # Adicione uma espera explícita
    wait = WebDriverWait(driver, 30)
    elemento = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[contains(text(), "{i}")]')))
    elemento.click()

    # Encontre o índice da linha que contém o valor de 'i' na coluna 'ticket'
    index = df[df['ticket'] == i].index[0]
    sleep(15)
    # Espera até que o elemento esteja presente na página
    # elementos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f'//*[contains(@id, "content_permanent_Ticket-{i}")]/div/div[2]/div/div[2]/div/div[3]/small/time')))
    elementos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@id, "content_permanent_Ticket-")]')))
    # Espera até que o elemento esteja presente na página
    # elementos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f'//*[contains(@id, "content_permanent_Ticket-{i}")]/div/div[2]/div/div[2]/div/div[3]/small/time')))

    for elemento in elementos:
        elemento.click()
       
        sleep(5)
        # Salva o texto do elemento na coluna 'descrição' na linha 'i'
        df.loc[index, 'descrição'] = elemento.text
        
        # # Localizar 'title' em elemento.text e atribuir o seu valor à variável 'Criado_em'
        # Criado_em = elemento.text.split('title: ')[0].split(' -')[1]
        # df.loc[index, 'Criado_em'] = Criado_em
        
        
        # Localizar a data em elemento.text e atribuir o seu valor à variável 'Criado_em'
        match = re.search(r'\d{2}/\d{2}/\d{4}', elemento.text)
        if match is not None:
            Criado_em = match.group()
            df.loc[index, 'Criado_em'] = Criado_em
        
        # Se em match tiver a palavra hora stribuie à variável Criado_em a data de hoje no formaro dd/mm/aaaa
        if 'hora' in elemento.text:
            Criado_em = datetime.date.today().strftime("%d/%m/%Y")
            df.loc[index, 'Criado_em'] = Criado_em
     
     
        # Localize o elemento pelo nome
        elemento = driver.find_element(By.NAME, 'priorizada')

        # Cria uma instância da classe Select
        select = Select(elemento)

        # Seleciona a opção pelo valor
        select.select_by_value(str(prioridade))
        
        # Localize o botão pelo texto
        botao = driver.find_element(By.XPATH, '//button/span[text()="Atualizar"]')

        # Clique no botão
        botao.click()
        
        # Aumenta o valor de prioridade em 1
        prioridade += 1
        

            

            
    # Adicionar as colunas Data_atual e hora_atual
    df['Data_atual'] = datetime.date.today()
    df['hora_atual'] = datetime.datetime.now().strftime("%H:%M:%S")
    
    
    
    
     # Crie uma coluna chamada 'Município' e atribua a ela a primeira ocorrência  entre "[]" da coluna 'Título'
    df['Município'] = df['Título'].str.extract(r'\[(.*?)\]')
    




    # Cria um dicionário para armazenar o nome mais recente de cada município
    municipios = {}

    def unificar_nome_municipio(nome):
        # Se o nome não for uma string, retorna como está
        if not isinstance(nome, str):
            return nome

        # Verifica se existe um nome semelhante no dicionário
        for nome_existente in municipios.keys():
            if process.extractOne(nome, municipios.keys()) and process.extractOne(nome, municipios.keys())[1] >= 70:
                # Se houver, substitui o nome do município pelo nome mais recente
                nome = municipios[nome_existente]
                break

        # Salva o nome do município no dicionário
        municipios[nome] = nome

        return nome

    # Aplica a função unificar_nome_municipio a cada município no DataFrame
    df['Município'] = df['Município'].apply(unificar_nome_municipio)






       
    # Se Proprietário for = a '-'  preencha com o valor de Proprietário da linha anterior
    df['Proprietário'] = df['Proprietário'].replace('-', method='ffill')

    # Remova as linha em que Ticket é igual a NaN
    df = df.dropna(subset=['ticket'])
    
    # Remova as linha em que Ticket é igual "Aberto" ou Feedback ou "Novo"
    df = df[df.ticket != 'aberto']
    df = df[df.ticket != 'Feedback']
    df = df[df.ticket != 'novo']
    


# Lê a planilha existente em um DataFrame
try:
    df_existente = pd.read_excel('priorizadas_semana.xlsx')
except FileNotFoundError:
    df_existente = pd.DataFrame()


# Adiciona os novos registros ao DataFrame existente
df_final = pd.concat([df_existente, df])

# Escreve o DataFrame de volta para a planilha
df_final.to_excel('priorizadas_semana.xlsx', index=False)


