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
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select

def init_driver():
    webdriver_options = Options()
    webdriver_options.add_experimental_option('detach', True)
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    webdriver_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service('venv\\chromedriver.exe'), options=webdriver_options)
    return driver

def login(driver, email, password):
    driver.get("https://ticket.crescer.net")
    campo_email = driver.find_element(By.XPATH, "//*[@id='username']")
    campo_senha = driver.find_element(By.XPATH, "//*[@id='password']")
    campo_email.send_keys(email)
    campo_senha.send_keys(password)
    elemento = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/button')))
    elemento.click()

def get_dataframe_from_html(driver):
    sleep(10)
    elemento = driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]')
    html_interior = elemento.get_attribute('innerHTML')
    df = pd.read_html(html_interior, index_col=0)[0].copy()
    df.rename(columns={'#': 'ticket', 'Unnamed: 1': 'Status'}, inplace=True)
    return df

def process_ticket_list(driver, df):
    lista = df['ticket'].tolist()
    lista = [x for x in lista if x.isdigit()]
    for i in lista:
        process_ticket(driver, df, i)

def process_ticket(driver, df, i):
    sleep(5)
    try:
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[1]/form/div[2]')
        elemento.click()
    except:
        pass    
    try:
        elemento = driver.find_element(By.XPATH, '//*[@id="navigation"]/div[2]/a[1]/span')
        elemento.click()
    except:
        pass    
    elemento = driver.find_element(By.XPATH, '//*[@id="global-search"]')
    elemento.clear()
    sleep(5)
    elemento = driver.find_element(By.XPATH, '//*[@id="global-search"]')
    elemento.send_keys(i)
    sleep(30)
    index = df[df['ticket'] == i].index[0]
    sleep(5)
    elementos = driver.find_elements(By.XPATH, '//*[contains(@id, "content_permanent_Ticket-")]')
    for index, elemento in enumerate(elementos):
        if elemento.is_displayed() and elemento.is_enabled():
            elemento.click()
            sleep(5)
            df.loc[index, 'descrição'] = elemento.text
            driver.execute_script("arguments[0].style.border='3px solid red'", elemento)

def main():
    driver = init_driver()
    login(driver, "claudio.vieira@vivver.com.br", "ticket#2023")
    df = get_dataframe_from_html(driver)
    process_ticket_list(driver, df)

if __name__ == "__main__":
    main()