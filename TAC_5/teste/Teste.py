dic = {}
while True:
    produto = input("Digite o produto: ")
    if produto == -1:
        break
    preco = float(input("Digite o preço: "))
    if preco == -1:
        break
    quant = input("Digite a quantidade: ")
    if quant == -1:
        break
    dic[produto] = [preco, quant]
print(dic)