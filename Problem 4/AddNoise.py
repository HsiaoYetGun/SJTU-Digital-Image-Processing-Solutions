import numpy as np
import random

def addNoisy(noiseType, originalImage, mean = 0, variance = 400, prob = 0.1):
    row, col= originalImage.shape
    noisyImage = np.zeros(originalImage.shape)
    if noiseType == "Uniform":
        std = variance ** 0.5
        uniformNoise = np.random.normal(mean, std, (row, col))
        uniformNoise = uniformNoise.reshape(row, col)
        noisyImage = originalImage + uniformNoise
        for i in range(row):
            for j in range(col):
                noisyImage[i, j] = round(noisyImage[i, j])
                if noisyImage[i, j] < 0:
                    noisyImage[i, j] = 0
                if noisyImage[i, j] > 255:
                    noisyImage[i, j] = 255

    elif noiseType == "Gaussian":
        std = variance ** 0.5
        gaussianNoise = np.random.normal(mean, std, (row, col))
        gaussianNoise = gaussianNoise.reshape(row, col)
        noisyImage = originalImage + gaussianNoise
        for i in range(row):
            for j in range(col):
                noisyImage[i, j] = round(noisyImage[i, j])
                if noisyImage[i, j] < 0:
                    noisyImage[i, j] = 0
                if noisyImage[i, j] > 255:
                    noisyImage[i, j] = 255

    elif noiseType == "Salt":
        for i in range(row):
            for j in range(col):
                rdn = random.random()
                if rdn < prob:
                    noisyImage[i, j] = 255
                else:
                    noisyImage[i, j] = originalImage[i, j]

    elif noiseType == "Pepper":
        for i in range(row):
            for j in range(col):
                rdn = random.random()
                if rdn > 1 - prob:
                    noisyImage[i, j] = 0
                else:
                    noisyImage[i, j] = originalImage[i, j]
    return noisyImage