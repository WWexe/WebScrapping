# Caminho do arquivo de texto
caminho_arquivo_inicial = 'C:/Users/User/Desktop/Scraping and Writing/autoPython/Codes py/titulos pt-br.txt'
caminho_arquivo_final = 'C:/Users/User/Desktop/Scraping and Writing/autoPython/Codes py/codigos.txt'

# Lista para armazenar os títulos
texto = []

with open(caminho_arquivo_inicial, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            texto.append(linha)
            
with open(caminho_arquivo_final, 'w', encoding='utf-8') as arquivoFinal:        
    for titulo in texto:
        palavras = titulo.split()

        ultima_palavra = palavras[-1]

        arquivoFinal.write(ultima_palavra + '\n')
