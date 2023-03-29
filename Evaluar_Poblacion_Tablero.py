import numpy as np
from Diagonales_Tablero import diagonales_tablero

def evaluacion_poblacion(vector):

	"""
	Vector de ingreso de la forma: [tupla_1, ..., tupla8, F = 0]
	Vector de retorno de la forma: [tupla_1, ..., tupla8, F]
	"""
	
	### Calculo ataques en filas y columnas
	for i in range(len(vector)-1):

		x = vector[i][0]
		y = vector[i][1]

		for j in range(len(vector)-1):

			if i != j :

				if x == vector[j][0]: 
					vector[-1] += 0.5	

				elif y == vector[j][1]: 
					vector[-1] += 0.5	
	
		# Calculo ataques en Diagonales
		Diagonal = diagonales_tablero((x,y), 8) 

		# Creacion de temporal para las pos. de las reinas
		conjunto_temporal = vector[0:len(vector)] 

		# Eliminar la reina de la iteracion i 
		del conjunto_temporal[i]

		# Interseccion de elem. diagonal y posiciones de reinas
		conjunto_temporal = set(conjunto_temporal)
		z = Diagonal.intersection(conjunto_temporal)

		# Suma de ataques entre reinas
		vector[-1] += len(z) / 2

	if len(vector[:-1]) != len(set(vector[:-1])):
		vector[-1] = 50
	
	return vector 
