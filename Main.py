import numpy as np
import os
from Poblacion import pob_0
from Evaluar_Poblacion_Tablero import evaluacion_poblacion
from Diagonales_Tablero import diagonales_tablero
from Torneos_Tablero import Torneo_con_sustitucion
from Cruce_Multipunto_Tablero import Cruce_multipuntos
from Mutacion_Tablero import mutacion
from Union_Poblaciones import Seleccion
from Mejor_Solucion import mejor_solucion
from Grafica import graph_indef
from Grafica import graph_fija

N = 200
iteraciones = 1000
pm = 0.4
experimentos = 1
Errores = 0

for l in range(experimentos):
	
	Poblacion_inicial= pob_0(N)

	for k in range(iteraciones):

		Poblacion_ciclo = Poblacion_inicial.copy()
		
		################################# Primera Evaluacion ################
		for j in Poblacion_ciclo:
			j[-1] = 0

		for i in range(len(Poblacion_ciclo)):
			Poblacion_ciclo[i] = evaluacion_poblacion(Poblacion_ciclo[i])


		################### Seleccion: Torneo con sustitucion ################
		Poblacion_ciclo = Torneo_con_sustitucion(Poblacion_ciclo, N)

		
		############################## Cruzamiento multipunto ################
		for ii in range(0, (len(Poblacion_ciclo)//2) + 1,2):
			Poblacion_ciclo[ii], Poblacion_ciclo[ii+1] = Cruce_multipuntos(
				Poblacion_ciclo[ii], Poblacion_ciclo[ii+1], 4, 8)


		################ Mutacion de los individuos de la población ###########
		for iii in range(len(Poblacion_inicial)):
			Poblacion_ciclo[iii] = mutacion(pm, Poblacion_ciclo[iii])


		######################### Segunda Evaluacion ################################
		for j in Poblacion_ciclo:
			j[-1] = 0

		for iiii in range(len(Poblacion_ciclo)):
			Poblacion_ciclo[iiii] = evaluacion_poblacion(Poblacion_ciclo[iiii])

		################################# Union ################################
		Poblacion_ciclo = Seleccion(Poblacion_ciclo, Poblacion_inicial)
		Poblacion_inicial = Poblacion_ciclo.copy()
		
		mejor = mejor_solucion(Poblacion_inicial)
		
		#graph_indef(mejor[0])

		#if mejor[0][-1] == 0:
			#graph_fija(mejor[0])

	if mejor[0][-1] != 0.0:
		Errores += 1

print(mejor[0])


print("###########################################")
print("De un total de: ",  experimentos, " experimentos")
print("Cada uno de ellos con: ", iteraciones, " iteraciones")
print("Y una población conformada por: ", N)
print("Utilizando una Probabilidad de mutación de: ", pm )
print("Se obtuvo la siguiente precisión: ", 1 - (Errores / experimentos))
print("###########################################")

