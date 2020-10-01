import pandas as pd
import sys
df = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados\\Valores_CT.xlsx")
tabela = sys.argv[1]
coef_b = float(sys.argv[2])
coef_m = float(sys.argv[3])
df_q = df[['Target_Name' , 'Stage']]
df_q['Quantity'] = 10 ** ((df['CT'] - coef_b)/coef_m)
df_final = pd.merge(df,df_q)
df_final.to_excel(("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_2\\dados\\Tabela_Quant_Abs.xlsx"))
print (df_final)
