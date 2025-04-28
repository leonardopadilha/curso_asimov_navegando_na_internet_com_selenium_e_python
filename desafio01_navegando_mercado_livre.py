from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.mercadolivre.com.br/ofertas')

corrosseis = driver.find_elements(By.CLASS_NAME, 'carousel_item')

for i in range(len(corrosseis)):
    carrossel = corrosseis[i]

    if not carrossel.is_displayed():
        botao_seguinte = driver.find_element(By.CLASS_NAME, 'andes-carousel-snapped__control--next')
        botao_seguinte.click()
        sleep(1)
        corrosseis = driver.find_elements(By.CLASS_NAME, 'carousel_item')
        carrossel = corrosseis[i]

    carrossel.click()
    sleep(1)
    corrosseis = driver.find_elements(By.CLASS_NAME, 'carousel_item')
    carrossel = corrosseis[i]

    nome_carrossel = carrossel.find_element(By.TAG_NAME, 'p').text

    itens_promocao = driver.find_elements(By.CLASS_NAME, 'promotion-item__description')
    for item in itens_promocao:
        descricao = item.find_element(By.CLASS_NAME, 'promotion-item__title').text
        if len(item.find_elements(By.CLASS_NAME, 'andes-money-amount__discount')) == 0:
            desconto = '0% OFF'
        else:
            desconto = item.find_element(By.CLASS_NAME, 'andes-money-amount__discount').text
        print(nome_carrossel, '|', descricao, '|', desconto)
        