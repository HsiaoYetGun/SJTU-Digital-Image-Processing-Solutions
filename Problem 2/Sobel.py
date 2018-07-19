import numpy as np

def SobelOperators(preprocessImage, mode = 'abs'):
    row, col = preprocessImage.shape
    result = np.zeros((row - 2, col - 2))
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            gx = preprocessImage[i + 1, j - 1] + 2 * preprocessImage[i + 1, j] + preprocessImage[i + 1, j + 1] - \
                preprocessImage[i - 1, j - 1] - 2 * preprocessImage[i - 1, j] - preprocessImage[i - 1, j + 1]
            gy = preprocessImage[i - 1, j + 1] + 2 * preprocessImage[i, j + 1] + preprocessImage[i + 1, j + 1] - \
                preprocessImage[i - 1, j - 1] - 2 * preprocessImage[i, j - 1] - preprocessImage[i + 1, j - 1]
            if(mode == 'square-root'):
                result[i - 1, j - 1] = np.sqrt(np.power(gx, 2) + np.power(gy, 2))
            elif(mode == 'abs'):
                result[i - 1, j - 1] = np.abs(gx) + np.abs(gy)
    return  result