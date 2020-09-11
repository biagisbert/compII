refArquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
cabecalho = refArquivo.readline()[0:-1]
sequencia = ""
for linha in refArquivo:
    if '>' in linha:
        print ("Cabecalho: %s"%linha)
    else:
        sequencia = linha
    print ("Sequencia: %s"%sequencia)
refArquivo.close()