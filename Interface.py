from Robo import Robo
import tkinter as tk
from tkinter import font
import os


class Interface(Robo):
    def __init__(self):
        self.diretorio_atual = os.getcwd()
        self.icone = os.path.join(self.diretorio_atual, 'Imagens', 'icon_nelson.ico')

    
    def configurar_janela(self):
        # Adiciona o titulo
        self.janela.title('Sistema de automações Nelson Wendt')
        # Adiciona o icone superior
        self.janela.iconbitmap(self.icone)
        # Ajusta o tamanho da janela
        self.janela.geometry('418x280+300+280')
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

        tratar_arquivo = tk.Button(font=self.fonte, text='Tratar Arquivo Excel', command=self.tratar_estoque, width=19, height=2, bg='#fbff07', fg='#2d4390')
        tratar_arquivo.grid(row=2, column=1, padx=14, pady=10, sticky='nsew')

        arrumar_estoque = tk.Button(font=self.fonte, text='Arrumar Estoque Almox', command=self.arrumar_estoque, width=19, height=2, bg='#fbff07', fg='#2d4390')
        arrumar_estoque.grid(row=3, column=0, padx=14, pady=10, sticky='nsew')
    

    def criar_interface(self):
        self.janela = self.janela = tk.Tk()
        self.fonte = font.Font(family='Roboto', size=12)
        self.configurar_janela()
        self.criar_botoes()
        self.janela.mainloop()