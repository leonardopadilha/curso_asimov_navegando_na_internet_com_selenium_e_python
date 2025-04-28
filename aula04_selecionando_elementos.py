from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.ibge.gov.br/')

barra_busca = driver.find_element(By.ID, "mod-search-searchword")
barra_busca.send_keys("Inflação")

barra_busca.clear()

barra_busca_name = driver.find_element(By.NAME, "searchword")
barra_busca_name.send_keys("População")
barra_busca_name.clear()

data_noticia = driver.find_element(By.CLASS_NAME, "home-noticia-data")
print(data_noticia.text)

datas_noticias = driver.find_elements(By.CLASS_NAME, "home-noticia-data")
print()
for datas in datas_noticias:
  print(datas.text)

links = driver.find_elements(By.TAG_NAME, "a")
print()
for link in range(len(links)):
    if link < 10:
      print(f"contagem - {link}")
      #print(links[link].get_attribute('href'))
