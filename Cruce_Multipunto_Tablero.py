import numpy as np

def Cruce_multipuntos(padre_1, padre_2, n_puntos, elementos_a_cruzar):

	"""
	Parametros: dos padres que se cruzarán tantas veces como n_puntos
	
	"""
	
	# Creacion de los lugares de corte
	sitios_corte = np.sort(np.random.choice(range(1, elementos_a_cruzar), n_puntos, replace = False))
	
	# Creacion de la lista para almacenar los lugares de corte
	parejas = []

	# Listas de retorno
	vector1_cruzado = []
	vector2_cruzado = []

	# Iteración sobre la longitud de los sitios de corte
	for i in range(len(sitios_corte)):
		
		if i != 0:
			# intervalos distintos del origen
			parejas.append((sitios_corte[i-1],sitios_corte[i]))

		else:
			# Primer intervalo
			parejas.append((0,sitios_corte[i]))

	#último intervalo
	parejas.append((sitios_corte[-1], elementos_a_cruzar))
	
	# Cruzamiento con ayuda de los sitios de corte
	# con ayuda del indice j para la seleccion del tipo de cruce
	for j,jj in enumerate(zip(parejas)):
		
		if j % 2 == 1:
			vector1_cruzado[jj[0][0]: jj[0][1]] = padre_1[jj[0][0]: jj[0][1]]
			vector2_cruzado[jj[0][0]: jj[0][1]] = padre_2[jj[0][0]: jj[0][1]]
		
		else: 
			vector1_cruzado[jj[0][0]: jj[0][1]] = padre_2[jj[0][0]: jj[0][1]]
			vector2_cruzado[jj[0][0]: jj[0][1]] = padre_1[jj[0][0]: jj[0][1]]

	# Agregar la FO a cada pareja igualada a 0
	vector1_cruzado.append(0)
	vector2_cruzado.append(0)
	return vector1_cruzado, vector2_cruzado