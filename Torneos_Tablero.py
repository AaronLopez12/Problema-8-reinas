import numpy as np

def Torneo_con_sustitucion(Matriz_de_entrada, n_individuos):
	"""
	Ingresa de individuos
	retorna una matriz de individuos

	El torneo se hace seleccionando un indiviudo random
	para cada uno de los individuos dentro del ciclo
	Selección con sustitución
	"""

	Matriz_retorno = Matriz_de_entrada.copy()

	for i in range(n_individuos):
		# Numero random de la poblacion
		numero_random = np.random.randint(0, n_individuos)

		if Matriz_de_entrada[i][-1]  < Matriz_de_entrada[numero_random][-1]:
			# Si el F0. Value del i esimo indiviudo es mayor que el 
			# FO Value del random, gana el iesimo individuo
			Matriz_retorno[i] = Matriz_de_entrada[i]

		elif  Matriz_de_entrada[i][-1]  > Matriz_de_entrada[numero_random][-1]:
			# Si el F0. Value del i esimo indiviudo es menor que el 
			# FO Value del random, gana el random de la poblacion
			Matriz_retorno[i] = Matriz_de_entrada[numero_random] 

		else:
			# En el caso de que sean iguales ambos FO Values
			# Se seleccionará uno de ellos de manera alearotia 
			tmp = np.random.uniform()

			if tmp > 0.5: 
				# Gana el de la iteración i
				Matriz_retorno[i] = Matriz_de_entrada[i]
			
			else:
				# Gana el individuo en la posición i de la permitacion
				Matriz_retorno[i] = Matriz_de_entrada[numero_random]
			
	return Matriz_retorno


def Torneo_sin_sustitucion(Matriz_de_entrada, n_individuos):

	"""
	Ingresa de individuos
	retorna una matriz de individuos

	El torneo se hace seleccionando un indiviudo único
	para cada uno de los individuos dentro del ciclo
	Selección sin sustitución: una vez seleccionado deja de estar disponible.
	"""

	Matriz_retorno = Matriz_de_entrada.copy()

	# Creación de una lista para comparar. 
	# Una vez seleccionado el i-esimo individuo deja de estar disponible
	permutacion = np.random.choice(n_individuos, n_individuos, replace = False)
		

	for i in range(n_individuos):
		
		# Comparar individuo iesimo de la poblacion con el iesimo de la permutacion
		
		if Matriz_de_entrada[i][-1] < Matriz_de_entrada[permutacion[i]][-1]:
			# Si FO value del iesimo es mayor que el iesimo FO Value de la lista
			# De permutación  entonces gana el torneo el de la entrada
			Matriz_retorno[i] = Matriz_de_entrada[i]

		elif Matriz_de_entrada[i][-1] > Matriz_de_entrada[permutacion[i]][-1]:
			# Si el FO value de la Entrada es menor que el random de la permutacion
			# Gana el random de la permutacion
			Matriz_retorno[i] = Matriz_de_entrada[permutacion[i]]

		else:
			# En el caso de que sean iguales ambos FO Values
			# Se seleccionará uno de ellos de manera alearotia 
			tmp = np.random.uniform()

			if tmp > 0.5:
				# Gana el de la iteración i
				Matriz_retorno[i] = Matriz_de_entrada[i]
			
			else:
				# Gana el individuo en la posición i de la permitacion
				Matriz_retorno[i] = Matriz_de_entrada[permutacion[i]]

	return Matriz_retorno

