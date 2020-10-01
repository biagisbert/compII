import pandas as pd
import xlrd
import sys
arquivo = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados\\Valores_CT.xlsx")
tabela = sys.argv[1]
coef_b = sys.argv[2]
coef_m = sys.argv[3]
print (sys.argv)



