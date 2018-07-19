import numpy as np

def product(image1, image2):
    row, col = image1.shape
    result = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            result[i, j] = image1[i, j] * image2[i, j] / 255
    return result

def sum(image1, image2):
    row, col = image1.shape
    result = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            result[i, j] = image1[i, j] + image2[i, j]
    return result

def powerLawTransformation(image, c = 1, gamma = 0.5):
    row, col = image.shape
    result = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            result[i, j] = c * np.power(image[i, j], 0.5)
    return result