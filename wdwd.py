codigo = "U2027C"

arquivo_entrada = "C:/Users/User/Desktop/Scraping and Writing/autoPython/Titulos/tituloEN.txt"

descricao = None

with open(arquivo_entrada, 'r') as entrada:
    encontrou_codigo = False
    
    # Itera sobre as linhas do arquivo de entrada
    for linha in entrada:
        # Se a palavra for encontrada, define como True
        if codigo in linha:
            encontrou_codigo = True
            continue 
        
        if encontrou_codigo:
            descricao = linha.strip()  
            break  

print(descricao)