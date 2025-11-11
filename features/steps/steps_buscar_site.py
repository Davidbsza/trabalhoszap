from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)

driver.get("https://web.whatsapp.com")
print("Escaneie o QR Code...")
time.sleep(20)

contato = "[QA IBTECH | AGO/25]"
mensagem = "Olá! Mensagem enviada automaticamente."

campo_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
campo_pesquisa.click()
campo_pesquisa.send_keys(contato)
time.sleep(2)
campo_pesquisa.send_keys(Keys.RETURN)

campo_msg = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
campo_msg.click()
campo_msg.send_keys(mensagem)
campo_msg.send_keys(Keys.RETURN)

print("Mensagem enviada!")
time.sleep(20)
driver.quit()
