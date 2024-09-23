class TabelaSimbolos:
    # inicializa a tabela de simbolos com as palavras reservadas
    def __init__(self, reserved):
        self.tabela = {palavra: (f'PAL_RES_{palavra.upper()}', None) for palavra in reserved}
        self.contador_id = 1  # contador de IDs
    
    # adiciona um lexema à tabela de símbolos, se ainda não estiver presente
    def adicionar_na_tabela(self, lexema, tipo):
        if lexema not in self.tabela:
            # associar um numero unico para IDs
            if tipo == 'ID':
                self.tabela[lexema] = (tipo, self.contador_id)
                self.contador_id += 1
            else:
                self.tabela[lexema] = (tipo, None)  # outros tipos de token, nao associar

    # retorna os itens da tabela de simbolos
    def itens(self):
        return self.tabela.items()

    # retorna o ID associado a um identificador
    def obter_id(self, lexema):
        if lexema in self.tabela and self.tabela[lexema][1] is not None:
            return self.tabela[lexema][1]
        return None
