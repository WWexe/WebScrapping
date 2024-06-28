import requests
from bs4 import BeautifulSoup
import os
import urllib

for i in range(3, 46+1):
    url = f"https://www.dhzfitness.com/products/page/{i}/"

    # Fazendo a solicitação HTTP
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrando todos os <li> com a classe "product_list_item"
        list_items = soup.find_all('li', class_='product_list_item')
        
        # Diretório para salvar as imagens
        save_directory = f"imagens_raspadas_definitive{i}"
        
        # Verifica se o diretório já existe, caso contrário, cria-o
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Iterando sobre todos os <li> encontrados
        for item in list_items:
            # Encontrando a <span> com a classe "item_img" dentro do <li>
            span_item_img = item.find('span', class_='item_img')
            
            # Verificando se a <span> foi encontrada e se contém uma imagem
            if span_item_img:
                # Encontrando a <img> dentro da <span>
                img = span_item_img.find('img')
                
                # Verificando se a <img> foi encontrada e se contém a URL da imagem
                if img and 'src' in img.attrs:
                    # Obtendo a URL da imagem
                    img_url = img['src']
                    
                    # Obtendo o nome do arquivo da imagem a partir da URL
                    filename = os.path.basename(img_url)
                    filename_formatado = filename.replace('-', " ")
                    
                    urllib.request.urlretrieve(img_url, os.path.join(save_directory, filename_formatado))
                    print(f"Imagem '{filename_formatado}' baixada com sucesso e salva em '{save_directory}'!")
                else:
                    print("URL da imagem não encontrada.")
            else:
                print("Span com classe 'item_img' não encontrada.")
    else:
        print("Falha ao fazer a solicitação HTTP.")
