import pyautogui as pt

class Manutencao():

    def gerar_quantidade_iteracoes(self):
        while True:
            quantidade_manutencoes = pt.prompt(text='Digite quantas manutenções/relatórios serão feitos')

            if quantidade_manutencoes is None:
                pt.alert(text='Campo vazio. Digite um valor.', title='Erro de digitação')
            elif not quantidade_manutencoes:
                pt.alert(text='Campo vazio. Digite um valor.', title='Erro de digitação')
            else:
                try:
                    quantidade_manutencoes = int(quantidade_manutencoes)
                    if quantidade_manutencoes <= 0:
                        pt.alert(text='Valor inválido. Digite um número maior que zero.', title='Erro de digitação')
                    else:
                        break
                    
                except ValueError:
                    pt.alert(text='Valor inválido. Digite um número válido.', title='Erro de digitação')
        
        return quantidade_manutencoes


    def revisao_dados_manutencao(self, lista_equipamento, lista_descricoes_manutencao, ProdutoQuantia, a):
        revisao_dados_manutencao = pt.confirm(text=f'''Revise suas informações\n
equipamento: {lista_equipamento[a]}
descrição da manutenção: {lista_descricoes_manutencao[a]}
produto e quantidade: {ProdutoQuantia}''')
        return revisao_dados_manutencao


    def informacoes_manutencao(self, quantidade_manutencoes):
        lista_equipamento = []
        lista_descricoes_manutencao = []
        lista_quantos_produtos = []
        produto_quantidade = []

        for a in range(quantidade_manutencoes):
            while True:
                equipamento = self.verificar_texto('Digite o nome do equipamento: ')
                lista_equipamento.append(equipamento)

                descricoes_manutencao = self.verificar_texto('Digite a descricao da manutenção: ').lower()
                lista_descricoes_manutencao.append(descricoes_manutencao)

                quantos_produtos = self.verificar_numero('Digite quantos produtos há na manutenção: ')
                lista_quantos_produtos.append(quantos_produtos)

                ProdutoQuantia = []

                n = 0
                
                for _ in range(lista_quantos_produtos[a]):
                    n += 1
                    nome_produto = self.verificar_texto(f'Digite o nome do {n}° produto: ')
                    quantidade = self.verificar_numero(f'Digite a quantidade usada do {n}° produto: ')
                    quantidade = str(quantidade)

                    ProdutoQuantia.append((nome_produto, quantidade))
                
                revisao_dados_manutencao = self.revisao_dados_manutencao(lista_equipamento, lista_descricoes_manutencao, ProdutoQuantia, a)
                
                if revisao_dados_manutencao == 'Cancel':
                    pt.alert(text='Digite os dados novamente!')
                    del lista_equipamento[a]
                    del lista_descricoes_manutencao[a]
                    del lista_quantos_produtos[a]

                else:
                    pt.alert(text='Manutencao programada!')
                    produto_quantidade.append(ProdutoQuantia)
                    break

        return lista_equipamento, lista_descricoes_manutencao, lista_quantos_produtos, produto_quantidade


    def gerar_dicionario_manutencoes(self):

        quantidade_manutencoes = self.gerar_quantidade_iteracoes()
        
        lista_equipamento, lista_descricoes_manutencao, lista_quantos_produtos, produto_quantidade = self.informacoes_manutencao(quantidade_manutencoes)

        dicionario_manutencoes = {
        'equipamento': lista_equipamento, 
        'descricao_manutencao': lista_descricoes_manutencao,
        'quantos_produtos': lista_quantos_produtos,
        'produto_quantidade': produto_quantidade, 
        }

        return dicionario_manutencoes, quantidade_manutencoes


    def revisao_dados_manutencao_comprar(self, lista_equipamento, lista_descricoes_manutencao, lista_descricoes_compra, ProdutoQuantia, a):
        revisao_dados = pt.confirm(text=f'''Revise suas informações\n
equipamento: {lista_equipamento[a]}
descrição da manutenção: {lista_descricoes_manutencao[a]}
descrição da compra: {lista_descricoes_compra[a]}
produto e quantidade: {ProdutoQuantia}''')
        return revisao_dados 
    
    
    def informacoes_manutencao_comprar(self, quantidade_manutencoes):
        produto_quantidade = []
        produto_quantidade_descricao = []   
        lista_equipamento = []
        lista_descricoes_manutencao = []
        lista_quantos_produtos = []
        lista_descricoes_compra = []

        for a in range(quantidade_manutencoes):
            while True:
                equipamento = self.verificar_texto('Digite o nome do equipamento: ')
                lista_equipamento.append(equipamento)

                descricoes_manutencao = self.verificar_texto('Digite a descricao da manutenção: ')
                lista_descricoes_manutencao.append(descricoes_manutencao)
                
                quantos_produtos = self.verificar_numero('Digite quantos produtos há na manutenção: ')
                lista_quantos_produtos.append(quantos_produtos)

                descricoes_compra = self.verificar_texto('Digite a descricao da compra: ').lower()
                lista_descricoes_compra.append(descricoes_compra)
                
                ProdutoQuantia = []
                ProdutoQuantiaDescricao = []

                n = 0
                
                for _ in range(lista_quantos_produtos[a]):
                    n += 1
                    nome_produto = self.verificar_texto(f'Digite o nome do {n}° produto: ')
                    quantidade = self.verificar_numero(f'Digite a quantidade usada do {n}° produto: ')
                    quantidade = str(quantidade)
                    
                    cc = ''
                    if 'enge' in lista_equipamento[a]:
                        cc = '324'
                    elif 'empacota' in lista_equipamento[a]:
                        cc = '328'
                    elif 'secad' in lista_equipamento[a]:
                        cc = '323'
                    elif 'parbo' in lista_equipamento[a]:
                        cc = '322'
                    elif 'ete' in lista_equipamento[a]:
                        cc = '331'
                    elif 'eta' in lista_equipamento[a]:
                        cc = '332'
                    elif 'tomb' in lista_equipamento[a]:
                        cc = '330'
                    elif  'grane' in lista_equipamento[a] :
                        cc = '330' 
                    elif 'automa' in lista_equipamento[a]:
                        cc = '340'
                    elif 'pre-limp' in lista_equipamento[a]:
                        cc = '321'
                    elif 'eletro' in lista_equipamento[a]:
                        cc = '325'
                    elif 'calde' in lista_equipamento[a]:
                        cc = '326'
                    elif 'safra' in lista_equipamento[a]:
                        cc = '334'
                    elif 'compres' in lista_equipamento[a]:
                        cc = '335'
                    elif 'gerado' in lista_equipamento[a]:
                        cc = '336'
                    elif 'substacao' in lista_equipamento[a]:
                        cc = '337'
                    elif 'retiro' in lista_equipamento[a]:
                        cc = '338'
                    elif 'expedi' in lista_equipamento[a]:
                        cc = '339'
                    else:
                        cc = '333'

                    ProdutoQuantiaDescricao.append((nome_produto, quantidade, cc))
                    ProdutoQuantia.append((nome_produto, quantidade))

                revisao_dados_manutencao_comprar = self.revisao_dados_manutencao_comprar(lista_equipamento, lista_descricoes_manutencao, lista_descricoes_compra, ProdutoQuantia, a)
            
                if revisao_dados_manutencao_comprar == 'Cancel':
                    pt.alert(text='Digite os dados novamente!')
                    del lista_equipamento[a]
                    del lista_descricoes_manutencao[a]
                    del lista_quantos_produtos[a]
                    del lista_descricoes_compra[a]


                else:
                    pt.alert(text='Manutencao programada!')
                    produto_quantidade.append(ProdutoQuantia)
                    produto_quantidade_descricao.append(ProdutoQuantiaDescricao)
                    break

        return lista_equipamento, lista_descricoes_manutencao, lista_quantos_produtos, lista_descricoes_compra, produto_quantidade, produto_quantidade_descricao
    

    def gerar_dicionario_manutencoes_compras(self):

        quantidade_manutencoes = self.gerar_quantidade_iteracoes()

        lista_equipamento, lista_descricoes_manutencao, lista_quantos_produtos, lista_descricoes_compra, produto_quantidade, produto_quantidade_descricao = self.informacoes_manutencao_comprar(quantidade_manutencoes)

        dicionario_manutencoes = {
'equipamento': lista_equipamento, 
'descricao_manutencao': lista_descricoes_manutencao,
'quantos_produtos': lista_quantos_produtos,
'produto_quantidade': produto_quantidade, 
'produto_quantidade_descricao': produto_quantidade_descricao,
'descricao_compra': lista_descricoes_compra
}

        return dicionario_manutencoes, quantidade_manutencoes
    

    def gerar_lista_equipamento(self):
        quantidade_relatorios = self.gerar_quantidade_iteracoes()

        lista_equipamento = []
        for i in range(quantidade_relatorios):
            equipamento = self.verificar_texto(f'Digite o nome do {i + 1}° equipamento: ')
            lista_equipamento.append(equipamento)
        
        return lista_equipamento, quantidade_relatorios