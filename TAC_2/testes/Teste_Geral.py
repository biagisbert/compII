import pandas as pan
import xlrd
import sys
tabela = sys.argv[1]
coef_b = float(sys.argv[2])
coef_m = float(sys.argv[3])
df = pan.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados\\Valores_CT.xlsx")
df_q = df['Target_Name' , 'Stage']
df_q['Quantity'] = 10 ** ((df['CT'] - coef_b)/coef_m)
df_final = pan.merge(df,df_q)
df_final.to_excel(("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados\\Tabela_Quant_Abs.xlsx"))
print (df_final)
