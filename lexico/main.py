from lexer import AnalisadorLexico

def main():
    # nome do arquvio contendo o codigo em Micro Pascal
    nome_arquivo_entrada = 'codigo.txt'
    
    # limpar o conteúdo do arquivo de saída anterior para novo resultado, se existir
    open('saida.lex', 'w').close()

    # ler o arquivo com o codigo
    with open(nome_arquivo_entrada, 'r') as arquivo:
        codigo = arquivo.read()

    # criar uma instância do AnalisadorLexico
    lexer = AnalisadorLexico()

    # tentar executar a analise lexica
    try:
        lexer.executar_analisador(codigo)
    finally:
        # salvar e imprimir a tabela de simbolos e exibir uma mensagem de sucesso
        lexer.salvar_e_imprimir_tabela_simbolos()
        print("Arquivo 'saida.lex' gerado com sucesso.")

if __name__ == "__main__":
    # executar a funcao principal
    main()