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

def solveUssingIterative(a, b, relaxation = 1, maxIterations = 100, TOL = 0.0001):
    b = np.matmul(a.T, b)
    a = np.matmul(a.T, a)
    rows = np.shape(a)[0]
    x0 = np.ones(rows)
    d = relaxation*np.diag(a)
    errorNorm = 100
    currentIteration = 0
    while errorNorm > TOL and currentIteration < maxIterations:
        for _ in range(30):
            x1 = x0 + (b - np.matmul(a, x0))/d
            errorNorm = (x0 - x1)/x1
            errorNorm = np.linalg.norm(errorNorm)
            x0 = x1
            currentIteration += 1
    if errorNorm > TOL and currentIteration > maxIterations:
        print("The algorithm not converged, try setting more iterations, lowering error or incressing relaxation parameter")
        return none
    return x1

# A = np.array([[1, -1, 0, 3], [2, 1, 2, 1], [2, -3, -2, 0], [0, 3, -2, 4]])
# B = np.array([8 ,11, -8, 14])
# print(solveUssingIterative(A, B))