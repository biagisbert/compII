from Bio import SeqIO
arquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\sequencias.fasta")
count = 1
for i in SeqIO.parse(arquivo,"fasta"):
    arg = ("sequencia_")+count.__str__()
    new = SeqIO.write(i,arg,"fasta")
    count = count+1
print('fim')
##Salvaram 837 arquivos na pasta do sample, transferi eles manualmente para os dados##