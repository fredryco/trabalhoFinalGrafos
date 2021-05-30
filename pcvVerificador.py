#!/usr/bin/python

import math, re, sys
import pcvVisitas as visita

# forma como deve ser utilizado: python verificador.py arquivoEntrada arquivoFinal

def main(arquivoEntrada, arquivoFinal):

    visita.main(arquivoEntrada, arquivoFinal)
	
    cidades = leitura(arquivoEntrada)
    solucao = leituraSolucao(arquivoFinal)
    checarSolucao(cidades, solucao[0][0], solucao[1])
    
def distancia(a,b):
    # a e b são pares inteiros 
    # Distância euclidiana arredondada para o número inteiro mais próximo:
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    #equivalente à próxima linha
    return int(round(math.sqrt(dx*dx + dy*dy)))
    
def leitura(arquivo):
    # cada linha do arquivo de entrada representa uma cidade dada por três inteiros:
    # identificador coordenada x coordenada y (separada por espaço)
    # identificadores de cidade são sempre inteiros consecutivos começando com 0
    # (embora isso não seja assumido aqui explicitamente,
    # será um requisito para corresponder ao arquivo de solução)
    f = open(arquivo,'r')
    linhaArq = f.readline()
    cidades = []
    while len(linhaArq) > 1:
        converterLinha = re.findall(r'[^,;\s]+', linhaArq)
        cidades.append([int(converterLinha[1]),int(converterLinha[2])])
        linhaArq = f.readline()
    f.close()
    return cidades

def leituraSolucao(arquivo):
    # primeira linha é o comprimento da solução
    # linhas restantes são as cidades na ordem em que são visitadas
    # cada cidade é listada uma vez
    # cidades são identificadas por números inteiros de 0 a n-1

    # leitura do tamanho da caminhada(rota)
    f = open(arquivo,'r')
    valor = int(f.readline())

    # leitura das cidades
    solucao = []
    linhaArq = f.readline()
    while len(linhaArq) > 1:
        converterLinha = re.findall(r'[^,;\s]+', linhaArq)
        solucao.append(int(converterLinha[0]))
        linhaArq = f.readline()
    f.close()

    return [[valor], solucao]

def checarSolucao(cidades, valor, ordemCidades):
    # calcular o do passeio fornecido usando a ordem das cidades:
    n = len(cidades)
    dist = 0
    for i in range(n):
        dist = dist + distancia(cidades[ordemCidades[i]],cidades[ordemCidades[i - 1]])
    
    # verifica o valor da solução
    if dist == valor:
        print('solução encontrada de comprimento ', valor)
    else:
        print('comprimento da solução dado como ', valor)
        print('mas calculado como ', dist)

    # verifica todas as cidades
    n = len(cidades)
    ordemCidades.sort()
    for i in range(n):
        if not(ordemCidades[i] == i):
            print('cidade nao encontrada: ', i)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
