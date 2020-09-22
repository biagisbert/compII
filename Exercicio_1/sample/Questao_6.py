import pandas as pd
import xlrd
ler = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\Exercicio_1\\dados\\WHO POP TB some.xls.xls")
normalizar = ler['TB deaths'].mul(100)
taxa = normalizar/ler['Population (1000s)']
pop = ler['Population (1000s)']/100
nova = pd.DataFrame({'Country' : ler['Country'],
                     'Population(100.000)' : pop,
                    'Taxa de morte' : taxa})
print (nova)