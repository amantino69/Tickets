#####################################

from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def highlight_element(driver, locator):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].setAttribute('style', 'border: 2px solid red;');", element)
    return element

# Carrega a planilha do Excel
wb = load_workbook(r'C:\Users\Regina Casoti\Documents\Vivver\Tickets_Vivver.xlsx')
sheet = wb['Todos']

# Cria uma lista com os valores da coluna Ticket
tickets = [cell.value for cell in sheet['A'] if cell.value is not None]

# Cria uma nova instância do Google Chrome
driver = webdriver.Chrome()

# Vai para a página do sistema Ticket
driver.get('https://ticket.crescer.net')

# Faz login no sistema Ticket
username = highlight_element(driver, (By.ID, 'id_do_campo_de_usuario'))  # Substitua 'id_do_campo_de_usuario' pelo ID correto
password = highlight_element(driver, (By.ID, 'id_do_campo_de_senha'))  # Substitua 'id_do_campo_de_senha' pelo ID correto
username.send_keys('claudio.vieira@vivver.com.br')
password.send_keys('ticket#2023')
login_button = highlight_element(driver, (By.ID, 'id_do_botao_de_login'))  # Substitua 'id_do_botao_de_login' pelo ID correto
login_button.click()

# Busca o estado de cada ticket
for ticket in tickets:
    # Entra na página do ticket
    driver.get(f'http://www.sistema-ticket.com/tickets/{ticket}')

    # Busca e destaca o estado do ticket
    status = highlight_element(driver, (By.ID, 'status'))
    print(f'Ticket: {ticket}, Status: {status.text}')

driver.quit()
