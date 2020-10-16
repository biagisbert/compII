seq_1 = input("Sequencia 1: ").upper()
seq_2 = input("Sequencia 2: ").upper()
sequencia = seq_1 + seq_2
seq_final = ""
for e in sequencia:
    if e == "A":
        seq_final = seq_final + e.replace("A","T")
    elif e == "T":
        seq_final = seq_final + e.replace("T","A")
    elif e=="C":
        seq_final = seq_final + e.replace("C","G")
    elif e=="G":
        seq_final = seq_final + e.replace("G","C")
print(seq_final)