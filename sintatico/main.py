from lexer import lexer
from parser import parser

# Ler o código de `codigo.txt`
with open("codigo.txt", "r") as file:
    code = file.read()

# Executar o analisador léxico
lexer.input(code)
print("Tokens:")
for token in lexer:
    print(f"Token: '{token.type}', Valor: '{token.value}', Linha: '{token.lineno}'")

# Executar o analisador sintático
# print("\nAnalisando...")
# result = parser.parse(code)
# print("Analise Sintatica completa!")