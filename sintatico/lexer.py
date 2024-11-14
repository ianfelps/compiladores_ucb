import ply.lex as lex

# Lista de tokens
tokens = [
    'PROGRAM', 'ID', 'SEMI', 'DOT', 'VAR', 'COLON', 'INTEGER', 'REAL', 'BOOLEAN', 'BEGIN', 
    'END', 'ASSIGN', 'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'EQ', 'NE', 'LT', 'LE', 'GT', 'GE',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUM_INT', 'NUM_REAL', 'LPAREN', 'RPAREN', 'COMMA'
]

# Palavras reservadas
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'integer': 'INTEGER',
    'real': 'REAL',
    'boolean': 'BOOLEAN',
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO'
}

# Tokens simples
t_SEMI = r';'
t_DOT = r'\.'
t_COLON = r':'
t_ASSIGN = r':='
t_EQ = r'='
t_NE = r'<>'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

# Ignora espaços e tabs
t_ignore = ' \t'

# Ignorar e validar comentários no estilo Pascal entre { e }
def t_COMMENT(t):
    r'\{'
    start_pos = t.lexer.lexpos  # Posição inicial do comentário
    while True:
        if t.lexer.lexpos >= len(t.lexer.lexdata):  # Se chegou ao fim do input
            print(f"Erro: comentário não fechado iniciado na linha {t.lineno}")
            t.lexer.skip(1)  # Ignora para evitar um loop infinito
            break
        current_char = t.lexer.lexdata[t.lexer.lexpos]
        t.lexer.lexpos += 1  # Avança o lexer
        if current_char == '}':  # Encontrou o fechamento
            break
    pass  # Ignora o comentário completo

# Regras de tokens complexas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra reservada
    return t

def t_NUM_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a linha dos erros
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()
