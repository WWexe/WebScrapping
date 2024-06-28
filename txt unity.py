import os

def juntar_arquivos_texto(pasta_entrada, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as outfile:
        for nome_arquivo in os.listdir(pasta_entrada):
            if nome_arquivo.endswith('.txt'):  
                with open(os.path.join(pasta_entrada, nome_arquivo), 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read() + '\n')

    print(f'Arquivos de texto juntados em {arquivo_saida}')

pasta_entrada = 'C:/Users/ti3/OneDrive/Área de Trabalho/descriçoes/descriçoes' 

arquivo_saida = 'C:/Users/ti3/OneDrive/Área de Trabalho/descriçoes/descriçoes unity/arquivo_saida.txt'  

juntar_arquivos_texto(pasta_entrada, arquivo_saida)
