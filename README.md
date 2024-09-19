# analisador_lexico
O analisador realiza a leitura de um arquivo com código fonte em MicroPascal e gera como saída uma tabela de símbolos e uma lista de tokens reconhecidos, identificando erros léxicos e de sintaxe.

Analisador Léxico para a linguagem MicroPascal, desenvolvido em Python utilizando a biblioteca PLY (Python Lex-Yacc).

## Como funciona

O analisador léxico funciona lendo o código fonte em MicroPascal e dividindo-o em tokens, que são as menores unidades de significado na linguagem, como palavras-chave, identificadores, operadores, números e símbolos. Cada token é comparado com um conjunto de regras pré-definidas, e então classificado em categorias, como operadores (+, -, =), palavras reservadas (program, begin, end), e identificadores (nomes de variáveis e funções). Além disso, o analisador identifica e reporta erros léxicos, como o uso de aspas duplas para strings ou a falta de símbolos de pontuação, como ";" e "." A tabela de símbolos gerada contém informações sobre os tokens encontrados, facilitando o processo de análise sintática posterior.

O analisador léxico identifica e trata diversos erros léxicos que podem ocorrer no código MicroPascal, como:
- **Caracteres Desconhecidos:** Se o analisador encontra um caractere que não faz parte da linguagem MicroPascal ou dos tokens definidos, ele é classificado como um erro. Isso garante que o código contenha apenas elementos válidos.
- **Fechamento incorreto de strings:** O analisador verifica se todas as strings delimitadas por aspas simples (') são corretamente fechadas. Caso uma string não tenha o fechamento adequado, o erro é reportado, garantindo que as cadeias de caracteres estejam bem formadas.


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

4. O status da geração do arquivo de saída será exibido no console, e o arquivo **_saida.lex_** conterá os tokens reconhecidos e a tabela de símbolos.

## compiladores_ucb
Repositório para atividades e projetos da disciplina de Linguagens Formais, Autômatos e Compiladores na UCB (4º semestre).