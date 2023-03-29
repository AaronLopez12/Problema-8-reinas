import numpy as np

def mejor_solucion(Poblacion):
	# Listas auxiliares
	individuo = []
	lista_temporal  = []

	# Obtencion de los F.O. de cada individuo
	for i in Poblacion:
		lista_temporal.append(i[-1])

	# Orden de las F.O. padres
	lista_ordenadas = np.sort(np.array(lista_temporal))

	# Preguntar por la posicion del menor resultado de la poblacion
	Indice = np.where(np.array(lista_temporal) == lista_ordenadas[0])

	# Apendizar el individuo de  menor F0
	individuo.append(Poblacion[Indice[0][0]])
	return individuo

