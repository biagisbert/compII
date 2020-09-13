refArquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
cabecalho = refArquivo.readline()[:]
sequencia = ""
for linha in refArquivo:
    if '>' in linha:
        print("Sequencia: %s" % sequencia)
        print ("Cabecalho: %s"%linha)
        sequencia = ""
    else:
        sequencia += linha.replace('\n','')
print("Sequencia: %s" % sequencia)
refArquivo.close()