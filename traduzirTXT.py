from openpyxl import Workbook

def texto_para_excel(arquivo_texto, arquivo_excel):
    # Criar um novo arquivo Excel
    wb = Workbook()
    ws = wb.active
    
    # Abrir o arquivo de texto e ler seu conteúdo
    with open(arquivo_texto, 'r', encoding='latin-1') as file:
        linhas = file.readlines()
    
    # Escrever o conteúdo do arquivo de texto no arquivo Excel
    for i, linha in enumerate(linhas, start=1):
        # Dividir o texto em blocos separados por quebra de linha
        blocos = linha.split('\n')
        
        # Escrever cada bloco em células separadas na mesma linha
        for j, bloco in enumerate(blocos, start=1):
            ws.cell(row=i, column=j, value=bloco)
    
    # Salvar o arquivo Excel
    wb.save(arquivo_excel)
    print(f"Arquivo Excel '{arquivo_excel}' gerado com sucesso!")

# Nome do arquivo de texto de entrada
arquivo_texto = "C:/Users/ti3/OneDrive/Área de Trabalho/Atualizado/Scraping and Writing/descricoesES.txt"

# Nome do arquivo Excel de saída
arquivo_excel = "C:/Users/ti3/OneDrive/Área de Trabalho/Atualizado/Scraping and Writing/descricoesES.xlsx"

# Converter o arquivo de texto para Excel
texto_para_excel(arquivo_texto, arquivo_excel)

from openpyxl import load_workbook

def apagar_celulas_vazias_coluna1(arquivo_excel):
    wb = load_workbook(arquivo_excel)
    ws = wb.active
    
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=1):
        for cell in row:
            if cell.value is None:
                ws.delete_rows(cell.row, amount=1)
    
    wb.save(arquivo_excel)
    print("Células vazias da coluna 1 removidas com sucesso!")

arquivo_excel = "C:/Users/ti3/OneDrive/Área de Trabalho/Atualizado/Scraping and Writing/descricoesES.xlsx"

apagar_celulas_vazias_coluna1(arquivo_excel)


