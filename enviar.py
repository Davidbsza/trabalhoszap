from behave import given, when, then
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given("que o navegador Microsoft Edge está aberto")
def step_open_browser(context):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    context.driver = Edge(options=options)
    context.driver.get("https://web.whatsapp.com")

    print("Aguardando login no WhatsApp Web...")
    time.sleep(20)  # Tempo para escanear o QR Code manualmente


@when('eu pesquisar por um contato no WhatsApp')
def step_search_contact(context):
    campo_pesquisa = context.driver.find_element(
        By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'
    )

    contato = "[QA IBTECH | AGO/25]"  # 🔹 altere aqui o nome exato do contato

    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    time.sleep(2)
    campo_pesquisa.send_keys(Keys.RETURN)
    print(f"Contato '{contato}' selecionado com sucesso!")


@then("devo enviar uma mensagem pré-programada")
def step_send_message(context):
    mensagem = "Olá! Esta é uma mensagem automática enviada pelo Selenium "

    campo_msg = context.driver.find_element(
        By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'
    )

    campo_msg.click()
    campo_msg.send_keys(mensagem)
    campo_msg.send_keys(Keys.RETURN)

    print("Mensagem enviada com sucesso!")
    time.sleep(3)
    context.driver.quit()
