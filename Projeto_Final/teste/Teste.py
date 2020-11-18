import sys
import pandas as pd
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline

blastx_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastx.exe"
meuOutput = "C:\\Users\\bia_g\\PycharmProjects\\compII\\Projeto_Final\\dados\\out.blastp.outfmt6.fasta"

Tabela_1 = sys.argv[1]
seq_desconhecida = sys.argv[2]
arquivo_multi = sys.argv[3]

#(Tabela_1 = sys.argv[1]; seq_desconhecida = sys.argv[2]; arquivo_multi = sys.argv[3])
#Tabela_1
dt = pd.read_excel("C:\\Users\\bia_g\\PycharmProjects\\compII\\Projeto_Final\\dados\\Tabela_1.xlsx")
#seq_desconhecida
dd = SeqIO.parse("C:\\Users\\bia_g\\PycharmProjects\\compII\\Projeto_Final\\dados\\Rdesconhecidus.fasta", "fasta")
#arquivo_multi
dm = SeqIO.parse("C:\\Users\\bia_g\\PycharmProjects\\compII\\Projeto_Final\\dados\\VectorBase-48_RprolixusCDC_Annotated"
                 "Proteins.fasta", "fasta")

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
gene_cond = list(id_gene)

for i in gene_cond:
     nomeArq = str("{}.fasta").format(i)
     refArquivoSaida = open(nomeArq,"w")
     SeqIO.write(i, refArquivoSaida, "fasta")
     refArquivoSaida.close()
     sequencia = nomeArq
     refArquivoSaida.close()

     linha_de_comando_blastx = NcbiblastxCommandline(cmd=blastx_path, query=sequencia, subject=dm,
                                                         outfmt=6, out=meuOutput, evalue=0.05)
     stdout, stderr = linha_de_comando_blastx()


blast_result = open(meuOutput, "r")

qseqid = 0
sseqid = 1
pident = 2
length = 3
mismatch = 4
gapopen = 5
qstart = 6
qend = 7
sstart = 8
send = 9
evalue = 10
bitscore = 11

results = blast_result.read()
s = results.split('\n')
besthit = '0'
Evalue = 0
encontrada = '0'

for linha in s:
  hit = linha.split('\t')
  if len(hit) != 12:
      break
  if float(besthit) < float(hit[bitscore]):
      busca = hit[qseqid]
      besthit = hit[bitscore]
      Evalue = hit[evalue]
      encontrada = hit[sseqid]

  print("Sequência encontrada: %s" % encontrada)
  print("Score = %s" % besthit)
  print("E-value = %s" % Evalue)