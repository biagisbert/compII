import pandas as pd
import xlrd
ler = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\Exercicio_1\\dados\\WHO POP TB some.xls.xls")
brics = ler.iloc[[1,2,5,8,10]]
total = brics.sum()
media = total['TB deaths']//5
print('Total =  %s' %total['TB deaths'])
print("Media = %s" %media)