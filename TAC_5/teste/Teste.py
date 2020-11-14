import TAC_5.lib.operacõesCompra as tc

dic = {}
while True:
    produto = input("Digite o produto: ")
    if produto == "-1":
        break
    preco = float(input("Digite o preço: "))
    if preco == -1:
        break
    quantidade = int(input("Digite a quantidade: "))
    if quantidade == -1:
        break
    dic[produto] = [preco, quantidade]

prod = tc.imprimeProdutos(dic)
quant = tc.imprimeQuantidades(dic)
calculo = tc.calculaTotalCompra(dic)
