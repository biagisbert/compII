import pandas as pd
import xlrd
ler = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\Exercicio_1\\dados\\WHO POP TB some.xls.xls")
print('Valor Maximo de mortes = %s' %ler['TB deaths'].max())
print('Valor Minimo de mortes = %s' %ler['TB deaths'].min())