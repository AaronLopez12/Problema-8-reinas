import matplotlib.pyplot as plt
import numpy as np

def graph_indef(vector):

	"""
	Vector de la forma [(x1,y1),...,(x8,y8),F]
	
	"""
	Matrix = np.zeros((8,8))

	for i in range(len(vector)-1):
		x = vector[i][0]
		y = vector[i][1]
		
		Matrix[x,y] = 1
	
	plt.title("Posición de las reinas")
	plt.xlabel("Posición X")
	plt.ylabel("Posición Y")
	plt.imshow(Matrix, cmap='gray')
	plt.pause(0.5)
	plt.close()	

def graph_fija(vector):

	"""
	Vector de la forma [(x1,y1),...,(x8,y8),F]
	
	"""
	Matrix = np.zeros((8,8))

	for i in range(len(vector)-1):
		x = vector[i][0]
		y = vector[i][1]
		
		Matrix[x,y] = 1
	
	plt.title("Posición de las reinas")
	plt.xlabel("Posición X")
	plt.ylabel("Posición Y")
	plt.imshow(Matrix, cmap='gray')
	plt.show()