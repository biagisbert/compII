import pandas as pd
import xlrd
ler = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\Exercicio_1\\dados\\WHO POP TB some.xls.xls")
normalizar = ler['TB deaths'].mul(100)
print (normalizar)