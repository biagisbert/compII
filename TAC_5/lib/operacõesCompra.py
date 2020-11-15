def imprimeProdutos(dic):
    print("Relação de Produtos")
    for e in dic:
        print(e)

def imprimeQuantidades(dic):
    print("Relação de Produtos e Quantidade")
    for e in dic:
        print(e, '\t', dic[e][1])

def calculaTotalCompra(dic):
    print("Relação de Produtos e Preço")
    total = 0
    for e in dic:
        valor = dic[e][0] * dic[e][1]
        total = total + valor
        print(e, '\t', total)
    print("Total da compra: %s" %total)
