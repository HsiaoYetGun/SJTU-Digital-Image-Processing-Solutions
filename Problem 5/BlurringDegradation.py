import numpy as np

def functionH(u, v, a = 0.1, b = 0.1, T = 1):
    temp = np.pi * (u * a + v * b)
    if temp == 0:
        return 1
    res = T * np.sin(temp) * np.exp(np.complex(0, -temp)) / temp
    return res

def getBlurringDegradationFunction(originalImage):
    row, col = originalImage.shape
    degradationFunction = np.zeros((row, col), dtype = np.complex)
    for i in range(row):
        for j in range(col):
            degradationFunction[i, j] = functionH(i - row / 2, j - col / 2)
    return degradationFunction