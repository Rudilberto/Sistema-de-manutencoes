import os
import pyscreeze
import time
import pyautogui as pt


class Image():
    pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False
    diretorio_atual = os.getcwd()

    aviso_atendimento = os.path.join(diretorio_atual, 'Imagens', 'aviso atendimento.PNG')
    confirmacao_atendimento = os.path.join(diretorio_atual, 'Imagens', 'confirmacao atendimento.PNG')
    confirmar_compra = os.path.join(diretorio_atual, 'Imagens', 'confirmar compra.PNG')
    f103aio = os.path.join(diretorio_atual, 'Imagens', 'F103AIO.PNG')
    f103emt = os.path.join(diretorio_atual, 'Imagens', 'F103EMT.PNG')
    f103prm = os.path.join(diretorio_atual, 'Imagens', 'F103PRM.PNG')
    f103rps = os.path.join(diretorio_atual, 'Imagens', 'F103RPS.PNG')
    f103smt = os.path.join(diretorio_atual, 'Imagens', 'F103SMT.PNG')
    f210ame = os.path.join(diretorio_atual, 'Imagens', 'F210AME.PNG')
    f210ssm = os.path.join(diretorio_atual, 'Imagens', 'F210SSM.PNG')
    f405gsa = os.path.join(diretorio_atual, 'Imagens', 'F405GSA.PNG')
    logo = os.path.join(diretorio_atual, 'Imagens', 'seniorlogo.PNG')
    pesquisa_registro = os.path.join(diretorio_atual, 'Imagens', 'pesquisa-registro.PNG')
    f207lot = os.path.join(diretorio_atual, 'Imagens', 'F207LOT.PNG')
    f000rpf = os.path.join(diretorio_atual, 'Imagens', 'F000RPF.PNG')
    f140gnf = os.path.join(diretorio_atual, 'Imagens', 'F140GNF.PNG')
    modelo501 = os.path.join(diretorio_atual, 'Imagens', 'modelo501.PNG')
    salvar = os.path.join(diretorio_atual, 'Imagens', 'salvar.PNG')

    def esperar_por_imagem(self, imagem):
        while not pt.locateOnScreen(imagem, confidence=0.9, grayscale=True):
            time.sleep(0.2)
        time.sleep(0.5)