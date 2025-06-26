arquivo = open('Analise Simples de CSV/notas.csv', 'r')
linhas = arquivo.readlines()[1:]
notas = []
nomes = []

for linha in linhas:
    nome, nota = linha.strip().split(',')
    nomes.append(nome)
    notas.append(float(nota))

arquivo.close()

total = len(notas)
media = sum(notas) / total
nota_maxima = max(notas)
nota_minima = min(notas)
nome_maximo = nomes[notas.index(nota_maxima)]
nome_minimo = nomes[notas.index(nota_minima)]

resumo  = open('resumo.csv', 'w')
resumo.write('total,media,notamaxima,notaminima\n')
resumo.write(f'{total},{media:.2f},{nota_maxima},{nota_minima}\n')



