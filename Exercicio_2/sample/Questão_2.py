seq = input("Digite a sequencia do aminoacido: ").upper()
bases = {'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0}
for e in seq:
    bases[e] = bases[e] +1
for e in bases:
    bases[e] = round(((bases [e]/len(seq))*100),2)
print(bases)