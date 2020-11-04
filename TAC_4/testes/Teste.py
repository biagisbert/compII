import re
from Bio import SeqIO
motivo = input("Digite sua sequencia: ").upper()
arquivo = "C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta"
ref_arquivo = SeqIO.parse(arquivo, "fasta")
count = 0
if re.search('^[ACGT]+$',motivo):
    print("É uma sequencia de DNA")
    for line in ref_arquivo:
        print("ID %s" % str(line.id))
        count = count +1
    print("O motivo se repete %s vezes" % count)
else:
    print("É uma sequencia de aminoácidos")
    for line in ref_arquivo:
        print("ID %s" % str(line.id))
        count = count + 1
    print("O motivo se repete %s vezes" % count)
