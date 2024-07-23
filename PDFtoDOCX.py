import tabula
import pandas as pd

def pdf_to_xlsx(pdf_file, xlsx_file):
    tables = tabula.read_pdf(pdf_file, pages="all", multiple_tables=True)
    
    with pd.ExcelWriter(xlsx_file) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f"Sheet{i+1}", index=False)

pdf_file = "C:/Users/ti3/Downloads/PRICE - CBM.pdf"
xlsx_file = "C:/Users/ti3/Downloads/PRICE - CBM.xlsx"
pdf_to_xlsx(pdf_file, xlsx_file)



#C:/Users/ti3/Downloads/PRICE - CBM.pdf





