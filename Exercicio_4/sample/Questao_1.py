def quant(lista):
    return len(lista)
def ordem(lista):
    print(lista)
def inversa(lista):
    for e in lista[::-1]:
        print(e)
def soma(lista):
    soma = 0
    for e in lista:
        soma = e + soma
    return soma
def media(lista):
    return soma(lista)/len(lista)
def val_acima(lista):
    total = 0
    for e in lista:
        if e > media(lista):
            total = total + 1
    return total
num = int(input("Digite um numero: "))
lista = [num]
while num != -1:
    num = int(input("Digite outro numero: "))
    lista.append(num)
lista.remove(num)
print("Quantidade de numeros que foram lidos", quant(lista))
print("Valores na ordem, um ao lado do outro:"), ordem(lista)
print("Valores na ordem inversa, um abaixo do outro:"), inversa(lista)
print("Soma dos valores: ", soma(lista))
print("Media dos valores: ", media(lista))
print("Quantidade de valores acima da media:", val_acima(lista))
