import os
import shutil

pasta_raiz = "C:/Users/User/Desktop/Scraping and Writing/autoPython/Escraped for Write/600x600 images"

pasta_destino = "C:/Users/User/Desktop/Scraping and Writing/autoPython/Escraped for Write/ALL images"

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

for pasta, subpastas, arquivos in os.walk(pasta_raiz):
    for arquivo in arquivos:
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            caminho_origem = os.path.join(pasta, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_origem, caminho_destino)
            print(f"Imagem '{arquivo}' movida para '{pasta_destino}'.")

print("Todas as imagens foram movidas com sucesso.")
