from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys, ActionChains
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get('https://www.google.com.br')

campo_pesquisar = driver.find_element(By.XPATH, '//textarea[@title="Pesquisar"]')
acao = ActionChains(driver)
acao.click(on_element=campo_pesquisar)

acao.send_keys("Asimov")

acao.key_down(Keys.SHIFT)
acao.send_keys('asimov')

acao.key_up(Keys.SHIFT)
acao.perform() # Essa linha que executa as ações

sleep(10)