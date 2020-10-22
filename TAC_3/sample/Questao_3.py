import pandas as pd
from Bio.Blast.Applications import NcbiblastxCommandline
blast_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastx.exe"
arquivo_out = "C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_3\\dados\\out.blastp.outfmt6.fasta"
unknow_seq = open(input("Digite o caminho para a Sequencia desconhecida: "))
alvo_seq = open(input("Digite o caminho para a Sequencia alvo: "))
blast_line = NcbiblastxCommandline(cmd=blast_path, query=unknow_seq, subject=alvo_seq, outfmt=6, out= arquivo_out, evalue=0.05)
result_blast = pd.read_csv(arquivo_out, sep='\t', names=["qseqid","sseqid","pident","length","mismatch","gapopen","qstart","qend","sstart","send","evalue","bitscore"])
max_hit = result_blast.sort_values('bitscore')
print(max_hit.iloc[[-1]])
