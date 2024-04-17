import pyautogui as pt
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Nota():

    def baixar_nota(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        service = Service(ChromeDriverManager().install())

        nota = pt.prompt(text='Digite o numero da nota: ')

        navegador = webdriver.Chrome(options=options, service=service)

        # link edocs
        navegador.get(r'http://192.168.0.13/SDE/Login.aspx?ReturnUrl=%2fsde%2f')

        # logar no edocs
        navegador.find_element('xpath', '//*[@id="txbLogin"]').send_keys('nfe')
        navegador.find_element('xpath', '//*[@id="txbSenha"]').send_keys('nfe')
        time.sleep(1)
        navegador.find_element('xpath', '//*[@id="btnLogin"]').click()

        # Entrar nas emissoes
        navegador.find_element('xpath', '//*[@id="acdMenu"]/div[3]').click()
        time.sleep(1)
        navegador.find_element('xpath', '//*[@id="ctl13_lkbNfeEmissao"]').click()
        time.sleep(1)
        navegador.find_element('xpath', '//*[@id="btnFiltrarNfe"]').click()
        time.sleep(1)

        # Pesquisar nota
        navegador.find_element('xpath',
                                '//*[@id="filtrofltEmissao3"]').send_keys(nota, Keys.ENTER)
        time.sleep(1)

        # Baixa
        navegador.find_element('xpath', '//*[@id="nfeGridInfo"]').click()
        navegador.find_element('xpath', '//*[@id="btnDanfe"]').click()

        time.sleep(2)

        navegador.quit()
    

    def emitir_nota_efluente(self):
        kilos_efluente = pt.prompt(text='Digite a quantidade (Kilos) de efluente')
        volumes = pt.prompt(text='Digite quantos volumes')
        pt.alert(text='Não mexa no computador até a nota ser finalizada', title='alerta')

        time.sleep(2)
        pt.PAUSE = 0.8

    # Entra da tela de emissao de notas
        pt.press('f11')
        pt.write('F140GNF')
        pt.press('enter')

    # Coloca o fornecedor, transação e insere
        pt.press('tab', presses=4, interval=0.1)
        pt.write('1107')
        pt.press('tab')
        pt.write('5911l')
        pt.hotkey('alt', 'i')

    # Coloca o produto, quantidade e peso
        pt.press('tab', presses=4, interval=0.1)
        pt.write('85002011013')
        pt.press('tab', presses=4, interval=0.1)
        pt.write(kilos_efluente)
        pt.press('tab', presses=2)
        pt.write(kilos_efluente)
        pt.hotkey('shift', 'tab')
        pt.write(kilos_efluente)
        pt.press('tab', presses=3)
        pt.write('5')
        pt.press('up')
        time.sleep(1.5)

    # Colocar transportadora (Sao miguel = 650) e fechar a nota
        pt.hotkey('alt', 'y')
        time.sleep(2)
        pt.press('tab', presses=5)
        pt.write('650')
        pt.press('tab', presses=8, interval=0.2)
        pt.write(volumes)
        pt.press('tab')
        pt.write('13')
        pt.hotkey('alt', 'p')

    # Fechar a nota
        pt.PAUSE = 1.5
        pt.hotkey('alt', 'f')
        pt.hotkey('alt', 's')
        pt.hotkey('alt', 's')
        pt.hotkey('alt', 'o')
        pt.hotkey('alt', 'o')
