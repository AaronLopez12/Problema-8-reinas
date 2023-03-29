import numpy as np

def diagonales_tablero(posicion_tablero, tamaño_tablero):
	"""
	Ingresa una posicion de un tablero cuya indexación empieza en cero
	tamaño_tablero = número de celdas del tablero cuadrado

	Retorna un conjunto de posiciones que son las diagonales de dicha posicion

	"""
	posicion_tablero = (posicion_tablero[0], posicion_tablero[1])
	Lista_diagonales_tablero = []
	
	for i in range(tamaño_tablero):

		# Creando posiciones sobre la diagonal alejandose del punto de origen
		
		x_1 = posicion_tablero[0] + i
		y_1 = posicion_tablero[1] + i
		
		x_2 = posicion_tablero[0] + i
		y_2 = posicion_tablero[1] - i
		
		x_3 = posicion_tablero[0] - i
		y_3 = posicion_tablero[1] + i
		
		x_4 = posicion_tablero[0] - i
		y_4 = posicion_tablero[1] - i

		# Si la posicion creada se sale del tablero, no se agrega a la lista
		if (x_1 >= 0 and x_1 <= 7 ) and (y_1 >= 0 and y_1 <= 7):
			Lista_diagonales_tablero.append((x_1, y_1))
		
		if (x_2 >= 0 and x_2 <= 7 ) and (y_2 >= 0 and y_2 <= 7):
			Lista_diagonales_tablero.append((x_2, y_2))
		
		if (x_3 >= 0 and x_3 <= 7 ) and (y_3 >= 0 and y_3 <= 7):
			Lista_diagonales_tablero.append((x_3, y_3))
		
		if (x_4 >= 0 and x_4 <= 7 ) and (y_4 >= 0 and y_4 <= 7):
			Lista_diagonales_tablero.append((x_4, y_4))

	# Eliminar las redundancias
	diagonales_tablero = set(Lista_diagonales_tablero)
	diagonales_tablero.discard(posicion_tablero)

	return diagonales_tablero