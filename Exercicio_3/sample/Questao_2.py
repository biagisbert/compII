name = input("Digite o nome do aluno: ")
i = 0
note = int(input("Digite uma nota: "))
notas = note
while i != 2:
    note = int(input("Digite outra nota: "))
    notas = note + notas
    i = i + 1
faltas = input("Digite o numero de faltas: ")
media = float(notas/3)
presenca = float((int(faltas)*100)/80)
if media < 7:
    if presenca >= 25:
        print("Aluno reprovado por falta")
    else:
        print("Aluno reprovado por media inferior a 7")
if media >= 7:
    print("Aluno aprovado!")
