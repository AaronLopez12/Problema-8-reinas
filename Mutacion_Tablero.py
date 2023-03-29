import numpy as np

def mutacion(probabilidad_mutar, vec):
	"""
	Funcion para mutar a un vector de tuplas de la forma:
	vec = [(x1,y1)...(xn,yn),F] cambiando una o más de sus 
	tuplas por otros valores siempre que no estén en el arreglo

	probabilidad_mutar: constante entre [0,1], entre menor sea menos
	probabilidad hay de que las tuplas muten

	"""

	vector = vec.copy() # copia del vector de entrada
	
	# mascara de las tuplas con prob. c/u entre [0,1]
	mascara = np.random.uniform(size = len(vector)) 

	# Indices que tienen probabilidad mayor al parametro
	# Si cumplen la condicion, será mutada la tupla
	indices = np.where(mascara >= (1-probabilidad_mutar))[0]
	
	# Iteracion sobre los elementos a iterar
	for i in range(len(indices)-1):
		
		# Listas auxiliares para las ordenadas X e Y
		tmp_list1 = [x for x in range(0,8)]
		tmp_list2 = [x for x in range(0,8)]
		
		# Se elimina el elemento de la tupla original
		# para tener diversidad
		tmp_list1.remove(vector[indices[i]][0])
		tmp_list2.remove(vector[indices[i]][1])

		# Asignación de la tupla en el lugar antiguo
		vector[indices[i]] = (np.random.choice(tmp_list1), 
			                  np.random.choice(tmp_list2))
		
		# Si la tupla nueva se repite, se repite el proceso
		#if vec[indices[i]] in vec:
		#	return vec
	
	# retorno del vector auxiliar
	return vector
