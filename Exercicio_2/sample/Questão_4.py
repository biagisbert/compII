seq = input("Digite a sequencia: ")
coord_exon_1 = input("Digite a coordenada do primeiro exon: ").split(";")
coord_exon_2 = input("Digite a coordenada do segundo exon: ").split(";")
exon_1 = seq[int(coord_exon_1[0])-1:int(coord_exon_1[1])]
exon_2 = seq[int(coord_exon_2[0])-1:int(coord_exon_2[1])]
seq_final = exon_1 + exon_2
print(seq_final)
