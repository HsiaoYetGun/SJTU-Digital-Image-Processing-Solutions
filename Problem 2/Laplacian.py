import numpy as np


def calculate(image, x, y):
    return 8 * image[x, y] - (image[x + 1, y] + image[x - 1, y] + image[x, y + 1] + image[x, y - 1] + image[x - 1, y - 1] + \
           image[x - 1, y + 1] + image[x + 1, y - 1] + image[x + 1, y + 1])

def laplace(input, output):
    row, col = output.shape
    for i in range(row):
        for j in range(col):
            output[i, j] = calculate(input, i + 1, j + 1)
            if output[i, j] < 0:
                output[i, j] = 0

def sharp(laplacianImage, originalImage):
    row, col = laplacianImage.shape
    result = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            result[i, j] = originalImage[i, j] + laplacianImage[i, j]
            if result[i, j] > 255:
                result[i, j] = 255
    return result