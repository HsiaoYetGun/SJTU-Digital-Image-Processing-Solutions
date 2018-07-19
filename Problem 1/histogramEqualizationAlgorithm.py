import numpy as np

def histogramProcessing(originalImage):
    m, n =  originalImage.shape
    size = m * n
    sum = 0
    image = originalImage.copy()
    grayCount = np.zeros(256, dtype = int)
    histogramEqualization = {}

    for i in range(m):
        for j in range(n):
            grayCount[originalImage[i][j]] += 1

    grayCDF = dict((i, grayCount[i]) for i in range(256) if grayCount[i] != 0)

    for key in range(256):
        if key in grayCDF.keys():
            grayCDF[key] += sum
            sum = grayCDF[key]

    minGray = min(grayCDF.values())

    for key in grayCDF.keys():
        histogramEqualization[key] = grayCDF[key] * 1.0 / size
        grayCDF[key] = transformFunction(grayCDF[key], minGray, size)

    for i in range(m):
        for j in range(n):
            image[i][j] = grayCDF[image[i][j]]

    return image, histogramEqualization, grayCDF

def transformFunction(pixelCDF, minGray, size):
    return round(1.0 * (pixelCDF - minGray) / (size - minGray) * 255)