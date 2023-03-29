import numpy as np

A = [(i,j) for i in range (8) for j in range (8)]

def pob_0(N):
    """
    Funcion que realiza una matriz de poblacion N de la siguiente forma

    [[(x1,y1),...,(x8,y8), F0]
    [(x1,y1),...,(x8,y8), F0]
    [(x1,y1),...,(x8,y8), F0]
    ...
    [(x1,y1),...,(x8,y8), F0]
    ]
    """
    
    padres = []
    for i in range(N):
        indices=np.random.choice(range(64),8, replace = False )
        padres.append([A[indices[0]], A[indices[1]],A[indices[2]], A[indices[3]], A[indices[4]], A[indices[5]],A[indices[6]], A[indices[7]], 0])
    return padres