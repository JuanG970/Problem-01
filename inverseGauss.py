#import numpy as np
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
        for i in range(j - 1, -1, -1):
            factor = augmentedMatrix[i, j]
            if factor == 0:
                continue
            augmentedMatrix[i] = augmentedMatrix[j] + augmentedMatrix[i]*pivot/(-factor)
        augmentedMatrix[j] = augmentedMatrix[j]/augmentedMatrix[j,j]
    return augmentedMatrix[:,n:]

#matrixToSolve =  np.matrix([[2,3,4], [1,1,1], [2,1,1]])
#print(inverseUsingGauss(matrixToSolve))