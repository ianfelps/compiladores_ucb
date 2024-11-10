import ply.lex as lex
import ply.yacc as yacc

# Definições do analisador léxico (tokens e literais)
tokens = (
    'ID', 'NUM_INT', 'NUM_FLT', 'OP_EQ', 'OP_GE', 'OP_MUL', 'OP_NE', 'OP_LE',
    'OP_DIV', 'OP_GT', 'OP_AD', 'OP_ASS', 'OP_LT', 'OP_MIN', 'SMB_OBC', 
    'SMB_COM', 'SMB_CBC', 'SMB_SEM', 'SMB_OPA', 'SMB_CPA', 'COLON', 'DOT'
)

# Palavras-chave
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'integer': 'INTEGER',
    'real': 'REAL',
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
}

tokens = list(tokens) + list(reserved.values())

# Regras de tokens e palavras-chave para o analisador léxico
t_OP_EQ = r'='
t_OP_GE = r'>='
t_OP_MUL = r'\*'
t_OP_NE = r'<>'
t_OP_LE = r'<='
t_OP_DIV = r'/'
t_OP_GT = r'>'
t_OP_AD = r'\+'
t_OP_ASS = r':='
t_OP_LT = r'<'
t_OP_MIN = r'-'
t_SMB_OBC = r'\{'
t_SMB_COM = r','
t_SMB_CBC = r'\}'
t_SMB_SEM = r';'
t_SMB_OPA = r'\('
t_SMB_CPA = r'\)'
t_COLON = r':'
t_DOT = r'\.'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUM_FLT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere desconhecido '{t.value[0]}'")
    t.lexer.skip(1)

# Constroi o lexer
lexer = lex.lex()

# Regras da gramática para o analisador sintático
def p_program(p):
    '''program : PROGRAM ID SMB_SEM var_declaration block DOT'''
    print("Programa reconhecido!")

def p_block(p):
    '''block : BEGIN statement_list END'''
    pass

def p_var_declaration(p):
    '''var_declaration : VAR var_list
                       | empty'''
    pass

def p_var_list(p):
    '''var_list : id_list COLON type SMB_SEM var_list
                | id_list COLON type SMB_SEM
                | empty'''
    pass

def p_id_list(p):
    '''id_list : ID
               | ID SMB_COM id_list'''
    pass

def p_type(p):
    '''type : INTEGER
            | REAL'''
    pass

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | empty'''
    pass

def p_statement(p):
    '''statement : assignment SMB_SEM
                 | if_statement
                 | while_statement
                 | block SMB_SEM
                 | empty'''
    pass

def p_assignment(p):
    '''assignment : ID OP_ASS expression'''
    pass

def p_if_statement(p):
    '''if_statement : IF expression THEN statement else_clause'''
    pass

def p_else_clause(p):
    '''else_clause : ELSE statement
                   | empty'''
    pass

def p_while_statement(p):
    '''while_statement : WHILE expression DO statement'''
    pass

def p_expression(p):
    '''expression : expression OP_AD term
                  | expression OP_MIN term
                  | term'''
    pass

# Adiciona comparação entre expressões
def p_expression_comparison(p):
    '''expression : expression OP_EQ term
                  | expression OP_GE term
                  | expression OP_GT term
                  | expression OP_LE term
                  | expression OP_LT term
                  | expression OP_NE term'''
    pass

def p_term(p):
    '''term : term OP_MUL factor
            | term OP_DIV factor
            | factor'''
    pass

def p_factor(p):
    '''factor : NUM_INT
              | NUM_FLT
              | ID
              | SMB_OPA expression SMB_CPA'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Função de erro
def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' na linha {p.lineno}")
        parser.errok()
    else:
        print("Erro de sintaxe no final da entrada")

# Constrói o parser
parser = yacc.yacc()

# nome do arquvio contendo o codigo em Micro Pascal
nome_arquivo_entrada = 'codigo.txt'

# ler o arquivo com o codigo
with open(nome_arquivo_entrada, 'r') as arquivo:
    codigo = arquivo.read()

# Executa o parser
parser.parse(codigo)