import re
from Bio.Seq import Seq
from Bio import SeqIO

def Counting_Motifs(sequence,motif):
    gene=str(line.id)
    mc=sequence.count(motif)
    if mc!=0:
        print("Identificador:",gene,"Motivo",motif,"Count",mc,sep="")

motif=str(input("Insira seu motivo de DNA ou AA:")).upper()

if re.search('^[ACGT]+$',motif):
    print("É uma sequencia de DNA")
    mulfasta = SeqIO.parse(open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta",'r'),"fasta")
    for line in mulfasta:
        sequencia=str(line.seq)
        Counting_Motifs(sequencia,motif)
else:
    print("É uma sequencia de AA")
    multifasta=SeqIO.parse(open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta"),"fasta")
    for line in multifasta:
        sequence=str(line.seq)
        Counting_Motifs(sequence,motif)