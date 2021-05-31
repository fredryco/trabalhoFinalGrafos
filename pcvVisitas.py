#!/usr/bin/python

import math, re, sys

# forma como deve ser utilizado: python pcvVerificador.py arquivoEntrada arquivoFinal

def main(arquivoEntrada, arquivoFinal):
	valoresEntrada = leituraValoresEntrada(arquivoEntrada)
	
	valoresSaida = leituraValoresSaida(arquivoFinal)
	problema = calculoChecagem(valoresEntrada, valoresSaida)
	
	
	if( len(problema) == 0):
		print('Cada item parece existir no arquivo de entrada e no arquivo de saída.')
	else:
		print('possível problema inclui:\n')
		for p in problema:
			print(problema[p])
	
def leituraValoresEntrada(arquivoEntrada):
	# cada linha de in_file deve ter um rótulo como seu primeiro int em cada linha,
	# captura uma lista dessas etiquetas
	# (esperado de 0 a n - 1, mas apenas a exclusividade é necessária)
	
	arquivo = open(arquivoEntrada,'r')
	linha = arquivo.readline()
	
	#locais rastreia os pontos como a chave e o número de visitas
	locais = []
	while len(linha) > 1:
		conversorLinha = re.findall(r'[^,;\s]+', linha)
		locais.append(int(conversorLinha[0]))
		linha = arquivo.readline()
	arquivo.close()
	
	locais = sorted(locais)
	
	return locais
	
def leituraValoresSaida(arquivoSaida):
	# cada linha de arquivoEntrada deve ter um rótulo como seu primeiro int em cada linha,
	# captura uma lista desses itens
	
	arquivo = open(arquivoSaida,'r')
	
	arquivo.readline()
	
	linha = arquivo.readline()
	
	locais = []
	while len(linha) > 1:
		conversorLinha = re.findall(r'[^,;\s]+', linha)
		locais.append(int(conversorLinha[0]))
		linha = arquivo.readline()
	arquivo.close()
	
	locais = sorted(locais)
	
	return locais

def calculoChecagem(list_a, list_b):
	problema = dict()
	
	if(len(list_a) != len(list_b) ):
		problema[-1] = ('Número diferente de pontos nos arquivos, então eles não podem coincidir.')
	
	desloc_1 = 0
	desloc_2 = 0
	contadorProblemas = 0
	while (desloc_1 < len(list_a) ) and (desloc_2 < len(list_b) ):
		item_1 = list_a[desloc_1]
		item_2 = list_b[desloc_2]
				
		if(item_1 < item_2):
			problem = (str(desloc_1) + ' faltando na saída.')
			problema[desloc_1] = problem
			
			desloc_1 += 1
			contadorProblemas += 1
		elif(item_1 > item_2):
			problem = (str(desloc_2) + ' faltando na saída.')
			problema[desloc_1] = problem
			
			desloc_2 += 1
			contadorProblemas += 1
		else:
			desloc_1 += 1
			desloc_2 += 1
			
	return problema
