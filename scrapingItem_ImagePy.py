import requests
from bs4 import BeautifulSoup
import os
import urllib

for i in range(3, 46+1):
    url = f"https://www.dhzfitness.com/products/page/{i}/"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        list_items = soup.find_all('li', class_='product_list_item')
        
        save_directory = f"imagens_raspadas_definitive{i}"
        
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        for item in list_items:
            span_item_img = item.find('span', class_='item_img')
            
            if span_item_img:
                img = span_item_img.find('img')
                
                if img and 'src' in img.attrs:
                    img_url = img['src']
                    
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
