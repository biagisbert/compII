def calculaAreaRetangulo(x,y):
    if y == 0:
        return x*x
    else:
        return x*y
x = int(input("Digite o valor do lado: "))
y = int(input("Digite outro valor: "))
print(calculaAreaRetangulo(x,y))
