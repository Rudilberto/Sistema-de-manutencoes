from AutomacaoSenior import AutomacaoSenior
from Manutencao import Manutencao
from Nota import Nota
from Estoque import Estoque
import time
import pyautogui as pt


class Robo(AutomacaoSenior, Manutencao, Nota, Estoque):

    def confirmar_manutencao(self):
        confirmacao_manutencao = pt.confirm(text='''O programa fará as manutenções agora, 
feche todas as janelas do programa senior, ligue o Caps Lock 
e não mecha no computador até ele terminar, 
ou se preferir clique em cancelar para cancelar a manutenção''')

        time.sleep(0.4)

        # Começa o programa

        if confirmacao_manutencao == 'Cancel':
            pt.confirm(text='''Manutenções canceladas!''')
            
        else:
            self.window.destroy()

            pt.PAUSE = 0.8
            # Acha o programa
            pt.hotkey('alt', 'tab')
            time.sleep(1.5)

            while not pt.locateOnScreen(f'{self.logo}', confidence=0.9, grayscale=True):
                time.sleep(1)
                pt.hotkey('alt', 'shift', 'tab')

        return confirmacao_manutencao  


    def loop_quantidade_manutencoes(self, quantidade_manutencoes, dicionario_manutencoes):
        for i in range(quantidade_manutencoes):
            self.solicitar_manutencao(dicionario_manutencoes, i)
            self.programar_emitir()
            self.requisitar_produto(dicionario_manutencoes, i)
            self.atender()
            self.finalizar_manutencao()

            if i == quantidade_manutencoes - 1:
                pt.confirm(text='''Manutenções concluidas!''')
                break

        self.criar_interface()


    def fazer_manutencao(self):       
        dicionario_manutencoes, quantidade_manutencoes = self.gerar_dicionario_manutencoes()
        confirmacao_manutencao = self.confirmar_manutencao()
        
        if confirmacao_manutencao == 'Cancel':
            pass
        else:
            self.loop_quantidade_manutencoes(quantidade_manutencoes, dicionario_manutencoes)

                     
    def loop_quantidade_manutencoes_comprar(self, quantidade_manutencoes, dicionario_manutencoes):
        for i in range(quantidade_manutencoes):            
            self.comprar_produto(dicionario_manutencoes, i)
            self.solicitar_manutencao(dicionario_manutencoes, i)
            self.programar_emitir()
            self.requisitar_produto(dicionario_manutencoes, i)
            self.atender()
            self.finalizar_manutencao()

            if i == quantidade_manutencoes - 1:
                pt.confirm(text='''Manutenções concluidas!''')
                break

        self.criar_interface()

        
    def fazer_manutencao_comprar(self):
        dicionario_manutencoes, quantidade_manutencoes = self.gerar_dicionario_manutencoes_compras()
        confirmacao_manutencao = self.confirmar_manutencao()
        
        if confirmacao_manutencao == 'Cancel':
            pass
        else:
            self.loop_quantidade_manutencoes_comprar(quantidade_manutencoes, dicionario_manutencoes)

    
    def loop_comprar_material(self, quantidade_manutencoes, dicionario_manutencoes):
        for i in range(quantidade_manutencoes):
            self.solicitar_manutencao(dicionario_manutencoes, i)
            self.programar_emitir()
            self.requisitar_produto(dicionario_manutencoes, i)
            self.atender_comprar(dicionario_manutencoes, i)

            if i == quantidade_manutencoes - 1:
                pt.confirm(text='''Manutenções concluidas!''')
                break

        self.criar_interface()


    def comprar_material(self):
        dicionario_manutencoes, quantidade_manutencoes = self.gerar_dicionario_manutencoes_compras()
        confirmacao_manutencao = self.confirmar_manutencao()
        
        if confirmacao_manutencao == 'Cancel':
            pass
        else:
            self.loop_comprar_material(quantidade_manutencoes, dicionario_manutencoes)


    def arrumar_estoque(self):
        self.window.destroy()

        codigos, quantidade, observacao, conta_contabil, centro_custo = self.tratar_arquivo_final()
        self.requisitar_material_estoque(codigos, quantidade, observacao, conta_contabil, centro_custo)
        self.atender_material_requisitado(codigos)

        self.criar_interface()


    def emitir_nota_efluente(self):
        self.window.destroy()
        
        self.nota_efluente()
        pt.alert(text='Nota fiscal salva na pasta downloads!')

        self.criar_interface()

    
    def baixar_relatorio_equipamento(self):
        quantidade_relatorios = self.gerar_quantidade_iteracoes('Digite quantos relatórios serão feitos')

        lista_equipamento = [self.verificar_texto(f'Digite o nome do {i + 1}° equipamento: ') for i in range(quantidade_relatorios)]

        pt.alert(text='Iniciando download de relatorios', title='alerta')

        self.window.destroy()

        pt.PAUSE = 0.8

        pt.hotkey('alt', 'tab')
        while not pt.locateOnScreen(self.logo, confidence=0.9, grayscale=True):
            pt.hotkey('alt','shift','tab')
            time.sleep(0.2)


        for equipamento in lista_equipamento:
            self.relatorio_equipamento(equipamento)
            time.sleep(2)
        
        pt.alert(text='Relatorios baixados!')
        self.criar_interface()

    
    def baixar_relatorio_nfs(self):

        data_relatorio = self.verificar_texto('Digite a data para o relatório:')
        pt.alert(text='Iniciando download de relatorios', title='alerta')

        self.window.destroy()

        pt.PAUSE = 0.8

        while not pt.locateOnScreen(self.logo, confidence=0.9, grayscale=True):
            pt.hotkey('alt','shift','tab')
            time.sleep(0.2)

        self.relatorio_nfs(data_relatorio)

        pt.alert(text='Relatorios baixados!')
        self.criar_interface()