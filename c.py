import requests
from bs4 import BeautifulSoup
import os
import urllib

def download_image(url, directory):
    filename = os.path.join(directory, os.path.basename(url))
    urllib.request.urlretrieve(url, filename)

url = 'https://www.dhzfitness.com/products/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='product-item')

image_directory = 'product_images'

if not os.path.exists(image_directory):
    os.makedirs(image_directory)

for product in products:
    name = product.find('h3', class_='product-name').text.strip()
    
    image_url = product.find('img')['src']
    
    download_image(image_url, image_directory)
    
    print('Nome:', name)
    print('URL da imagem:', image_url)
    print()

print('Download de imagens concluído!')
