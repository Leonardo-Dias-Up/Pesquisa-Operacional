import  tabula
import os 
from PyPDF2 import PdfFileReader, PdfFileMerger
import pdfplumber
import pytesseract
import cv2 
import datetime
import pandas as pd

tabula.environment_info()

pdf_path = r"D:\04. Consecon\Projetos\Farmacia\TCC-Matheus-Lopes-de-Matos-2018.1.pdf"

dfs = tabula.read_pdf(pdf_path, stream=True, pages=22)
# read_pdf returns list of DataFrames
print(len(dfs))
dfs
df = dfs[0]
# df1 = dfs[1]
# df1.to_excel(r'D:\04. Consecon\Projetos\Farmacia\tables2_pg18.xlsx')

df.to_excel(r'D:\04. Consecon\Projetos\Farmacia\tables_pg18.xlsx')








