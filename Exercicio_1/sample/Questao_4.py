import pandas as pd
import xlrd
ler=pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\Exercicio_1\\dados\\WHO POP TB some.xls.xls")
soma = ler['TB deaths'].sum()//12
mediana = ler['TB deaths'].iloc[[0,1]].sum()
med = mediana//2
print("Numero medio = %s" %soma)
print( "Mediana = %s" %med)