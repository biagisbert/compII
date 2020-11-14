def imprimeProdutos(dic):
    for e in dic:
        print(e)

def imprimeQuantidades(dic):
    for e in dic:
        print(e, '\t', dic[e][1])

def calculaTotalCompra(dic):
    for e in dic:
        total = dic[e][0] * dic[e][1]
        print(e, '\t', total)
