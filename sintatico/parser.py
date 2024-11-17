import ply.yacc as yacc
from lexer import tokens

# Regra inicial
start = 'programa'

# Tabela de símbolos para armazenar variáveis declaradas
symbol_table = set()

# Definição do programa principal
def p_programa(p):
    "programa : PROGRAM ID SEMI bloco DOT"
    p[0] = ('programa', p[2], p[4])

# Bloco e declaração de variáveis
def p_bloco(p):
    "bloco : parte_declaracoes_variaveis comando_composto"
    p[0] = ('bloco', p[1], p[2])

def p_parte_declaracoes_variaveis(p):
    """parte_declaracoes_variaveis : VAR declaracao_variaveis_list SEMI
                                   | empty"""
    p[0] = p[2] if len(p) > 2 else None

def p_declaracao_variaveis_list(p):
    """declaracao_variaveis_list : declaracao_variaveis
                                 | declaracao_variaveis_list SEMI declaracao_variaveis"""
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_declaracao_variaveis(p):
    "declaracao_variaveis : lista_identificadores COLON tipo"
    # Adiciona cada identificador na tabela de símbolos
    for var in p[1]:
        if var in symbol_table:
            print(f"Erro: variável '{var}' já foi declarada.")
        else:
            symbol_table.add(var)
    p[0] = ('declaracao_variaveis', p[1], p[3])

def p_lista_identificadores(p):
    """lista_identificadores : ID
                             | lista_identificadores COMMA ID"""
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_tipo(p):
    """tipo : INTEGER
            | REAL
            | BOOLEAN"""
    p[0] = p[1]

# Comando composto
def p_comando_composto(p):
    "comando_composto : BEGIN comando_list END"
    p[0] = ('comando_composto', p[2])

def p_comando_list(p):
    """comando_list : comando
                    | comando_list SEMI comando"""
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

# Definição de comandos
def p_comando(p):
    """comando : atribuicao
               | comando_composto
               | comando_condicional
               | comando_repetitivo"""
    p[0] = p[1]

# Atribuição
def p_atribuicao(p):
    "atribuicao : ID ASSIGN expressao"
    # Verifica se a variável foi declarada antes de usá-la
    if p[1] not in symbol_table:
        print(f"Erro: variável '{p[1]}' não foi declarada.")
    p[0] = ('atribuicao', p[1], p[3])

# Comando condicional if ... else
def p_comando_condicional(p):
    """comando_condicional : IF expressao THEN comando
                           | IF expressao THEN comando ELSE comando"""
    p[0] = ('comando_condicional', p[2], p[4]) if len(p) == 5 else ('comando_condicional', p[2], p[4], p[6])

# Comando repetitivo while
def p_comando_repetitivo(p):
    "comando_repetitivo : WHILE expressao DO comando"
    p[0] = ('comando_repetitivo', p[2], p[4])

# Expressões e operações
def p_expressao(p):
    """expressao : expressao_simples
                 | expressao_simples relacao expressao_simples"""
    p[0] = p[1] if len(p) == 2 else ('expressao', p[1], p[2], p[3])

def p_relacao(p):
    """relacao : EQ
               | NE
               | LT
               | LE
               | GT
               | GE"""
    p[0] = p[1]

def p_expressao_simples(p):
    """expressao_simples : termo
                         | expressao_simples PLUS termo
                         | expressao_simples MINUS termo"""
    p[0] = p[1] if len(p) == 2 else ('expressao_simples', p[1], p[2], p[3])

def p_termo(p):
    """termo : fator
             | termo TIMES fator
             | termo DIVIDE fator"""
    p[0] = p[1] if len(p) == 2 else ('termo', p[1], p[2])

def p_fator(p):
    """fator : ID
             | NUM_INT
             | NUM_REAL
             | LPAREN expressao RPAREN"""
    if len(p) == 2 and isinstance(p[1], str):  # Caso seja uma variável ID
        # Verifica se a variável foi declarada antes de usá-la
        if p[1] not in symbol_table:
            print(f"Erro: variável '{p[1]}' não foi declarada.")
    p[0] = p[1] if len(p) == 2 else p[2]

# Regra para vazio (empty)
def p_empty(p):
    "empty :"
    p[0] = None

def p_error(p):
    if p:
        # Erro de ponto e vírgula ausente
        if p.type in {'ID', 'IF', 'WHILE', 'BEGIN', 'NUM_INT', 'NUM_REAL'}:
            print(f"Erro de sintaxe: falta de ponto e vírgula (';') no final da linha {p.lineno - 1}")

        # Erro para estruturas de controle incompletas
        elif p.type == 'THEN':
            print(f"Erro de sintaxe: 'THEN' sem condição 'IF' na linha {p.lineno}")
        elif p.type == 'DO':
            print(f"Erro de sintaxe: 'DO' sem condição 'WHILE' na linha {p.lineno}")
        elif p.type == 'END':
            print(f"Erro de sintaxe: 'END' sem correspondente 'BEGIN' na linha {p.lineno}")
        elif p.type == 'ELSE':
            print(f"Erro de sintaxe: 'ELSE' sem 'IF' na linha {p.lineno}")

        # Erro de fechamento de parênteses ou blocos
        elif p.type == 'RPAREN':
            print(f"Erro de sintaxe: parêntese de fechamento ')' sem correspondente '(' na linha {p.lineno}")
        elif p.type == 'LPAREN':
            print(f"Erro de sintaxe: parêntese de abertura '(' não fechado na linha {p.lineno}")

        # Qualquer outro erro
        else:
            print(f"Erro de sintaxe no token '{p.value}', linha {p.lineno}")
    else:
        # Caso o parser chegue ao final do arquivo e ainda espere por um token
        print("Erro de sintaxe: final do arquivo inesperado")

# Construção do parser
parser = yacc.yacc()

# Função de parsing
def parse(data):
    result = parser.parse(data)
    print("Parsing completed.")
    return result