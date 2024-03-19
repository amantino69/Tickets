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

# Vá para a página de Prioridades Samanais
elemento = driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]/div[1]/div[1]/div/a[2]/span[1]')
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
    sleep(15)
    
    # Adicione uma espera explícita
    wait = WebDriverWait(driver, 20)
    elemento = wait.until(EC.presence_of_element_located((By.LINK_TEXT, i)))
    elemento.click()
    
#     # Encontre o índice da linha que contém o valor de 'i' na coluna 'ticket'
    index = df[df['ticket'] == i].index[0]
    
    sleep(1)
    

#     # Espera até que o elemento esteja presente na página
    elementos = driver.find_elements(By.XPATH, '//*[contains(@id, "content_permanent_Ticket-")]')

    for elemento in elementos:
        elemento.click()
        sleep(5)
#         # Salva o texto do elemento na coluna 'descrição' na linha 'i'
        df.loc[index, 'descrição'] = elemento.text
        
#     # Adicionar as colunas Data_atual e hora_atual
    df['Data_atual'] = datetime.date.today()
    df['hora_atual'] = datetime.datetime.now().strftime("%H:%M:%S")

#     # Lê a planilha existente em um DataFrame
    try:
        df_existente = pd.read_excel('priorizadas_semana.xlsx')
    except FileNotFoundError:
        df_existente = pd.DataFrame()
        

# # Adiciona os novos registros ao DataFrame existente
df_final = pd.concat([df_existente, df])

# # Escreve o DataFrame de volta para a planilha
df_final.to_excel('priorizadas_semana.xlsx', index=False)





