import sys
import pandas as pd
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline

blast_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastx.exe"
out_blast = "C:\\Users\\bia_g\\PycharmProjects\\compII\\Projeto_Final\\dados\\out.blastp.outfmt6.fasta"

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
   'gene_id': dt['gene_id'],
   'Rep1_A_CPM': dt['Rep1_A'] * fatorNormalizado_Rep1_A,
   'Rep2_A_CPM': dt['Rep2_A'] * fatorNormalizado_Rep2_A,
   'Rep1_B_CPM': dt['Rep1_B'] * fatorNormalizado_Rep1_B,
   'Rep2_B_CPM': dt['Rep2_B'] * fatorNormalizado_Rep2_B}

dt_normalizado = pd.DataFrame(data_normalizado, columns=['gene_id', 'Rep1_A_CPM', 'Rep2_A_CPM', 'Rep1_B_CPM',
                                                         'Rep2_B_CPM'])

df = pd.merge(dt, dt_normalizado)

data_media = {
   'gene_id': df['gene_id'],
   'Rep1_A_CPM': df['Rep1_A_CPM'],
   'Rep2_A_CPM': df['Rep2_A_CPM'],
   'Rep1_B_CPM': df['Rep1_B_CPM'],
   'Rep2_B_CPM': df['Rep2_B_CPM'],
   'Cond_A_CPM_media': ((df['Rep1_A_CPM']+df['Rep2_A_CPM'])/2),
   'Cond_B_CPM_media': ((df['Rep1_B_CPM']+df['Rep2_B_CPM'])/2)}

df_media = pd.DataFrame(data_media, columns=['gene_id', 'Rep1_A_CPM', 'Rep2_A_CPM', 'Rep1_B_CPM', 'Rep2_B_CPM',
                                             'Cond_A_CPM_media', 'Cond_B_CPM_media'])

df_final = pd.merge(df, df_media)

asc_A = pd.DataFrame(df_final.nlargest(5, 'Cond_A_CPM_media'))
asc_B = pd.DataFrame(df_final.nlargest(5, 'Cond_B_CPM_media'))
id_gene = asc_A['gene_id'].append(asc_B['gene_id'])

