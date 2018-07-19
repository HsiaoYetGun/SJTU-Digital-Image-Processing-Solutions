import numpy as np
from PIL import Image

def principalComponentsTransform(originalImageSet):
    m, n = originalImageSet[0].size
    size = m * n
    vectors = np.zeros((size, 6))
    pixList = []
    for i in range(6):
        t = originalImageSet[i].load()
        pixList.append(t)
    ctr = 0
    for i in range(m):
        for j in range(n):
            for k in range(6):
                vectors[ctr, k] = pixList[k][i, j]
            ctr += 1

    mx = np.zeros((1, 6))
    for i in range(size):
        mx += vectors[i, :]
    mx = mx.T / (m * n)

    cx = np.zeros((6, 6))
    for i in range(size):
        cx += np.dot(vectors[i, :].T, vectors[i, :])
    cx /= size
    cx -= np.dot(mx, mx.T)
    eigenValue, eigenVector = np.linalg.eig(cx)
    vectorLen = len(eigenVector)
    eigenVectorT = eigenVector.copy()
    for i in range(vectorLen - 1, -1, -1):
        temp = eigenVector[i]
        eigenVectorT[vectorLen - 1 - i] = temp
    PCs = 2
    vectorMetas = np.zeros((size, PCs))
    for i in range(size):
        mxList = []
        for j in range(6):
            mxList.append(vectors[i, j].T - mx[j])
        vectorMetas[i, :] = (np.dot(eigenVectorT[0 : PCs, :], mxList)).T

    vectorReconstructs = np.zeros((size, 6))
    for i in range(size):
        mxList = np.dot(eigenVectorT[0 : PCs, :].T, vectorMetas[i, :].T)
        for j in range(6):
            mxList[j] += mx[j]
        vectorReconstructs[i, :] = mxList.T

    reconstructsImageSet = []
    for i in range(6):
        temp = np.zeros((m, n))
        reconstructsImageSet.append(temp)
    ctr = 0
    for i in range(m):
        for j in range(n):
            for k in range(6):
                reconstructsImageSet[k][j, i] = vectorReconstructs[ctr, k]
            ctr += 1

    return reconstructsImageSet