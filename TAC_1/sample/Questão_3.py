import csv
with open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\species.csv") as ArquivoEntrada:
    ArquivoLeitura = csv.reader(ArquivoEntrada)
    for linha in ArquivoLeitura:
        data = linha.split(",")
        if data[3].upper().rstrip() == "BIRD":
            print("%s\t%s\t%s\t%s" % (data[0], data[1], data[2], data[3].rstrip()))
    ArquivoEntrada.close()