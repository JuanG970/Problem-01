import numpy as np

def inverseUsingGauss(*a):
    a = np.matrix(a[0])
    dimensions = np.shape(a)
    nCol = dimensions[1]
    nRows = dimensions[0]
    
    if nRows != nCol:
        print("Matrix is not square, this algorithm does not work! :(")
        return None
    if np.linalg.det(a) == 0:
        print("The matrix is singular, the alforithm dows not work! :(")
        return None
    n = nCol
    iMatrix = np.eye(n) #The identity matrix to append
    augmentedMatrix = np.c_[a, iMatrix]
    print(augmentedMatrix)
    #Gauss: Generate an upper triangular matrix
    for j in range(n - 1):
        pivot = augmentedMatrix[j, j]
        for i in range(n - 1 -  j):
            factor = augmentedMatrix[i+1+j, j]
            if factor == 0:
                continue
            augmentedMatrix[i + 1 + j] = augmentedMatrix[j] + augmentedMatrix[i + 1 + j] * pivot/(-factor) 
    #Gauss-Jordan: Generates the inverse 
    for j in range(n - 1, -1, -1):
        pivot = augmentedMatrix[j,j]
        for i in range(j, -1, -1):
            factor = augmentedMatrix[i, j]
            if factor == 0:
                continue
            augmentedMatrix[i-1] = augmentedMatrix[i-1] + augmentedMatrix[j]*pivot/(-factor)
    print(augmentedMatrix)




matrixToSolve =  np.matrix([[1, -1, 0, 3], [2, 1, 2, 1], [2, -3, -2, 0], [0, 3, -2, 4]])

print(inverseUsingGauss(matrixToSolve))