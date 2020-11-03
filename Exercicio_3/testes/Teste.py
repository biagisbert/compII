altura = float(input("Digite sua altura : "))
peso = float(input("Digite seu peso em : "))
IMC = round((peso/altura),2)
if IMC < 18.5:
    print("Abaixo do peso.")
elif 18.5 >= IMC < 25:
    print("Peso normal.")
elif 25 >= IMC < 30:
    print("Acima do peso.")
elif IMC > 30:
    print("Obeso.")
else:
    print("ERROR")
