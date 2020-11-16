import pandas as pd
import numpy as np
import sys
from Bio import SeqIO

#Caminho abrindo o terminal no projeto final: python teste\Teste.py dados\Tabela_1.xlsx dados\Rdesconhecidus.fasta dados\VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta
Tabela_1 = sys.argv[1]
seq_desconhecida = sys.argv[2]
arquivo_multi = sys.argv[3]

dt = pd.read_excel(Tabela_1)
dd = SeqIO.parse(seq_desconhecida, "fasta")
dm = SeqIO.parse(arquivo_multi, "fasta")

fatorNormalizado_Rep1_A = 10**6/dt['Rep1_A'].sum()
fatorNormalizado_Rep2_A = 10**6/dt['Rep2_A'].sum()
fatorNormalizado_Rep1_B = 10**6/dt['Rep1_B'].sum()
fatorNormalizado_Rep2_B = 10**6/dt['Rep2_B'].sum()

data_normalizado = {
   'gene_id' : dt['gene_id'],
   'Rep1_A_CPM' : dt['Rep1_A'] * fatorNormalizado_Rep1_A,
   'Rep2_A_CPM': dt['Rep2_A'] * fatorNormalizado_Rep2_A,
   'Rep1_B_CPM': dt['Rep1_B'] * fatorNormalizado_Rep1_B,
   'Rep2_B_CPM': dt['Rep2_B'] * fatorNormalizado_Rep2_B}

dt_normalizado = pd.DataFrame(data_normalizado, columns=['gene_id','Rep1_A_CPM','Rep2_A_CPM','Rep1_B_CPM','Rep2_B_CPM'])

df = pd.merge(dt,dt_normalizado)

data_media = {
   'gene_id' : df['gene_id'],
   'Rep1_A_CPM' : df['Rep1_A_CPM'],
   'Rep2_A_CPM': df['Rep2_A_CPM'],
   'Rep1_B_CPM': df['Rep1_B_CPM'],
   'Rep2_B_CPM': df['Rep2_B_CPM'],
   'Cond_A_CPM_media' : ((df['Rep1_A_CPM']+df['Rep2_A_CPM'])/2),
   'Cond_B_CPM_media' : ((df['Rep1_B_CPM']+df['Rep2_B_CPM'])/2)}

df_media = pd.DataFrame(data_media, columns=['gene_id','Rep1_A_CPM','Rep2_A_CPM','Rep1_B_CPM','Rep2_B_CPM',
                                            'Cond_A_CPM_media','Cond_B_CPM_media'])

df_final = pd.merge(df,df_media)
#ver um jeito de pegar os 5 maiores nos dois
#obs: nao precisa printar
asc_A = df_final.sort_values('Cond_A_CPM_media')
print(asc_A['Cond_A_CPM_media'])
asc_B = df_final.sort_values('Cond_B_CPM_media')
print(asc_B['Cond_B_CPM_media'])

#Fazer a função do BLAST




#Revisar o codigo