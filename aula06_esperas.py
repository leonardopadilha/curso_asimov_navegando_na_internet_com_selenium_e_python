from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.selenium.dev/selenium/web/dynamic.html')

# apenas para praticar
driver.implicitly_wait(2)

xpath_id_box = 'box0'
xpath_id_input = 'revealed'

botao_add_box = driver.find_element(By.ID, 'adder')
botao_add_box.click()

wait = WebDriverWait(driver, timeout=3)
wait.until(EC.presence_of_all_elements_located((By.ID, xpath_id_box)))

xpath_botao_reveal_input = '//input[@value="Reveal a new input"]'
botao_reveal_input = driver.find_element(By.XPATH, xpath_botao_reveal_input)
botao_reveal_input.click()
text_input = wait.until(EC.visibility_of_element_located((By.ID, xpath_id_input)))
text_input.send_keys("Teste utilizando selenium webdriver com python")

