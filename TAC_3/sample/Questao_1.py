from Bio.Seq import Seq
seq = Seq(input("Digite uma sequencia de DNA: "))
mRNA = seq.transcribe()
protein = mRNA.translate()
print(mRNA)
print(protein)
