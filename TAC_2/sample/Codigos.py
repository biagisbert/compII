import pandas as pd
import xlrd
import sys
Teste_Geral=sys.argv[0]
tabela=sys.argv[1]
coef_m=float(sys.argv[2])
coef_b=float(sys.argv[3])
df = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados\\Valores_CT.xlsx")
quantity = 10**((df['CT']-b)/m)
df_q = pd.DataFrame({'Target_Name' : df['Target_Name'] ,
                     'Stage' : df['Stage'] ,
                     'Quantity': quantity})
df_final = pd.merge(df,df_q)
df_final.to_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados" , sheet_name="Ct_Abs")
print (df_final)