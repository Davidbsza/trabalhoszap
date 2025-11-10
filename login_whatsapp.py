from selenium import webdriver
import time

# abrir navegador
navegador = webdriver.Microsoft.Edge()

# Acessar um site
navegador.get("https://web.whatsapp.com")

#Colocar o navegador em tela cheia
navegador.maximize_window()

# Selecionar um elemento na tela


time.sleep(5)