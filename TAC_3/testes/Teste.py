##Executa BLAST da sequência desconhecida de DNA contra as sequências de aminoácidos usando formato de saída nº 6 e e-valor igual à 0,05
##Imprima somente o hit com o maior score.#
# C://Users//bia_g//PycharmProjects//compII//TAC_3//dados//sequenciaDesconhecida.fasta
# C://Users//bia_g//PycharmProjects//compII//TAC_3//dados//TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta
import pandas as pd
from Bio.Blast import Applications
from Bio.Blast.Applications import NcbiblastxCommandline

blast_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastp"
output =str("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\out.blastp.outfmt6.fasta")
unknow_seq = open("C://Users//bia_g//PycharmProjects//compII//TAC_3//dados//sequenciaDesconhecida.fasta")
seq_alvo = open("C://Users//bia_g//PycharmProjects//compII//TAC_3//dados//TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
print(unknow_seq)
blast_line = NcbiblastxCommandline(cmd=blast_path, query=unknow_seq, subject=seq_alvo, outfmt=6, out=output, evalue=0.05)
stdout = output
result_blast = pd.read_csv(output,sep='\t', names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])
max_hit = result_blast.sort_values('bitscore')
print(seq_alvo)