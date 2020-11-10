vog = lambda caractere: caractere.upper() in "AEIOU"
conso = lambda caractere: caractere.upper() in "BCDFGHJKLMNPQRSTUXWZ"
num = lambda caractere: caractere in "1234567890"
frase = input("Digite uma frase: ")
total_vogal = 0
total_consoante = 0
total_numero = 0
total_outros = 0
for caractere in frase:
    if vog(caractere):
        total_vogal += 1
    elif conso(caractere):
        total_consoante += 1
    elif num(caractere):
        total_numero += 1
    else:
        total_outros += 1
print("Total de consoantes: %d" % total_consoante)
print("Total de vogais: %d" % total_vogal)
print("Total de números: %d" % total_numero)
print("Total de outros: %d" % total_outros)