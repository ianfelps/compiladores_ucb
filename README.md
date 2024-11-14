Analisadores para a linguagem MicroPascal, desenvolvidos em Python utilizando a biblioteca PLY (Python Lex-Yacc).

# Analisador Léxico
O analisador léxico (ou lexer) é responsável por dividir o código fonte em unidades menores chamadas tokens. Ele identifica palavras-chave, operadores, identificadores, números e outros elementos da linguagem, transformando o texto em uma sequência de tokens que o analisador sintático pode processar. Além disso, o analisador léxico pode identificar erros léxicos, como caracteres inválidos.

# Analisador Sintático
Um analisador sintático (ou parser) verifica se a sequência de tokens gerada pelo analisador léxico está correta de acordo com as regras gramaticais da linguagem. Ele organiza os tokens em uma árvore sintática e detecta erros de estrutura no código.


## Tabela de Símbolos

| Token        | Descrição                                      | Exemplo       |
|--------------|------------------------------------------------|---------------|
| **PROGRAM**  | Palavra reservada para declaração de programa  | `program`     |
| **VAR**      | Palavra reservada para declaração de variáveis | `var`         |
| **INTEGER**  | Tipo de dado inteiro                           | `integer`     |
| **REAL**     | Tipo de dado real (ponto flutuante)            | `real`        |
| **BEGIN**    | Início de um bloco                             | `begin`       |
| **END**      | Fim de um bloco                                | `end`         |
| **IF**       | Palavra reservada para condição                | `if`          |
| **THEN**     | Palavra reservada para consequência            | `then`        |
| **ELSE**     | Palavra reservada para alternativa             | `else`        |
| **WHILE**    | Palavra reservada para laço                    | `while`       |
| **DO**       | Palavra reservada para execução de laço        | `do`          |
| **ID**       | Identificador (variáveis e funções)            | `x`, `count`  |
| **NUM_INT**  | Número inteiro                                 | `123`         |
| **NUM_FLT**  | Número real (ponto flutuante)                  | `123.45`      |
| **STRING**   | Cadeia de caracteres delimitada por aspas simples | `'hello'`  |
| **OP_EQ**    | Operador de igualdade                          | `=`           |
| **OP_GE**    | Operador maior ou igual                        | `>=`          |
| **OP_MUL**   | Operador de multiplicação                      | `*`           |
| **OP_NE**    | Operador de diferença                          | `<>`          |
| **OP_LE**    | Operador menor ou igual                        | `<=`          |
| **OP_DIV**   | Operador de divisão                            | `/`           |
| **OP_GT**    | Operador maior que                             | `>`           |
| **OP_AD**    | Operador de adição                             | `+`           |
| **OP_ASS**   | Operador de atribuição                         | `:=`          |
| **OP_LT**    | Operador menor que                             | `<`           |
| **OP_MIN**   | Operador de subtração                          | `-`           |
| **SMB_OBC**  | Símbolo de abertura de bloco                   | `{`           |
| **SMB_COM**  | Símbolo de vírgula                             | `,`           |
| **SMB_CBC**  | Símbolo de fechamento de bloco                 | `}`           |
| **SMB_SEM**  | Símbolo de ponto-e-vírgula                     | `;`           |
| **SMB_OPA**  | Símbolo de abertura de parênteses              | `(`           |
| **SMB_CPA**  | Símbolo de fechamento de parênteses            | `)`           |
| **SMB_DOT**  | Símbolo de ponto final                         | `.`           |
| **SMB_COL**  | Símbolo de dois pontos                         | `:`           |


## Como usar
1. Instale a biblioteca PLY:
```
pip install ply
```
2. Insira o código MicroPascal que deseja analisar no arquivo: **_codigo.txt_**

3. Execute o arquivo main:
```
python main.py
```

## compiladores_ucb
Repositório para atividades e projetos da disciplina de Linguagens Formais, Autômatos e Compiladores na UCB (4º semestre).