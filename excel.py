import pandas as pd
import os

# Função para converter arquivo de texto para Excel
def converter_txt_para_excel(arquivo_entrada, pasta_saida):
    # Carrega o arquivo de texto para um DataFrame
    df = pd.read_csv(arquivo_entrada, delimiter='\t')  
    
    nome_arquivo_saida = os.path.join(pasta_saida, os.path.splitext(os.path.basename(arquivo_entrada))[0] + '.xlsx')

    df.to_excel(nome_arquivo_saida, index=False)

    print(f'Arquivo convertido para Excel e salvo como {nome_arquivo_saida}')

arquivo_entrada = 'C:/Users/ti3/OneDrive/Área de Trabalho/descriçoes/descriçoes unity/arquivo_saida.txt'  

pasta_saida = 'C:/Users/ti3/OneDrive/Área de Trabalho/descriçoes/descriçoes unity'  
converter_txt_para_excel(arquivo_entrada, pasta_saida)
