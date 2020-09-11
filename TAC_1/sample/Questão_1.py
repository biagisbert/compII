refArquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\TcCLB.506717.80_AA.fasta")
cabecalho = refArquivo.readline()[1:-1]
sequencia = ""
for linha in refArquivo:
    sequencia += linha.replace('\n','')
print (("Cabecalho: %s"%cabecalho),'\t',("Sequencia: %s"%sequencia))
refArquivo.close()