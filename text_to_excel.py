import time
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://bedinsat.com.br/panel/_login.php")

arquivo_entrada_pt_br = "C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/Titulos/titulos pt-br.txt"

arquivo_entrada_en = "C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/Titulos/titulo.txt"

arquivo_entrada_es = "C:/Users/ti3/OneDrive/Área de Trabalho/autoPython/Titulos/titulos es.txt"

while True:
    with open(arquivo_entrada_pt_br, 'r', encoding='utf-8') as arquivoBR, \
         open(arquivo_entrada_en, 'r', encoding='utf-8') as arquivoEN, \
         open(arquivo_entrada_es, 'r', encoding='utf-8') as arquivoES:
             
        while True:
            tituloBR = arquivoBR.readline().strip()
            tituloEN = arquivoEN.readline().strip()
            tituloES = arquivoES.readline().strip()

            if not tituloBR and not tituloEN and not tituloES:
                break

            navegador.find_element("xpath", '/html/body/div[4]/div/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input[1]').send_keys(tituloBR)
            navegador.find_element("xpath", '/html/body/div[4]/div/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input[2]').send_keys(tituloEN)
            navegador.find_element("xpath", '/html/body/div[4]/div/div[2]/div[1]/form/table/tbody/tr[1]/td[2]/input[3]').send_keys(tituloES)

    time.sleep(100)
