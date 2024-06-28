import pyautogui
import pyinput
import io
import tempfile
import time
from PIL import Image
import os

pyautogui.alert("O Script COMEÇOU! NÃO USE nada do PC enquanto o Script estiver rodando")
pyautogui.PAUSE = 0.4
pyautogui.click(929, 1045)
contador = 0
while contador <= 6:
    pyautogui.hotkey('ctrl', '-')
    contador += 0.6

for _ in range(44):
    pyautogui.click(1027, 967)
    time.sleep(0.15)
    
    pyautogui.rightClick(870, 192)
    pyautogui.click(925, 239)
    time.sleep (2)

    for _ in range(6):
        pyautogui.press('tab')
        time.sleep(0.2)

    pyautogui.press('enter')
    pyautogui.write('C:/Users/ti3/OneDrive/imagens.webp')
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.press('enter')

    pyautogui.rightClick(870, 254)
    pyautogui.click(913, 298)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(872, 322)
    pyautogui.click(917, 365)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(866, 379)
    pyautogui.click(920, 425)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(866, 449)
    pyautogui.click(926, 496)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(872, 581)
    pyautogui.click(932, 626)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(874, 646)
    pyautogui.click(937, 694)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(868, 714)
    pyautogui.click(940, 464)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(866, 778)
    pyautogui.click(986, 520)
    time.sleep (1)
    pyautogui.press('enter')

    pyautogui.rightClick(870, 846)
    pyautogui.click(942, 593)
    time.sleep (2)
    pyautogui.press('enter')

    pyautogui.rightClick(865, 911)
    pyautogui.click(957, 654)
    time.sleep (2)
    pyautogui.press('enter')

pyautogui.press('winleft')
pyautogui.write('explorer')
time.sleep(1)
pyautogui.press('enter')

# Pasta de origem das imagens webp
pasta_origem = "C:/Users/ti3/OneDrive/imagens.webp"

# Pasta de destino para as imagens convertidas
pasta_destino = "C:/Users/ti3/OneDrive/Área de Trabalho/imagens.jpeg"

# Lista todos os arquivos na pasta de origem
arquivos = os.listdir(pasta_origem)

# Loop sobre cada arquivo na pasta de origem
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem webp
    if arquivo.endswith(".webp"):
        # Abre a imagem webp
        caminho_completo = os.path.join(pasta_origem, arquivo)
        imagem = Image.open(caminho_completo)

        # Remove a extensão .webp do nome do arquivo e adiciona a extensão .jpeg
        nome_arquivo_jpeg = os.path.splitext(arquivo)[0] + ".jpeg"
        caminho_destino = os.path.join(pasta_destino, nome_arquivo_jpeg)

        # Converte e salva a imagem como JPEG na pasta de destino
        imagem.convert("RGB").save(caminho_destino, "JPEG")

        # Fecha a imagem
        imagem.close()

# Caminho para a pasta contendo as imagens originais
caminho_pasta_origem = "C:/Users/ti3/OneDrive/Área de Trabalho/imagens.jpeg"
# Caminho para a pasta onde as imagens redimensionadas serão salvas
caminho_pasta_destino = "C:/Users/ti3/OneDrive/Área de Trabalho/imagens.png 600x600"

# Verifica se o caminho da pasta de origem existe
if os.path.exists(caminho_pasta_origem):
    # Se o caminho da pasta de destino não existe, cria a pasta
    if not os.path.exists(caminho_pasta_destino):
        os.makedirs(caminho_pasta_destino)

    # Lista todos os arquivos na pasta de origem
    arquivos = os.listdir(caminho_pasta_origem)

    # Itera sobre todos os arquivos na pasta de origem
    for arquivo in arquivos:
        # Verifica se o arquivo é uma imagem
        if arquivo.endswith(".jpeg") or arquivo.endswith(".png"):
            # Caminho completo para o arquivo de origem
            caminho_arquivo_origem = os.path.join(caminho_pasta_origem, arquivo)
            # Abre a imagem
            imagem = Image.open(caminho_arquivo_origem)
            # Redimensiona a imagem para 600x600 pixels
            imagem_redimensionada = imagem.resize((600, 600))
            # Caminho completo para o arquivo de destino
            caminho_arquivo_destino = os.path.join(caminho_pasta_destino, arquivo)
            # Salva a imagem redimensionada
            imagem_redimensionada.save(caminho_arquivo_destino)
            print(f"Imagem {arquivo} redimensionada com sucesso.")
else:
    print("O caminho da pasta de origem não existe.")


print("Conversão concluída.")

pyautogui.alert("O Script TERMINOU! \n Você PODE a usar o PC agora!")




