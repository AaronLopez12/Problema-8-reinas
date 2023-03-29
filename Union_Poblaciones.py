import numpy as np


def Seleccion(Matriz_Padres, Matriz_Hijos):
	"""
	Ingresan dos matrices de poblaciones: Padres e Hijos.
	Retorna una matriz con los mejores individuos de cada poblacion
	"""

	Poblacion_retorno = []
	for i in range(len(Matriz_Padres)):
		Poblacion_retorno.append([])

	#Listas auxiliares para almacenamiento de los elementos de FO
	lista_temporal_padres = []
	lista_temporal_hijos  = []

	# Agregar el FO según corresponda
	for i in Matriz_Padres:
		lista_temporal_padres.append(i[-1])

	for i in Matriz_Hijos:
		lista_temporal_hijos.append(i[-1])
	
	# Orden de las listas de menor a mayor
	lista_ordenadas_padres = np.sort(np.array(lista_temporal_padres)) # Orden de las F.O. padres
	lista_ordenadas_hijos  = np.sort(np.array(lista_temporal_hijos)) # Orden de las F.0. Hijos
	
	for i in range(int(len(lista_temporal_hijos)/2)):
		# Iterar sobre los n/2 elementos de las listas 
		# Encontrar el indice acorde a los mayores valores de la poblacion		
		Indice_padre = np.where(np.array(lista_temporal_padres) == lista_ordenadas_padres[i])
		Indice_hijo  = np.where(np.array(lista_temporal_hijos)  == lista_ordenadas_hijos[i])

		# Asignación de los individuos en la nueva población
		Poblacion_retorno[2*i] = Matriz_Padres[Indice_padre[0][0]]
		Poblacion_retorno[2*(i+1)-1] = Matriz_Hijos[Indice_hijo[0][0]]
	return Poblacion_retorno
