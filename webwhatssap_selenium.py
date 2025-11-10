from selenium import webdriver
# Ferramentas
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
import time 


# 1. Abertura do Navegador Edge


# Baixe o driver do Edge
service = EdgeService(EdgeChromiumDriverManager().install())

# Abrir maximizado
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")

# Abre o navegador
navegador = webdriver.Edge(service=service, options=options)


# 2. Acessar o WhatsApp Web


print("Abrindo WhatsApp Web...")
navegador.get("https://web.whatsapp.com")

# 3. Colocar o navegador em tela cheia
navegador.maximize_window()

# 4. Tempo de Espera para o Login
#  (1 minuto) para o usuário escanear o QR Code
print("Por favor, escaneie o QR Code no navegador. Você tem 60 segundos...")
time.sleep(60) 

# 5. Após o login, você pode começar a automatizar ações aqui
print("Fim da espera de login. O navegador continuará aberto por 10 segundos.")
time.sleep(10)

# Recomendação: feche o navegador ao terminar
navegador.quit()