from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com.br/')

sleep(10)

menu_hamburguer = driver.find_element(By.XPATH, '//a[@id="nav-hamburger-menu"]//span')
menu_hamburguer.click()

sleep(10)

caixa_prod_alta = driver.find_element(By.XPATH, '//ul/li/a[text()="Produtos em alta"]')
caixa_prod_alta.click()

sleep(2)

carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')
i = 0
while i < len(carrosseis):
  carrossel = carrosseis[i]
  action = ActionChains(driver)
  action.scroll_to_element(carrossel)
  action.perform()
  sleep(1)
  carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')
  i += 1

xpath_titulos = '//div[@class="a-row a-carousel-header-row a-size-large"]//h2[@class="a-carousel-heading a-inline-block"]'
titulos = driver.find_elements(By.XPATH, xpath_titulos)
titulos = [t.text.replace('Produtos em alta em ', '') for t in titulos]
print(titulos)
