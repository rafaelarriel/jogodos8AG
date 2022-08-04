#Rafael Victor Marciano Arriel 201811050
#Renan Fernandes Guimaraes 201711917

import numpy as np
from enum import Enum
from random import randint

tabR = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

#Funçoes auxiliares
#############################################################################

#Imprime o tabuleiro 
def imprimeTab(tab): 
	  
  print(tab[0],tab[1],tab[2])
  print(tab[3],tab[4],tab[5])
  print(tab[6],tab[7],tab[8])

#Opção 3 do menu
def op3(tabinlis):
	
	print("Os atributos a serem expecificados serão: Geração Maxima, Tamanho da População, Tamanho do Chromosome")
	print("Numero de Chromosomes selecionados(Melhores), Range de incremento do Chromoome & Incremento de tamnaho do Chromosome")
	print("Se desejar usar algum atributo expecifico ainda como padrão(best) digite p\n")




	print("Geração Maxima | ou digite p para deixar como padrão:")
	x = input(">>")  
	if x == 'p':
		gerMAXIMA = int(1000)
	else:
		gerMAXIMA = int(x)
	


	print("Tamanho da população | ou digite p para deixar como padrão:")
	x = input(">>")
	if x == 'p':
		tamanhoPOPULACAO = int(20)
	else:
		tamanhoPOPULACAO = int(x)
	
	

	print("Tamanho do Chormosome | ou digite p para deixar como padrão:")
	x = input(">>")
	if x == 'p':
		tamanhoCHROMOSOME = int(20)
	else:
		tamanhoCHROMOSOME = int(x)
	
	

	print("Numero de Chromosomes selecionados(Melhores) | ou digite p para deixar como padrão:")
	x = input(">>")
	if x == 'p':
		numeroCHROMOSOME_select = int(3)
	else:
		numeroCHROMOSOME_select = int(x)

	

	print("Range de incremento do Chromossomo | ou digite p para deixar como padrão:")
	x = input(">>")
	if x == 'p':
		rangeIncremt_CHROMOSSOME = int(50)
	else:
		rangeIncremt_CHROMOSSOME = int(x)



	
	print("Incremento de tamanho do Chromosome | ou digite p para deixar como padrão:")
	x = input(">>")
	if x == 'p':
		tamanhoIncremet_CHROMOSOME = int(5)
	else:
		tamanhoIncremet_CHROMOSOME = int(x)


	
	
	algen = algGen(gerMAXIMA, tamanhoPOPULACAO,tamanhoCHROMOSOME,numeroCHROMOSOME_select,rangeIncremt_CHROMOSSOME,tamanhoIncremet_CHROMOSOME,tabinlis)
	
	iterations = algen.solution()
	for iteration in iterations:
		print(iteration)
	melhor = algen.melhorSelect
	
	print("______________________________________________________________\n")
	#print(f"Tamanho:",melhor[1].fitness(),"\n")
	print(f"Melehores Chromosomes:\n",algen.getStrChromosome(melhor[0]),"\n")
	print(f"Resultado final:\n",melhor[1])	
 

#Classes  
##############################################################################

#Direção que se move
class Direcao(Enum):
	cima = 1
	direita = 2
	baixo = 3
	esquerda = 4

	def isEqual(self, direction):
		return self == direction

	def isOpposite(self, direction):
		return abs(self.value - direction.value) == 2

	def getOpposite(self):
		return Direcao(self.value - 2) if self.value > 2 else Direcao(self.value + 2)

	def getDifferent(self):
		enums = list(Direcao)
		enums.remove(self)
		return enums[randint(0, 2)]

	def getDifferentAxis(self):
		enums = list(Direcao)
		enums.remove(self)
		enums.remove(self.getOpposite())
		return enums[randint(0, 1)]

#Classe do jogo/ tabuleio
class Jogo:

	def __init__(self, tab):
		self.tabuleiro = np.reshape(tab, (3,3))

	def mover(self, direcao):

		if not isinstance(direcao, Direcao):
			raise TypeError("Direção deve ser um direction Enum!!!")

		x, y = np.where(self.tabuleiro == 0)
		if direcao == Direcao.cima:
			if x == 0:
				raise IndexError("A cordenada x não pode ser negativa!!!")
			self.__swap([x, y], [x-1, y])
		elif direcao == Direcao.direita:
			if y == 2:
				raise IndexError("A cordenada y sai fora do tamanho do tabuleiro!!!")
			self.__swap([x, y], [x, y+1])
		elif direcao == Direcao.baixo:
			if x == 2:
				raise IndexError("A cordenada x sai fora do tamanho do tabuleiro!!!")
			self.__swap([x, y], [x+1, y])
		elif direcao == Direcao.esquerda:
			if y == 0:
				raise IndexError("A cordenada y não pode ser negativa!!!")
			self.__swap([x, y], [x, y-1])

	def __swap(self, cordenada1, cordenada2):
		tmp = self.tabuleiro[cordenada1[0], cordenada1[1]]
		self.tabuleiro[cordenada1[0], cordenada1[1]] = self.tabuleiro[cordenada2[0], cordenada2[1]]
		self.tabuleiro[cordenada2[0], cordenada2[1]] = tmp

	def fitness(self):
		mdis = 0
		for i in range(3):
			for j in range(3):
				if (tabR[i, j] == 0):
					continue
				x, y = np.where(self.tabuleiro == tabR[i, j])
				mdis += abs(x[0]-i) + abs(y[0]-j)
		return mdis

	def __str__(self):
		return str(self.tabuleiro)

#classe Algoritimo Genetico
##############################################################################
class algGen:
	def __init__(self, gerMAXIMA, tamanhoPOPULACAO,tamanhoCHROMOSOME,numeroCHROMOSOME_select,rangeIncremt_CHROMOSSOME,tamanhoIncremet_CHROMOSOME,tab):
		self.tab = tab
		self.gerMAXIMA = gerMAXIMA
		self.tamanhoPOPULACAO = tamanhoPOPULACAO
		self.tamanhoCHROMOSOME = tamanhoCHROMOSOME
		self.numeroCHROMOSOME_select = numeroCHROMOSOME_select
		self.rangeIncremt_CHROMOSSOME = rangeIncremt_CHROMOSSOME
		self.tamanhoIncremet_CHROMOSOME = tamanhoIncremet_CHROMOSOME
		self.melhorSelect = None

	def criaChromosome(self, length=20):
		enums = list(Direcao)
		chromosome = [ enums[randint(0, 3)] for i in range(length) ]
		return chromosome


	def iniPopulation(self):
		population = [ self.criaChromosome(self.tamanhoCHROMOSOME) for i in range(self.tamanhoPOPULACAO) ]
		return population

	#cromossomo (Lista <direção>)
	#Não pode ser movido na mesma direção mais de 3x (Desnecessario)

	def mutacao(self, chromosome):
		length = len(chromosome)

		if (length < 2):
			return chromosome

		if (length < self.tamanhoCHROMOSOME):
			chromosome += self.criaChromosome(self.tamanhoCHROMOSOME-length)

		if (chromosome[0].isOpposite(chromosome[1])):
			chromosome[1] = chromosome[1].getDifferent()

		for i in range(2, length):
			# Mesmo movimento prox. 3x
			if (chromosome[i].isEqual(chromosome[i-2]) and chromosome[i].isEqual(chromosome[i-1])):
				chromosome[i] = chromosome[i-1].getDifferentAxis()
			# Direção contra
			elif(chromosome[i].isOpposite(chromosome[i-1])):
				chromosome[i] = chromosome[i-1].getDifferent()

	#chromosome aplicado no começo do jogo
	# Se uma das direções sai do tabuleiro quando aplicada substitui por outro "eixo"
	def aplicaChromosome(self, chromosome):
		puzzle = Jogo(self.tab)
		i = 0
		while i < len(chromosome):
			try:
				if (puzzle.fitness() == 0):
					return [chromosome[:i], puzzle]
				puzzle.mover(chromosome[i])
				i += 1
			except IndexError:
				chromosome[i] = chromosome[i].getDifferentAxis()
		return [chromosome, puzzle]

	def crossover(self, chromosomes, index=0):
		if (self.numeroCHROMOSOME_select == index+1):
			return
		for i in range(index+1, self.numeroCHROMOSOME_select):
			chromosomes += (self.crossing(chromosomes[index], chromosomes[i]))
		self.crossover(chromosomes, index+1)

	def crossing(self, chromosome1, chromosome2):
		i = randint(0, self.tamanhoCHROMOSOME//2-1)
		j = randint(self.tamanhoCHROMOSOME//2, self.tamanhoCHROMOSOME)

		c1 = chromosome1[:i] + chromosome2[i:]
		c2 = chromosome2[:i] + chromosome1[i:]

		c3 = chromosome1[:j] + chromosome2[j:]
		c4 = chromosome2[:j] + chromosome1[j:]

		c5 = chromosome1[:i] + chromosome2[i:j] + chromosome1[j:]
		c6 = chromosome2[:i] + chromosome1[i:j] + chromosome2[j:]

		c7 = chromosome1[j:] + chromosome1[:i] + chromosome2[i:j]
		c8 = chromosome2[j:] + chromosome2[:i] + chromosome1[i:j]

		c9 = chromosome2[i:j] + chromosome1[:i] + chromosome1[j:]
		c10 = chromosome1[i:j] + chromosome2[:i] + chromosome2[j:]

		return [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

	# Retorna melhores chromosomes
	# return [[Chromosome, Puzzle], ...] 
	def selecao(self, chromosomes):
		res = []
		for chromosome in chromosomes:
			tmp = self.aplicaChromosome(chromosome)
			res.append([tmp[0], tmp[1]])
		# Seleção ranked
		res.sort(key=lambda x: x[1].fitness())
		return res[:self.numeroCHROMOSOME_select]

	def getStrChromosome(self, chromosome):
		return [x.name for x in chromosome]

	def solution(self):
		generation, numOfIncrement, bestmdis = 0, 0, 36
		bestSelection = []

		population = self.iniPopulation()
		while generation < self.gerMAXIMA:

			generation += 1

			# Mutação
			for item in (population):
				self.mutacao(item)

			# Selecao
			slct = self.selecao(population)
			mdis = slct[0][1].fitness()
			population = [item[0] for item in slct]

			# Seleciona melhor
			if (mdis < bestmdis):
				bestmdis = mdis
				bestSelection = slct[0]

			# Incrementa tamanho chromosome 
			if (generation//self.rangeIncremt_CHROMOSSOME > numOfIncrement):
				numOfIncrement += 1
				self.tamanhoCHROMOSOME += self.tamanhoIncremet_CHROMOSOME

			yield f"geração: {generation} | tamaho: {mdis}"

			# Resultado
			if (mdis == 0):
				self.melhorSelect = bestSelection
				break

			self.crossover(population)




#MENU | MAIN
##############################################################################

tabinlis = []

print('*********JOGO DOS 8 COM INTELIGENCIA ARTIFICIAL(ALGORITIMNO GENETICO)*********\n')
print('Digite as peças do tabuleiro 0-8')
print('Não digite peças(numeros) Repitidos')
print('Digite linha por linha do tabuleiro')
#print('Digite numero por numero do tabuleiro, serão dividos depois 3 para cada linha')
print('0 = espaço vago no tabuleiro\n')


#input 1 por 1
#for i in range(9):
 # tab_inicialn.append(int(input(">>")))

#input linha por linha numero separado por espaço
cont = 0
for i in range(3):
  print("Linha",i+1,"digite 3 numeros separdos por espaço")
  x=input(">>")
  y=x.split(sep=" ")
  
  for j in range(3):
    tabinlis.append(int(y[j]))
  
  y.clear
  cont+=3


print("______________________________________________________________\n")
print("O tabuleiro ficou assim!!!\n")
imprimeTab(tabinlis)
print("\n")
print("DIGITE 1 PARA EXECUTAR DE FORMA PADRÃO (BEST)\n")
print("DIGITE 2 PARA EXECUTAR DE FORMA DIDATICA (POPULAÇÃO = 4, CROSSOVER = 70, MAX GERAÇÃO = 20 )")
print("		(Neste metodo o código dá érro se não for capza de executar com no maximo 20 gerações)\n")
print("DIGITE 3 SE DESEJA EXUCUTAR CONTROLANDO ALGUNS ATRIBUTOS DO ALGORITIMO GENETICO\n")

op = int(input('>>'))

if op == 1:

	algen = algGen(1000, 20, 20 ,3 ,50 ,5 ,tabinlis)
	
	iterations =algen.solution()
	for iteration in iterations:
		print(iteration)
	melhor = algen.melhorSelect
	
	print("______________________________________________________________\n")
	#print(f"Tamanho:",melhor[1].fitness(),"\n")
	print(f"Melehores Chromosomes:\n",algen.getStrChromosome(melhor[0]),"\n")
	print(f"Resultado final:\n",melhor[1])
	
if op == 2:

	algen = algGen(20, 4, 20 ,3 ,70 ,5 ,tabinlis)
	
	iterations =algen.solution()
	for iteration in iterations:
		print(iteration)
	melhor = algen.melhorSelect
	
	print("______________________________________________________________\n")
	#print(f"Tamanho:",melhor[1].fitness(),"\n")
	print(f"Melehores Chromosomes:\n",algen.getStrChromosome(melhor[0]),"\n")
	print(f"Resultado final:\n",melhor[1])

if op == 3:
	op3(tabinlis)