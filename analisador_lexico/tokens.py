class TabelaSimbolos:
    # inicializa a tabela de simbolos com as palavras reservadas
    def __init__(self, reserved):
        self.tabela = {palavra: f'PAL_RES_{palavra.upper()}' for palavra in reserved}
    
    # adiciona um lexema a tabela de simbolos, se ainda não estiver presente
    def adicionar_na_tabela(self, lexema, tipo):
        if lexema not in self.tabela:
            self.tabela[lexema] = tipo
    
    # retorna os itens da tabela de simbolos
    def itens(self):
        return self.tabela.items()