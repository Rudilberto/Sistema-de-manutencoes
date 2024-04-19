import pandas as pd
import os
from tkinter.filedialog import askopenfilename


class Estoque():
    abspath=os.path.abspath(__file__)
    dname=os.path.dirname(abspath)
    os.chdir(dname)
    diretorio_atual = os.getcwd()
    
    caminho_gabarito = os.path.join(diretorio_atual, 'gabarito.xlsx')
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, 'Arquivo_Final.xlsx')

    
    def tratar_estoque(self):
        gabarito = pd.read_excel(self.caminho_gabarito)      
        arquivo = askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])

        estoque_sistema = pd.read_excel(arquivo)

        estoque_sistema = estoque_sistema.loc[:, ['Vlr.Estoque', 'Unnamed: 2', 'Qtde Estq']]

        estoque_sistema = estoque_sistema.rename(columns={'Unnamed: 2': 'produto', 'Vlr.Estoque': 'codigo', 'Qtde Estq': 'quantidade em estoque'})

        estoque_sistema = estoque_sistema.dropna(axis='index')

        estoque_sistema['codigo'] = estoque_sistema['codigo'].astype(str)
        gabarito['codigo'] = gabarito['codigo'].astype(str)

        estoque_final = gabarito.merge(estoque_sistema[['codigo', 'quantidade em estoque']], on='codigo')

        estoque_final['estoque'] = estoque_final['quantidade em estoque']
        estoque_final = estoque_final.drop('quantidade em estoque', axis=1)

        estoque_final.to_excel(self.file_path, index=False)


    def tratar_arquivo_final(self):
        arquivo = askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
        estoque_final = pd.read_excel(arquivo)

        estoque_final = estoque_final[estoque_final['a retirar'] != 0]

        dicionario = estoque_final.to_dict()

        codigos = [str(codigo) for codigo in dicionario['codigo'].values()]
        quantidade = [round(float(codigo), 2) for codigo in dicionario['a retirar'].values()]
        observacao = [str(codigo) for codigo in dicionario['obs'].values()]
        conta_contabil = [str(codigo) for codigo in dicionario['conta contabil'].values()]
        centro_custo = [str(codigo) for codigo in dicionario['centro de custo'].values()]

        return codigos, quantidade, observacao, conta_contabil, centro_custo