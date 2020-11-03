import re
from Bio.Seq import Seq
from Bio import SeqIO
#input do motivo
motivo = str(input("Digite sua sequencia: "))
arquivo = "C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta"

for record in SeqIO.parse(arquivo, "fasta"):
    print("ID %s" % record.id)
