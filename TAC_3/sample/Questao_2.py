from Bio import SeqIO
arquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\sequencias.fasta")
for i in SeqIO.parse(arquivo,"fasta"):
    arg = ("sequencia_"+i.id).__str__()
    new = SeqIO.write(i,arg,"fasta")
print('fim')
##Salvaram 837 arquivos na pasta do sample, transferi eles manualmente para os dados##