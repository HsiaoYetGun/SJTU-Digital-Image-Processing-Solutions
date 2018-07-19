import numpy as np

def FFT(originalImage, matrix):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n

    f = np.zeros((q, p), dtype = np.int)
    originalImageMatrix = originalImage.load()
    for x in range(m):
        for y in range(n):
            f[y][x] = originalImageMatrix[x, y] * ((-1) ** (x + y))

    F = np.fft.fft2(f)
    for x in range(p):
        for y in range(q):
            F[y][x] = F[y][x] * matrix[y][x]

    G = np.fft.ifft2(F)

    outputImage = originalImage.copy()
    resultImageMatrix = outputImage.load()
    for x in range(m):
        for y in range(n):
            resultImageMatrix[x, y] = int( G[y][x].real * ((-1) ** (x + y)) )

    resultImage = outputImage
    return resultImage

def idealLowpass(originalImage, radius):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n

    matrix = np.zeros((q, p), dtype = np.int)

    for i in range(q):
        for j in range(p):
            D = ((i - n) ** 2 + (j - m) ** 2) ** 0.5
            if D <= radius:
                matrix[i][j] = 1

    resultImage = FFT(originalImage, matrix)
    return resultImage

def idealHighpass(originalImage, radius):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n
    matrix = np.zeros((q, p), dtype=np.int)

    for i in range(q):
        for j in range(p):
            D = ((i - n) ** 2 + (j - m) ** 2) ** 0.5
            if D > radius:
                matrix[i][j] = 1

    resultImage =  FFT(originalImage, matrix)
    return resultImage

def butterworthLowpass(originalImage, radius, order):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n
    matrix = np.zeros((q, p))

    for i in range(0, q):
        for j in range(0, p):
            D = ((i - n) ** 2 + (j - m) ** 2) ** 0.5
            if radius != 0:
                matrix[i][j] = 1 / (1 + (D / radius) ** (2 * order))
            elif D == 0:
                matrix[i][j] = 1

    resultImage = FFT(originalImage, matrix)
    return resultImage

def butterworthHighpass(originalImage, radius, order):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n
    matrix = np.zeros((q, p))

    for i in range(q):
        for j in range(p):
            D = ((i - n) ** 2 + (j - m) ** 2) ** 0.5
            if D != 0:
                matrix[i][j] = 1 / (1 + (radius / D) ** (2 * order))

    resultImage = FFT(originalImage, matrix)
    return resultImage

def gaussianLowpass(originalImage, radius):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n
    matrix = np.zeros((q, p))

    for i in range(q):
        for j in range(p):
            D = ((i - n) ** 2 + (j - m) ** 2) ** 0.5
            if radius != 0:
                matrix[i][j] = np.exp(-D * D / (2 * radius * radius))
            elif D == 0:
                matrix[i][j] = 1

    resultImage =  FFT(originalImage, matrix)
    return resultImage

def gaussianHighpass(originalImage, radius):

    m, n = originalImage.size
    p = 2 * m
    q = 2 * n
    matrix = np.zeros((q, p))

    for i in range(q):
        for j in range(p):
            D = ((i - n) ** 2 + (j - m) ** 2) ** 0.5
            if radius != 0:
                matrix[i][j] = 1 - np.exp(-D * D / (2 * radius * radius))
            elif D != 0:
                matrix[i][j] = 1

    resultImage =  FFT(originalImage, matrix)
    return resultImage