import requests
from bs4 import BeautifulSoup
import os

base_url = 'https://www.dhzfitness.com/products/page/'

pasta_destino = 'C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/Titulos'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

caminho_arquivo = os.path.join(pasta_destino, 'titulos.txt')

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:

    for i in range(3, 46+1):
        url = f'{base_url}{i}/'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        elementos = soup.find_all('h3', class_='item_title')

        for elemento in elementos:
            texto = elemento.find('a').text.strip()
            arquivo.write(texto + '\n')

    print("Raspagem concluída e textos salvos no arquivo 'titulos.txt'.")

    
    
    
    
    
    
    
    
    
    
