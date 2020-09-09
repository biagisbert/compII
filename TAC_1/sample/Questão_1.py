refArquivo = open("C:\\Users\\bia_g\\PycharmProjects\\compII\\TAC_1\\dados\\TcCLB.506717.80_AA.fasta")
arquivoFasta = refArquivo.read()
cabecalho = arquivoFasta.split('\n')[0][1:24]
sequencia = ''.join(arquivoFasta.split('\n')[1:])
print (("Identificador: %s"%cabecalho)),'\t',("Sequencia: %s"%sequencia)
refArquivo.close()