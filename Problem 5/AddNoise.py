import numpy as np

def addGaussianNoise(originalImageFFT, mean, variance):
    row, col = originalImageFFT.shape
    standardDeviation = variance ** 0.5
    gaussianNoise = np.random.normal(mean, standardDeviation, (row, col))
    gaussianNoise = gaussianNoise.reshape(row, col)
    return gaussianNoise