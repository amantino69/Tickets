from bs4 import BeautifulSoup
import undetected_chromedriver as uc

driver = uc.Chrome()

# Navega para a URL
driver.get("https://ticket.crescer.net/#ticket/view/quedas_lentidoes_certificados")

# Obtém o código fonte da página
html_content = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the div element
div = soup.find('div')

# Extract the class, id, and custom attribute
class_attr = div.get('class')  # Returns ['my_class']
id_attr = div.get('id')  # Returns 'my_id'
custom_attr = div.get('custom_attr')  # Returns 'custom_value'

print(class_attr)
print(id_attr)
print(custom_attr)