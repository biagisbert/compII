refArquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
cabecalho = refArquivo.readline()[0:-1]
sequencia = ""
for linha in refArquivo:
    sequencia += linha.replace('\n','')
    print ("Cabecalho: %s"%linha)
    print ("Sequencia: %s"%sequencia)
refArquivo.close()