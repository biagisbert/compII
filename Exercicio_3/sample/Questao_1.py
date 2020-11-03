num = int(input("Digite um numero, quando terminar digite 0: "))
lista = [num]
soma = 0
count_p = 0
count_n = 0
while num != 0:
    num = int(input("Digite outro numero: "))
    lista.append(num)
lista.remove(0)
media = sum(lista)/len(lista)
for i in lista:
    if i > 0:
        count_p = count_p + 1
    if i < 0:
        count_n = count_n + 1
perc_p = float((count_p*100)/len(lista))
perc_n = float((count_n*100)/len(lista))
print("Media Aritmetica : %s" % media)
print("Quantidade de positivos : %s" % count_p)
print("Quantidade de negativos : %s" % count_n)
print("Porcentagem de numeros positivos: %s" % perc_p)
print("Porcentagem de numeros negativos: %s" % perc_n)
