from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.globo.com/')

#span_esporte = driver.find_element(By.XPATH, '//span[text()="Esporte"]')
#span_esporte.click()

noticias = driver.find_elements(By.XPATH, '//a[@class="post__link"] //h2[@class="post__title"]')
for noticia in noticias:
  print(noticia.text)