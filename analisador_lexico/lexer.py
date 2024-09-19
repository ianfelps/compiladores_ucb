import ply.lex as lex
import sys
from tokens import TabelaSimbolos

class AnalisadorLexico:
    # inicializa o analisador lexico
    def __init__(self):
        self.reserved = {
            'program': 'PROGRAM', # palavras reservadas
            'var': 'VAR',
            'integer': 'INTEGER',
            'real': 'REAL',
            'begin': 'BEGIN',
            'end': 'END',
            'if': 'IF',
            'then': 'THEN',
            'else': 'ELSE',
            'while': 'WHILE',
            'do': 'DO'
        }
        
        self.tokens = [
            'ID', 'NUM_INT', 'NUM_FLT', 'STRING',   # identificadores, numeros e strings
            'OP_EQ', 'OP_GE', 'OP_MUL',   # operadores
            'OP_NE', 'OP_LE', 'OP_DIV',
            'OP_GT', 'OP_AD', 'OP_ASS',
            'OP_LT', 'OP_MIN',
            'SMB_OBC', 'SMB_COM', 'SMB_CBC',  # simbolos
            'SMB_SEM', 'SMB_OPA', 'SMB_CPA', 'SMB_DOT', 'SMB_COL'
        ] + list(self.reserved.values())

        # inicializar a tabela de símbolos
        self.tabela_simbolos = TabelaSimbolos(self.reserved)
        
        self.lexer = lex.lex(module=self)

    # regras de tokens com expressões regulares
    t_OP_EQ  = r'='
    t_OP_GE  = r'>='
    t_OP_MUL = r'\*'
    t_OP_NE  = r'<>'   
    t_OP_LE  = r'<='
    t_OP_DIV = r'/'
    t_OP_GT  = r'>'
    t_OP_AD  = r'\+'
    t_OP_ASS = r':='
    t_OP_LT  = r'<'
    t_OP_MIN = r'-'
    t_SMB_OBC = r'\{'
    t_SMB_COM = r','
    t_SMB_CBC = r'\}'
    t_SMB_SEM = r';'
    t_SMB_OPA = r'\('
    t_SMB_CPA = r'\)'
    t_SMB_DOT = r'\.'
    t_SMB_COL = r':'

    # regras para numeros inteiros e reais
    def t_NUM_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_NUM_FLT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    # regras para identificadores, palavras reservadas e strings
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')    # verifica se eh uma palavra reservada
        self.tabela_simbolos.adicionar_na_tabela(t.value, t.type)
        return t

    def t_STRING(self, t):
        r"'([^'\n]|(\\'))*'"  # regra para strings entre aspas simples
        t.value = t.value[1:-1]  # remove aspas ao redor da string
        return t

    # ignorar espaços em branco, tabulações e quebras de linha
    t_ignore = ' \t'

    # ignorar comentários de bloco { ... }
    def t_comment_block(self, t):
        r'\{[^}]*\}'
        pass

    # ignorar comentários de linha //...
    def t_comment_line(self, t):
        r'//.*'
        pass

    # registra a linha e coluna
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # tratar caracteres ilegais e strings nao fechadas
    def t_error(self, t):
        if t.value[0] == "'":
            linha_erro = f"Erro: string nao fechada na linha {t.lineno}, coluna {t.lexpos}\n"
        else:
            linha_erro = f"Caractere ilegal '{t.value[0]}' na linha {t.lineno}, coluna {t.lexpos}\n"
        
        with open('saida.lex', 'a') as arquivo_lex:
            arquivo_lex.write(linha_erro)
        
        print(linha_erro.strip())
        sys.exit(1)

    # salva e imprime os tokens no arquivo de saida
    def salvar_e_imprimir_token(self, t):
        linha = f"<{t.type}, {t.value}> na linha {t.lineno}, coluna {t.lexpos}\n"
        with open('saida.lex', 'a') as arquivo_lex:
            arquivo_lex.write(linha)

    # executa o analisador lexico com o codigo fornecido
    def executar_analisador(self, codigo):
        self.lexer.input(codigo)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            self.salvar_e_imprimir_token(tok)

    # salva e imprime a tabela de simbolos no arquivo de saida
    def salvar_e_imprimir_tabela_simbolos(self):
        with open('saida.lex', 'a') as arquivo_lex:
            arquivo_lex.write("\nTabela de Simbolos:\n")
            for lexema, tipo in self.tabela_simbolos.itens():
                linha = f"{lexema}: {tipo}\n"
                arquivo_lex.write(linha)