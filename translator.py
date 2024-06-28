from googletrans import Translator
import os

def traduzir_e_salvar_arquivo(arquivo_entrada, idioma_destino, pasta_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        texto = file.read()

    translator = Translator()

    traducao = translator.translate(texto, dest=idioma_destino)

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    nome_arquivo_saida = os.path.join(pasta_saida, os.path.splitext(os.path.basename(arquivo_entrada))[0] + f'_{idioma_destino}.txt')

    with open(nome_arquivo_saida, 'w', encoding='utf-8') as file:
        file.write(traducao.text)

    print(f'Arquivo traduzido para {idioma_destino} e salvo como {nome_arquivo_saida}')

arquivo_entrada = 'C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/Titulos/titulos'

pasta_saida_pt = 'traducoes_pt_br'

pasta_saida_es = 'traducoes_es'

traduzir_e_salvar_arquivo(arquivo_entrada, 'pt', pasta_saida_pt)

traduzir_e_salvar_arquivo(arquivo_entrada, 'es', pasta_saida_es)
