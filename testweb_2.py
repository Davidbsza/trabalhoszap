# ============================================================
# 🧩 Importação das bibliotecas necessárias
# ============================================================

from behave import given, when, then  
# Importa as anotações (decorators) do framework Behave, que são usadas para
# definir etapas do comportamento BDD:
# @given → representa o "Dado que"
# @when  → representa o "Quando"
# @then  → representa o "Então"
# Elas conectam o texto escrito no arquivo .feature com o código que o executa.

from selenium.webdriver import Edge  
# Importa o driver do navegador Microsoft Edge, usado pelo Selenium para controlar o navegador.

from selenium.webdriver.edge.options import Options  
# Importa a classe Options, que permite configurar parâmetros do navegador (como tela cheia, logs, etc).

from selenium.webdriver.common.by import By  
# Classe que define os diferentes tipos de seletores (estratégias para localizar elementos na página),
# como: By.ID, By.NAME, By.XPATH, By.CSS_SELECTOR, etc.

from selenium.webdriver.common.keys import Keys  
# Permite simular o uso de teclas do teclado, como ENTER, TAB, SETA, etc.

import time  
# Biblioteca padrão do Python usada aqui para adicionar pausas (delays) entre as ações.
# Isso garante que a página tenha tempo de carregar antes do próximo comando.

# ============================================================
# 🧠 Definição dos passos do teste BDD (Gherkin)
# ============================================================


# ----------------------------------------
# 1️⃣ Etapa "DADO QUE..."
# ----------------------------------------
@given("que o navegador Microsoft Edge está aberto")
def step_open_browser(context):
    # Cria um objeto de configuração do navegador
    options = Options()

    # Inicia o navegador maximizado (em tela cheia)
    options.add_argument("--start-maximized")

    # Desativa a detecção de automação (impede que sites saibam que o navegador é controlado por Selenium)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Remove mensagens de log desnecessárias no terminal (de "DevTools" e "EdgeAuth")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Inicializa o navegador Edge com as opções definidas acima
    context.driver = Edge(options=options)

    # Abre diretamente o site do WhatsApp Web
    context.driver.get("https://web.whatsapp.com")

    print("Aguardando login no WhatsApp Web...")
    time.sleep(20)  # tempo para escanear o QR Code manualmente


# ----------------------------------------
# 2️⃣ Etapa "QUANDO..."
# ----------------------------------------
@when('eu pesquisar por um contato no WhatsApp')
def step_search_contact(context):
    # Localiza o campo de pesquisa (barra lateral esquerda)
    campo_pesquisa = context.driver.find_element(
        By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'
    )

    contato = "[QA IBTECH | AGO/25]"  # 🔹 altere aqui o nome que aparece no WhatsApp

    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.RETURN)
    print(f"Contato '{"contato"}' selecionado com sucesso!")


# ----------------------------------------
# 3️⃣ Etapa "ENTÃO..."
# ----------------------------------------
@then("devo enviar uma mensagem pré-programada")
def step_send_message(context):
    mensagem = "Olá!  Esta é uma mensagem automática enviada pelo Selenium."
    
    # Localiza a caixa de digitação da mensagem
    campo_msg = context.driver.find_element(
        By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'
    )

    campo_msg.click()
    campo_msg.send_keys(mensagem)
    campo_msg.send_keys(Keys.RETURN)

    print("Mensagem enviada com sucesso!")
    time.sleep(3)
    context.driver.quit()