import argparse
from math import sqrt
import itertools
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='nomeArquivo', default='pcvExemplo1.txt', required=False, help="informe a localização do arquivo de entrada")

def leitura_arquivo(file):
	lines = open(file).readlines()
	return [line[1:].strip().split(' ') for line in lines]

def escrita_arquivo(file, line):
	with open(file + ".passeio", "a") as output:
		output.write(" ".join(line))
		output.write('\n')

def calculoDistancia(p1, p2):
	return sqrt((int(p2[0]) - int(p1[0])) ** 2 + (int(p2[1]) - int(p1[1])) ** 2)

def gerarMatrizDistancia(coordinates):
	matrix = []
	for a in coordinates:
		row = []
		for b in coordinates:
			row.append(calculoDistancia(a,b))
		matrix.append(row)
	return matrix

class PCV():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
 
    #função de para imprimir o PCV construído usando o pai []
    def obtemPCV(self, pai):
        PCV = []
        for i in range(1,self.V):
        	limite = (pai[i], i, self.graph[i][pai[i]])
        	PCV.append(limite)
        return PCV
 
    # Uma função de utilidade para encontrar o vertice com valor mínimo de distância, do
    # conjunto de vértices ainda não incluído na árvore do caminho mais curto
    def minVet(self, vet, cnjPCV):
 
        min = sys.maxint
 
        for v in range(self.V):
            if vet[v] < min and cnjPCV[v] == False:
                min = vet[v]
                index = v
 
        return index
 
    # Função para construir e imprimir PCV
    def imprimirPCV(self):
 
        vet = [sys.maxint] * self.V
        pai = [None] * self.V 
        vet[0] = 0   
        cnjPCV = [False] * self.V
 
        pai[0] = -1  # Raiz
 
        for cout in range(self.V):
 
            # Escolhe a distância mínima no conjunto de vértices ainda não processado.
            u = self.minVet(vet, cnjPCV)
 
            # Adiciona a distância mínima
            cnjPCV[u] = True
 
            # Atualizar o valor da distancia dos vértices adjacentes do vertice escolhido
            # apenas se a distância atual for maior que a nova distância e
            # o vertice não está na árvore do caminho mais curto
            for v in range(self.V):
                if self.graph[u][v] > 0 and cnjPCV[v] == False and\
                   vet[v] > self.graph[u][v]:
                        vet[v] = self.graph[u][v]
                        pai[v] = u
 
        return self.obtemPCV(pai)


def vertices_PCV(M, number_of_nodes):
    #Retorna os vértices com grau ímpar na árvore de abrangência mínima (PCV). "" "
	vertices = [0 for i in range(number_of_nodes)]
	for u,v,d in M:
		vertices[u] = vertices[u] + 1
		vertices[v] = vertices[v] + 1
	vertices = [vert for vert, degree in enumerate(vertices) if degree % 2 == 1]
	return vertices

def grafoBipartiteFunc(M, conjuntoBipartido, vertices):

	grafoBi = []
	conjuntoVertice = []
	for arrayVertices1 in conjuntoBipartido:
		arrayVertices1 = list(sorted(arrayVertices1))
		arrayVertices2 = []
		for vert in vertices:
			if vert not in arrayVertices1:
				arrayVertices2.append(vert)
		matrix = [[-1000000 for j in range(len(arrayVertices2))] for i in range(len(arrayVertices1))]
		for i in range(len(arrayVertices1)):
			for j in range(len(arrayVertices2)):
				if arrayVertices1[i] < arrayVertices2[j]:
					matrix[i][j] = M[arrayVertices1[i]][arrayVertices2[j]]
				else:
					matrix[i][j] = M[arrayVertices2[j]][arrayVertices1[i]]
		grafoBi.append(matrix)
		conjuntoVertice.append([arrayVertices1,arrayVertices2])
	return [grafoBi, conjuntoVertice]

def main():
    user_args = parser.parse_args()
    array_of_lines = leitura_arquivo(user_args.file_name)
    mst = PCV(len(array_of_lines))
    mst.graph = gerarMatrizDistancia(array_of_lines)
    triples = mst.imprimirPCV()
    
    print(triples)

    vertices = vertices_PCV(triples, len(array_of_lines))
    print(vertices)

    conjuntoBipartido = [set(i) for i in itertools.combinations(set(vertices), len(vertices)/2)]
    print(conjuntoBipartido)

    grafoBi = grafoBipartiteFunc(mst.graph, conjuntoBipartido, vertices)
    print(grafoBi)

if __name__ == "__main__":
    main()