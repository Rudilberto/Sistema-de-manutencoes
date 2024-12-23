from datetime import datetime, timedelta
import time
import pyautogui as pt
from Image import Image


class AutomacaoSenior(Image):
    data_atual = datetime.now().date()
    data_atual = data_atual.strftime('%d/%m/%Y')
    
    def comprar_produto(self, dicionario_manutencoes, i):
        '''Compra o produto'''

    # Entra na janela de compra de produtos #
        time.sleep(1)
        pt.PAUSE = 0.8

        pt.press('f11')
        pt.write('F405GSA')
        pt.press('enter')

        self.esperar_por_imagem(self.f405gsa)

        pt.PAUSE = 0.3

        for produto, quantidade, cc in dicionario_manutencoes['produto_quantidade_descricao'][i]:
            pt.press('tab', presses=3)
            pt.press('f3')

            self.esperar_por_imagem(self.pesquisa_registro)
    # Entra na janela do produto digite e seleciona o produto a comprar #
        
            pt.hotkey('alt', 'a')
            pt.press('backspace')
            pt.write(produto)
            pt.hotkey('alt', 'i')
            pt.press('tab', presses=4)
            pt.press('enter')

            self.esperar_por_imagem(self.f405gsa)

            pt.press('tab', presses=2)
            pt.write('31')
            pt.press('tab')
            pt.write(str(quantidade))
            pt.press('tab', presses=2)
            pt.write(cc)
    # Mostrar, colocar conta contabil e observacao #

            pt.hotkey('alt', 'm')
            pt.press('tab', presses=7, interval=0.2)
            pt.write('32450')
            pt.hotkey('alt', 'a')
            pt.write(dicionario_manutencoes['descricao_compra'][i])
            pt.hotkey('alt', 'p')
            time.sleep(0.2)
            pt.hotkey('alt', 's')
            time.sleep(0.2)
            pt.hotkey('alt', 'o')

        pt.hotkey('ctrl', 'f4')


    def solicitar_manutencao(self, dicionario_manutencoes, i):
        '''Faz a solicitação da manutenção'''

        pt.PAUSE = 0.8
    # Entra na janela de solicitação de manutenção #

        pt.press('f11')
        pt.write('F103SMT')
        pt.press('enter')

        self.esperar_por_imagem(self.f103smt)

    # Entrar na tela para encontrar o equipamento #
        pt.press('f3')

        self.esperar_por_imagem(self.pesquisa_registro)

        pt.PAUSE = 0.3

        pt.hotkey('alt', 'a')
        pt.press('backspace')
        pt.write(dicionario_manutencoes['equipamento'][i])
        pt.hotkey('alt', 'i')
        time.sleep(0.6)
        pt.press('tab', presses=4, interval=0.08)
        pt.press('enter')

    # Faz a solicitação #
        self.esperar_por_imagem(self.f103smt)

        pt.press('tab', presses=4, interval=0.1)
        pt.write('700030001')
        pt.press('tab', presses=2)

        for _ in range(2):
            pt.write('01')
            pt.press('tab')

        pt.write(dicionario_manutencoes['descricao_manutencao'][i])

        pt.press('tab', presses=2)
        pt.write('18:30') 

        pt.press('tab', presses=3, interval=0.1)

        pt.press('enter', presses=2, interval=1)

        pt.hotkey('ctrl', 'f4')


    def programar_emitir(self):
        '''Apenas programa e emite a manutenção'''

    # Entra na tela de programação #
        time.sleep(1)
        pt.PAUSE = 0.8
        pt.press('f11')
        pt.write('F103PRM')
        pt.press('enter')

        self.esperar_por_imagem(self.f103prm)

        pt.PAUSE = 0.3
    # Programar #

        pt.hotkey('alt', '2')
        pt.hotkey('alt', 'm')
        pt.hotkey('alt', 'r')
        pt.hotkey('alt', 'p')
        pt.press('enter')

        time.sleep(0.5)

    # Emitir #
        pt.hotkey('alt', '3')
        pt.hotkey('alt', 'm')
        pt.hotkey('alt', 'r')
        pt.hotkey('alt', 'p')

        time.sleep(0.5)

        pt.hotkey('alt', 'o')

        pt.hotkey('ctrl', 'f4')


    def requisitar_produto(self,dicionario_manutencoes, i, data_atual=data_atual):
        '''Coloca o produto pedido dentro da manutenção'''

    # Entrar na janela do painel de controle #
        time.sleep(1)
        pt.PAUSE = 0.8
        pt.press('f11')
        pt.write('F103EMT')
        pt.press('enter')

        self.esperar_por_imagem(self.f103emt)
        
        pt.PAUSE = 0.3
        pt.press('tab', presses=3, interval=0.05)

    # Entra na janela para adicionar o equipamento #
        pt.press('f3')

        self.esperar_por_imagem(self.pesquisa_registro)

        pt.hotkey('alt', 'a')
        pt.hotkey('alt', 'i')
        pt.press('tab', presses=4, interval=0.08)
        pt.press('enter')

        self.esperar_por_imagem(self.f103emt)

    # Colocar data #
        pt.press('tab', presses=9, interval=0.05)
        pt.write(data_atual)
        pt.press('tab')
        pt.write(data_atual)

    # Mostrar, requisição e entrar na janela de requisitar produto #
        pt.hotkey('alt', 'm')
        pt.press('tab', presses=14, interval=0.1)
        pt.press('down', presses=10)
        pt.hotkey('alt', 'e')

        self.esperar_por_imagem(self.f103rps)

    # Colocar produtos na janela de requisição #
        for produto, quantia in dicionario_manutencoes['produto_quantidade'][i]:   
            pt.press('down')
            time.sleep(0.2)
            
            pt.press('f3')

            self.esperar_por_imagem(self.pesquisa_registro)
            
            pt.hotkey('alt', 'a')
            pt.press('backspace')
            pt.write(produto)
            pt.hotkey('alt', 'i')
            pt.press('tab', presses=4)
            pt.press('enter')

            self.esperar_por_imagem(self.f103rps)

            pt.press('tab', presses=2, interval=0.2)

            pt.write(quantia)
            
        pt.hotkey('alt', 'p')
        time.sleep(1)
        pt.press('enter')
        
        pt.hotkey('alt', 'f4')

        pt.hotkey('ctrl', 'f4')


    def atender(self, data_atual=data_atual):
        '''Atende o produto requisitado'''

    # Entrar na janela de atendimento #
        time.sleep(1)
        pt.PAUSE = 0.8
        pt.press('f11')
        pt.write('F210AME')
        pt.press('enter')

    # Seleciona o deposito 31 #
        self.esperar_por_imagem(self.f210ame)

        pt.PAUSE = 0.3
        pt.write('31')

    # Colocar data no atendimento #
        pt.press('tab')
        pt.write(data_atual)
        pt.press('tab')
        pt.write(data_atual)

    # Mostrar, Marcar, Processar
        pt.PAUSE = 0.3
        pt.hotkey('alt', 'e')

        self.esperar_por_imagem(self.f210ssm)

        pt.press('tab', presses=18)
        pt.press('f3')
        
        self.esperar_por_imagem(self.pesquisa_registro)
        
        pt.hotkey('alt', 'a')
        pt.hotkey('alt', 'i')
        time.sleep(0.6)
        pt.press('tab', presses=4, interval=0.08)
        pt.press('enter')
        
        self.esperar_por_imagem(self.f210ssm)

        pt.hotkey('alt', 'o')
        time.sleep(0.2)
        
        pt.hotkey('alt', 'm')
        pt.hotkey('alt', 'a')
        pt.hotkey('alt', 'p')

        self.esperar_por_imagem(self.confirmacao_atendimento)
        pt.hotkey('alt', 's')

        self.esperar_por_imagem(self.aviso_atendimento)
        pt.hotkey('alt', 'o')

        pt.hotkey('ctrl', 'f4')

    
    def atender_comprar(self, dicionario_manutencoes, i, data_atual=data_atual):
        '''Entra no atendimento e requisita os produtos'''
    # Entrar na janela de atendimento #
        time.sleep(1)
        pt.PAUSE = 0.8
        pt.press('f11')
        pt.write('F210AME')
        pt.press('enter')

    # Mostrar, Marcar, Processar
        for produto, quantidade in dicionario_manutencoes['produto_quantidade'][i]:
            # Seleciona o deposito 31 #
            self.esperar_por_imagem(self.f210ame)

            pt.PAUSE = 0.3
            pt.write('31')

        # Colocar data no atendimento #
            pt.press('tab')
            pt.write(data_atual)
            pt.press('tab')
            pt.write(data_atual)
            pt.PAUSE = 0.3
            pt.hotkey('alt', 'e')

            self.esperar_por_imagem(self.f210ssm)
            pt.press('tab', presses=14, interval=0.07)
            pt.press('f3')

            self.esperar_por_imagem(self.pesquisa_registro)

            pt.hotkey('alt', 'a')
            pt.press('backspace')
            pt.write(produto)
            pt.hotkey('alt', 'i')
            pt.press('tab', presses=4, interval=0.05)
            pt.press('enter')

            self.esperar_por_imagem(self.f210ssm)

            pt.press('tab', presses=4)
            pt.press('f3')
            
            self.esperar_por_imagem(self.pesquisa_registro)
            
            pt.hotkey('alt', 'a')
            pt.hotkey('alt', 'i')
            time.sleep(0.6)
            pt.press('tab', presses=4, interval=0.08)
            pt.press('enter')
            
            self.esperar_por_imagem(self.f210ssm)

            pt.hotkey('alt', 'o')
            time.sleep(0.2)
            pt.hotkey('alt', 'm')

            pt.press('tab')
            pt.write('0')

            pt.press('tab')
            pt.write(quantidade)
            
            pt.hotkey('alt', 'j')
            pt.write(dicionario_manutencoes['descricao_compra'][i])
        
            pt.hotkey('alt', 'p')

            self.esperar_por_imagem(self.confirmacao_atendimento)
            pt.hotkey('alt', 's')

            self.esperar_por_imagem(self.confirmar_compra)
            pt.hotkey('alt', 'n')
            time.sleep(0.5)

        pt.hotkey('ctrl', 'f4')


    def finalizar_manutencao(self, data_atual=data_atual):
        '''Volta no painel de controle e aponta a manutenção'''
        
        time.sleep(1)
        pt.PAUSE = 0.8
        pt.press('f11')
        pt.write('F103EMT')
        pt.press('enter')
        
        self.esperar_por_imagem(self.f103emt)

        pt.PAUSE = 0.3
        pt.press('tab', presses=3, interval=0.05)

    # Entra na janela para adicionar o equipamento #
        pt.press('f3')

        self.esperar_por_imagem(self.pesquisa_registro)

        pt.hotkey('alt', 'a')
        pt.hotkey('alt', 'i')
        pt.press('tab', presses=4, interval=0.08)
        pt.press('enter')

        self.esperar_por_imagem(self.f103emt)

    # Colocar data #
        pt.press('tab', presses=9, interval=0.05)
        pt.write(data_atual)
        pt.press('tab')
        pt.write(data_atual)

    # Mostrar, requisição e entrar na janela de requisitar produto #
        pt.hotkey('alt', 'm')
        pt.press('tab', presses=14, interval=0.1)
        pt.press('down', presses=10)
        
        pt.hotkey('alt', 'n')

        self.esperar_por_imagem(self.f103aio)

        pt.press('tab', presses=2)
        pt.write('58')
        pt.press('tab', presses=2)
        pt.write(data_atual)
        pt.press('tab')
        pt.write('0750')
        pt.press('tab')
        pt.write(data_atual)
        pt.press('tab')
        pt.write('0750')
        pt.press('tab', presses=3)
        pt.press('space')

        pt.hotkey('alt', 'p')
        time.sleep(0.8)
        pt.hotkey('alt', 'p')
        time.sleep(1.5)
        pt.hotkey('alt', 'o')

        self.esperar_por_imagem(self.f103emt)

    # Fecha tudo para fazer a proxima manutenção #
        pt.hotkey('ctrl', 'f4')
        time.sleep(1.5)

    
    def requisitar_material_estoque(self, codigos, quantidade, observacao, conta_contabil, centro_custo):
        pt.PAUSE = 0.60

        pt.alert(text='Começando o acerto de estoque!')

        pt.hotkey('alt', 'shift', 'tab')

        while not pt.locateOnScreen(f'{self.logo}', confidence=0.9, grayscale=True):
            time.sleep(1)
            pt.hotkey('alt', 'shift', 'tab')

        pt.press('f11')
        pt.write('f207lot')
        pt.press('enter')

        self.esperar_por_imagem(self.f207lot)

        pt.press('tab', presses=19, interval=0.2)

        for i in range(len(codigos)):
            pt.write(codigos[i])
            pt.press('tab', presses=3)
            pt.write(str(quantidade[i]))
            pt.press('tab')
            pt.write(conta_contabil[i])
            pt.press('tab')
            pt.write(centro_custo[i])
            pt.press('tab')
            pt.write(observacao[i])
            pt.press('down') 
            time.sleep(0.65)

        pt.press('esc')
        pt.hotkey('alt', 'p')
        time.sleep(1)
        pt.hotkey('alt', 's')
        time.sleep(0.5)
        pt.hotkey('alt', 'o')

        pt.hotkey('ctrl', 'f4')
        time.sleep(2)

    
    def atender_material_requisitado(self, codigos):
        pt.PAUSE = 0.60
        
        pt.press('f11')
        pt.write('f210ame')
        pt.press('enter')

        self.esperar_por_imagem(self.f210ame)

        pt.write('31')
        for _ in range(2):
            pt.press('tab')
            pt.write(self.data_atual)

        pt.hotkey('alt', 'm')
        time.sleep(5)

        pt.hotkey('alt', 'p')
        time.sleep(1)
        pt.hotkey('alt', 's')
        time.sleep(1)

        for _ in range(len(codigos)):
            self.esperar_por_imagem(self.f000rpf)
            time.sleep(0.8)

            pt.hotkey('alt', 'o')
        
        pt.press('enter', presses=2, interval=0.8)

    
    def relatorio_equipamento(self, equipamento, data_atual=data_atual):
        '''Baixa relatorios de equipamento do modelo nw - 500'''

        pt.PAUSE = 0.9
        pt.keyDown('alt')
        pt.press('n')
        pt.press('r')
        pt.keyUp('alt')

        self.esperar_por_imagem(self.modelo501)

        pt.PAUSE = 0.3

        pt.press('tab', presses=2, interval=0.2)
        pt.press('f3')

        self.esperar_por_imagem(self.pesquisa_registro)

        pt.hotkey('alt', 'a')
        pt.press('backspace')
        pt.write(equipamento)
        pt.hotkey('alt', 'i')
        time.sleep(0.6)
        pt.press('tab', presses=4, interval=0.08)
        pt.press('enter')   

        self.esperar_por_imagem(self.modelo501)
        pt.press('tab')

        # TODO Arrumar para quando não haver manutenções naquele dia
        pt.write(data_atual)

        pt.hotkey('alt', 'o')

        pt.PAUSE = 0.9

        self.esperar_por_imagem(self.salvar)
        imagem = pt.locateCenterOnScreen(self.salvar, confidence=0.9, grayscale=True)

        pt.click(imagem)
        pt.write(equipamento)
        pt.press('tab')
        pt.press('down', presses=18, interval=0.09)
        time.sleep(1)
        pt.press('enter')
        pt.press('tab', presses=3, interval=0.5)
        pt.press('down')
        time.sleep(1)
        pt.press('r', presses=2, interval=1)
        time.sleep(1)
        pt.press('enter', presses=2, interval=0.5)
        time.sleep(5)
        pt.hotkey('alt', 'f4')

    
    def relatorio_nfs(self, data_relatorio):
        '''Gera e guarda em pdf relatórios do modelo 201'''

        pt.PAUSE = 0.9
        pt.keyDown('alt')
        pt.press('t')
        pt.press('r')
        pt.keyUp('alt')

        self.esperar_por_imagem(self.modelo201)

        pt.press('tab', presses=5, interval=0.15)

        pt.PAUSE = 0.4

        pt.write(data_relatorio)

        pt.PAUSE = 0.9

        pt.hotkey('alt', 'o')

        # Pergunta se o usuario deseja ou não salvar o relatorio
        time.sleep(2)
        continuar = pt.confirm(text='Deseja salvar o relatório?')

        if continuar == 'OK':
            pt.PAUSE = 0.8
            time.sleep(1)
            self.esperar_por_imagem(self.salvar)
            imagem = pt.locateCenterOnScreen(self.salvar, confidence=0.9, grayscale=True)
            pt.click(imagem)

            time.sleep(1.5)

            datahora = datetime.now()
            datahora = datahora.strftime('%d-%m-%Y, %H-%M-%S')

            pt.write(datahora)
            pt.press('tab')
            pt.press('down', presses=18, interval=0.09)
            pt.press('enter')
            pt.press('tab', presses=3, interval=0.1)
            time.sleep(1)
            pt.press('down')
            time.sleep(1.5)
            self.esperar_por_imagem(self.areadetrabalho)
            pt.press('up', presses=5, interval=0.1)
            pt.press('enter')
            pt.press('tab', presses=2, interval=0.1)
            pt.press('down', presses=9, interval=0.1)
            pt.press('enter')
            pt.hotkey('alt', 'l')
