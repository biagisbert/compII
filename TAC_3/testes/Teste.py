#Usar o arquivo sequencias.fasta
#O programa tem que criar arquivos e em cada arquivo
# precisa que tenha uma sequencia, chamando de
# sequencia_i.fasta(onde i varia de 1 a N)#
## exemplo: arquivo FASTA que contém duas sequências
#>seq1=AAAAA
#>seq2=TTTTT
## vocês vão criar 2 arquivos chamados sequencia_1.fasta e sequencia_2.fasta
## onde cada um dos arquivos tem apenas uma sequencia
from Bio.Seq import Seq
from Bio import SeqIO
arquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\sequencias.fasta")
for i in SeqIO.parse(arquivo,"fasta"):
    new = SeqIO.write(i,"sequencia_i.fasta","fasta")
print('fim')