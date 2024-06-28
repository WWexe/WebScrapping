import requests
from bs4 import BeautifulSoup
import os
import urllib

# Função para baixar uma imagem de uma URL para um diretório específico
def download_image(url, directory):
    filename = os.path.join(directory, os.path.basename(url))
    urllib.request.urlretrieve(url, filename)

# URL da página a ser analisada
url = 'https://www.dhzfitness.com/products/'

# Fazendo a solicitação HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando todos os elementos que representam produtos
products = soup.find_all('div', class_='product-item')

# Diretório para salvar as imagens dos produtos
image_directory = 'product_images'

# Verifica se o diretório já existe, caso contrário, cria-o
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# Loop através de todos os produtos encontrados
for product in products:
    # Obtendo o nome do produto
    name = product.find('h3', class_='product-name').text.strip()
    
    # Obtendo a URL da imagem do produto
    image_url = product.find('img')['src']
    
    # Baixando a imagem do produto
    download_image(image_url, image_directory)
    
    # Exibindo as informações do produto
    print('Nome:', name)
    print('URL da imagem:', image_url)
    print()

print('Download de imagens concluído!')
