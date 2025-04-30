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

 # Abre menu hamburguer
menu_hamburguer = driver.find_element(By.XPATH, '//a[@aria-label="Abrir Menu"]/span[text()="Todos"]')
menu_hamburguer.click()
sleep(1)

# Abre clica na caixa de Produtos em alta
caixa_prod_alta = driver.find_element(By.XPATH, '//a[@class="hmenu-item" and text()="Produtos em alta"]')
caixa_prod_alta.click()
sleep(1)
 
 # Scrola para fazer load de todos carroseis
carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')

i = 0
while i < len(carrosseis):
    carrosel = carrosseis[i]
    ActionChains(driver).scroll_to_element(carrosel).perform()
    sleep(1)
    carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')
    i+= 1
 
 # Pega todos titulos
titulos = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]/../../../..//h2')
titulos = [t.text.replace('Produtos em alta em ', '') for t in titulos]
sleep(1)

for i in range(len(titulos)):
    maior_item = 0
    while True:
        # Pega todos os cards do carrossel
        carrosseis = driver.find_elements(By.XPATH, '//div[contains(@id, "anonCarousel")]')
        carrosel = carrosseis[i]
        itens_carrossel = carrosel.find_elements(By.XPATH, f'.//li[@class="a-carousel-card"]')
        
        # Verifica se card já foi contabilizado
        if int(itens_carrossel[0].get_attribute('aria-posinset')) > maior_item:
            maior_item = int(itens_carrossel[0].get_attribute('aria-posinset'))
        else:
            break

        for item in itens_carrossel:
            if not item.get_attribute('aria-hidden') == 'true':
                modificacao = item.find_element(By.XPATH, './/span[contains(@class, "carousel-sales-movement")]')
                print(titulos[i], modificacao.text)
                # Clica no botão de next
                botao_seguir = carrosel.find_element(By.XPATH, './../..//a[@class="a-button a-button-image a-carousel-button a-carousel-goto-nextpage"]')
                botao_seguir.click()
                sleep(2)