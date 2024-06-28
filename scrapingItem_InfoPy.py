import requests
from bs4 import BeautifulSoup

with open('descricoes_produtos.txt', 'a', encoding='utf-8') as file:
    for i in range(3, 46+1):
        url = f'https://www.dhzfitness.com/products/page/{i}/'
    
        response = requests.get(url)
    
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            divs_item_info = soup.find_all('div', class_='item_info')
            
            descricoes = []
            
            for div_item_info in divs_item_info:
                spans = div_item_info.find_all('span')
                
                for span in spans:
                    
                    descricoes.append(span.get_text(strip=True))
            
            for descricao in descricoes:
                file.write(descricao + '\n\n')  
            
            print(f"Descrições dos produtos da página {i} foram salvas com sucesso!")
        else:
            print("Falha ao fazer a solicitação HTTP.")
