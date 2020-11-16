#ler da linha de comando: 1-tabela 1; 2-arquivo 1; 3-arquivo 2
# 1- Crie colunas adicionais na tabela.
# 1.1- Essas colunas vão receber os niveis de expressao normalizados por CPM
# 1.2- Nomeie como 'Rep1_a_CPM, Rep2_A_CPM, Rep1_V_CPM e Rep2_B_CPM
# 2- Crie mais colunas
# 2.1- Recebe a expressãp normalizada (CPM) media por condiçao
# 2.2- Nomeie as colunas como Cond_A_CPM_media e Cond_B_CPM_media
# 3- Selecione os  cinco genes mais expressos de cada condiçao baseado na expressao media
# 4- Faça uma busca BLAST da sequencia de DNA dos 10 genes selecionados anteriormente contra as sequencias de aminoacidos de R. prolixus
# 5- A partir do BLAST, imprimir o melhor hit de cada um dos genes baseado no bitscore
# 5.1- Caso o bitscore seja o mesmo, imprime o que tiver menor e-value
# 5.2- Caso permaneça, imprimi qualquer um dos dois
# A saida no terminal devera conter os seguintes dados:
## gene_id     Cond_A_CPM_media     Cond_B_CPM_media      id_proteína_encontrada
#### Onde gene_id é um dos genes mais expressos na condição A ou B;
#### Cond_A_CPM_media e Cond_B_CPM_media são os valores médios de CPM para cada condição
#### e id_proteína_encontrada é o identificador da sequência de proteína com melhor hit em R. prolixus.


#Caminho abrindo o terminal no projeto final:
# python PycharmProjects\compII\Projeto_Final\teste\Teste.py PycharmProjects\compII\Projeto_Final\dados\Tabela_1.xlsx PycharmProjects\compII\Projeto_Final\dados\Rdesconhecidus.fasta dados\VectorBase-48_RprolixusCDC_AnnotatedProteins.fasta
