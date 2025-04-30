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

#carrossel = carrosseis[0]

#xpath_botao_next = './../..//a[@class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage"]'
#botao_next = carrossel.find_element(By.XPATH, xpath_botao_next)
#botao_next.click()


carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')
for i in range(len(carrosseis)):
    print('=====================', titulos[i], '=====================')
    carrossel = carrosseis[i]
    while True:
        xpath = './/li[@class="a-carousel-card"]'
        cards = carrossel.find_elements(By.XPATH, xpath)

        for card in cards:
            sales_mov = card.find_element(By.XPATH, './/span[contains(@class, "sales-movement")]')
            nome_prod = card.find_element(By.XPATH, './/a[@class = "a-link-normal"]/span/div')
            print(sales_mov.text, nome_prod.text)

        posinset = cards[-1].get_attribute('aria-posinset')
        setsize = cards[-1].get_attribute('aria-setsize')
        if posinset == setsize:
            break
        else:
            xpath = './../..//a[@class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage"]'
            botao_next = carrossel.find_element(By.XPATH, xpath)
            botao_next.click()
            sleep(1)
    carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')
