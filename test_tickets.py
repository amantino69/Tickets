import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pandas as pd
import datetime
import re
from openpyxl import load_workbook
from selenium.webdriver.support.ui import Select

class TestTicketAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Chrome driver
        webdriver_options = Options()
        webdriver_options.add_experimental_option('detach', True)
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        webdriver_options.add_experimental_option("prefs", prefs)
        cls.driver = webdriver.Chrome(service=Service('venv\\chromedriver.exe'), options=webdriver_options)
        cls.wait = WebDriverWait(cls.driver, 20)

    def setUp(self):
        # Open the website
        self.driver.get("https://ticket.crescer.net")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_login(self):
        # Find the login and password fields
        campo_email = self.driver.find_element(By.XPATH, "//*[@id='username']")
        campo_senha = self.driver.find_element(By.XPATH, "//*[@id='password']")

        # Enter the login and password
        campo_email.send_keys("claudio.vieira@vivver.com.br")
        campo_senha.send_keys("ticket#2023")

        # Click on the login button
        elemento = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/button')))
        elemento.click()

        # Wait for the page to load
        sleep(10)

        # Check if the login was successful by verifying the presence of an element on the page
        try:
            self.driver.find_element(By.XPATH, '//*[@id="content_permanent_TicketOverview"]/div[3]/div[1]/div[1]/div/a[2]/span[1]')
        except NoSuchElementException:
            self.fail("Login failed")

    def test_search_ticket(self):
        # Find the search field
        elemento = self.driver.find_element(By.XPATH, '//*[@id="navigation"]/div[1]/form/div[2]')
        elemento.click()

        # Find the search input field
        elemento = self.driver.find_element(By.XPATH, '//*[@id="global-search"]')

        # Enter a ticket number to search
        elemento.send_keys("12345")

        # Wait for the search results to load
        sleep(10)

        # Check if the search results contain the expected ticket number
        try:
            self.driver.find_element(By.XPATH, f'//*[@id="content_permanent_Ticket-{ticket_number}"]/div/div[2]/div/div[2]/div/div[3]/small/time')
        except NoSuchElementException:
            self.fail("Ticket search failed")

    def test_prioritize_tickets(self):
        # Find the prioritize button
        elemento = self.driver.find_element(By.XPATH, '//*[@id="navigation"]/div[2]/a[1]/span')
        elemento.click()

        # Find the search input field
        elemento = self.driver.find_element(By.XPATH, '//*[@id="global-search"]')

        # Enter a ticket number to prioritize
        elemento.send_keys("12345")

        # Wait for the prioritize button to appear
        sleep(10)

        # Find the prioritize select element
        elemento = self.driver.find_element(By.XPATH, f'//*[@id="Ticket_{i}_priorizada"]')

        # Create a Select object
        select = Select(elemento)

        # Select the priority level
        select.select_by_value("1")

        # Check if the priority level was set successfully
        selected_option = select.first_selected_option
        self.assertEqual(selected_option.get_attribute("value"), "1")

if __name__ == '__main__':
    unittest.main()