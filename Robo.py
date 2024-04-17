from AutomacaoSenior import AutomacaoSenior
from Manutencao import Manutencao
from Nota import Nota
import time
import pyautogui as pt
import os
import tkinter as tk
from tkinter import font

class Robo(AutomacaoSenior, Manutencao, Nota):
    icone = os.path.join(AutomacaoSenior.diretorio_atual, 'Imagens', 'icon_nelson.ico')


    @staticmethod
    def verificar_texto(mensagem):
        while True:
            texto = pt.prompt(text=mensagem)
            if not texto:
                pt.alert(text='Valor inválido', title='Erro de digitação')     
            else:    
                break

        return texto.lower()


    @staticmethod
    def verificar_numero(mensagem):
        while True:
            numero = pt.prompt(text=mensagem)
            if numero is None:
                pt.alert(text='Valor inválido', title='Erro de digitação')

            elif not numero:
                pt.alert(text='Valor inválido', title='Erro de digitação')

            else:
                try:
                    numero = int(numero)
                    if numero <= 0:
                        pt.alert(text='Valor inválido. Digite um número maior que zero.', title='Erro de digitação')
                    else:
                        break
                    
                except ValueError:
                    pt.alert(text='Valor inválido. Digite um número válido.', title='Erro de digitação')

        return numero


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
            self.janela.destroy()

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


    def configurar_janela(self):
        # Adiciona o titulo
        self.janela.title('Sistema de automações Nelson Wendt')
        # Adiciona o icone superior
        self.janela.iconbitmap(self.icone)
        # Ajusta o tamanho da janela
        self.janela.geometry('418x210+300+280')
        # Coloca o fundo branco
        self.janela.configure(bg='#fff')


    def criar_botoes(self):
        # Botões
        botao_manutencoes = tk.Button(font=self.fonte, text='Manutenções', command=self.fazer_manutencao, width=19, height=2, bg='#fbff07', fg='#2d4390')
        botao_manutencoes.grid(row=0, column=0, padx=14, pady=10, sticky='nsew')

        botao_manutencoes_comprar = tk.Button(font=self.fonte, text='Manutenções e Comprar', command=self.fazer_manutencao_comprar, width=19, height=2, bg='#fbff07', fg='#2d4390')
        botao_manutencoes_comprar.grid(row=0, column=1, padx=14, pady=10, sticky='nsew')

        botao_comprar_material = tk.Button(font=self.fonte, text='Comprar Material', command=self.comprar_material, width=19, height=2, bg='#fbff07', fg='#2d4390')
        botao_comprar_material.grid(row=1, column=0, padx=14, pady=10, sticky='nsew')

        baixar_notas = tk.Button(font=self.fonte, text='Baixar Notas', command=self.baixar_nota, width=19, height=2, bg='#fbff07', fg='#2d4390')
        baixar_notas.grid(row=1, column=1, padx=14, pady=10, sticky='nsew')

        emitir_nota_efluente = tk.Button(font=self.fonte, text='Emitir Nota Efluente', command=self.emitir_nota_efluente, width=19, height=2, bg='#fbff07', fg='#2d4390')
        emitir_nota_efluente.grid(row=2, column=0, padx=14, pady=10, sticky='nsew')

    
    def criar_interface(self):
        self.janela = self.janela = tk.Tk()
        self.fonte = font.Font(family='Roboto', size=12)
        self.configurar_janela()
        self.criar_botoes()
        self.janela.mainloop()