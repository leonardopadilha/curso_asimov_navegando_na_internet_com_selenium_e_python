from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.selenium.dev/selenium/web/web-form.html')
text_box = driver.find_element(by=By.NAME, value='my-text')
text_box.send_keys('Selenium')

submit_button = driver.find_element(by=By.CSS_SELECTOR, value='button')
submit_button.click()

message = driver.find_element(by=By.ID, value='message')
print('Mensagem final', message.text)

sleep(5)