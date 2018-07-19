import copy
import numpy as np

def imagePreprocessing(input):
    row, col = input.shape
    output = np.zeros((row + 2, col + 2))
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            output[i, j] = input[i - 1, j - 1]
    for i in range(row + 2):
        output[i, 0] = output[i, 1]
        output[i, col + 1] = output[i, col]
    for j in range(col + 2):
        output[0, j] = output[1, j]
        output[row + 1, j] = output[row, j]
    return output

def ArithmeticMeanFilter3(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            result[i - 1, j - 1] = (image[i - 1, j - 1] + image[i - 1, j] + image[i - 1, j + 1] + image[i, j - 1] + image[i, j] +\
                image[i, j + 1] + image[i + 1, j - 1] + image[i + 1, j] + image[i + 1, j + 1]) / 9
            result[i - 1, j - 1] = round(result[i - 1, j - 1])
    return result

def GeometricMeanFilter3(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    e = 1 / 9
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            val = (image[i - 1, j - 1] * image[i - 1, j] * image[i - 1, j + 1] * \
                    image[i, j - 1] * image[i, j] * image[i, j + 1] * \
                    image[i + 1, j - 1] * image[i + 1, j] * image[i + 1, j + 1])
            result[i - 1, j - 1] = round(np.power(val, e))
            if result[i - 1, j - 1] > 255:
                result[i - 1, j - 1] = 255
    return result

def HarmonicMeanFilter(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    t = 9
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            val = (1 / image[i - 1, j - 1] + 1 / image[i - 1, j] + 1 / image[i - 1, j + 1] + \
                   1 / image[i, j - 1] + 1 / image[i, j] + 1 / image[i, j + 1] + \
                   1 / image[i + 1, j - 1] + 1 / image[i + 1, j] + 1 / image[i + 1, j + 1])
            result[i - 1, j - 1] = round(t / val)
            if result[i - 1, j - 1] > 255:
                result[i - 1, j - 1] = 255
    return result

def ContraharmonicMeanFilter(originalImage, q):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    q1 = q + 1
    q2 = q
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            val1 = (image[i - 1, j - 1] ** q1 + image[i - 1, j] ** q1 + image[i - 1, j + 1] ** q1 + \
                    image[i, j - 1] ** q1 + image[i, j] ** q1 + image[i, j + 1] ** q1 + \
                    image[i + 1, j - 1] ** q1 + image[i + 1, j] ** q1 + image[i + 1, j + 1] ** q1)
            val2 = (image[i - 1, j - 1] ** q2 + image[i - 1, j] ** q2 + image[i - 1, j + 1] ** q2 + \
                    image[i, j - 1] ** q2 + image[i, j] ** q2 + image[i, j + 1] ** q2 + \
                    image[i + 1, j - 1] ** q2 + image[i + 1, j] ** q2 + image[i + 1, j + 1] ** q2)
            if val2 == 0 and q > 0:
                result[i - 1, j - 1] = 0
            elif val2 == 0 and q < 0:
                result[i - 1, j - 1] = 255
            elif val1 == float('inf') and q > 0:
                result[i - 1, j - 1] = 255
            elif val1 == float('inf') and q < 0:
                result[i - 1, j - 1] = 0
            else:
                result[i - 1, j - 1] = round(val1 / val2)
            if result[i - 1, j - 1] > 255:
                result[i - 1, j - 1] = 255
    return result

def MedianFilter(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            result[i - 1, j - 1] = np.median((image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1], \
                image[i, j - 1], image[i, j], image[i, j + 1], \
                image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1]))
    return result


def MaxFilter(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            result[i - 1, j - 1] = np.max((image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1], \
                image[i, j - 1], image[i, j], image[i, j + 1], \
                image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1]))
    return result


def MinFilter(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            result[i - 1, j - 1] = np.min((image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1], \
                image[i, j - 1], image[i, j], image[i, j + 1], \
                image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1]))
    return result


def ArithmeticMeanFilter5(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    image = imagePreprocessing(image)
    for i in range(2, row + 2):
        for j in range(2, col + 2):
            result[i - 2, j - 2] = (image[i - 2, j - 2] + image[i - 2, j - 1] + image[i - 2, j] + image[i - 2, j + 1] + image[i - 2, j + 2] +\
                                    image[i - 1, j - 2] + image[i - 1, j - 1] + image[i - 1, j] + image[i - 1, j + 1] + image[i - 1, j + 2] +\
                                    image[i, j - 2] + image[i, j - 1] + image[i, j] +image[i, j + 1] + image[i, j + 2] +\
                                    image[i + 1, j - 2] + image[i + 1, j - 1] + image[i + 1, j] + image[i + 1, j + 1] + image[i + 1, j + 2] +\
                                    image[i + 2, j - 2] + image[i + 2, j - 1] + image[i + 2, j] + image[i + 2, j + 1] + image[i + 2, j + 2]) / 25
            result[i - 2, j - 2] = round(result[i - 2, j - 2])
    return result


def GeometricMeanFilter5(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    image = imagePreprocessing(image)
    e = 1 / 25
    for i in range(2, row + 2):
        for j in range(2, col + 2):
            val = (image[i - 2, j - 2] * image[i - 2, j - 1] * image[i - 2, j] * image[i - 2, j + 1] * image[i - 2, j + 2] *\
                   image[i - 1, j - 2] * image[i - 1, j - 1] * image[i - 1, j] * image[i - 1, j + 1] * image[i - 1, j + 2] *\
                   image[i, j - 2] * image[i, j - 1] * image[i, j] * image[i, j + 1] * image[i, j + 2] *\
                   image[i + 1, j - 2] * image[i + 1, j - 1] * image[i + 1, j] * image[i + 1, j + 1] * image[i + 1, j + 2] *\
                   image[i + 2, j - 2] * image[i + 2, j - 1] * image[i + 2, j] * image[i + 2, j + 1] * image[i + 2, j + 2])
            result[i - 2, j - 2] = round(np.power(val, e))
            if result[i - 2, j - 2] > 255:
                result[i - 2, j - 2] = 255
    return result


def MedianFilter5(originalImage):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    image = imagePreprocessing(image)
    for i in range(2, row + 2):
        for j in range(2, col + 2):
            result[i - 2, j - 2] = np.median((\
                image[i - 2, j - 2], image[i - 2, j - 1], image[i - 2, j], image[i - 2, j + 1], image[i - 2, j + 2],\
                image[i - 1, j - 2], image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1], image[i - 1, j + 2],\
                image[i, j - 2], image[i, j - 1], image[i, j], image[i, j + 1], image[i, j + 2],\
                image[i + 1, j - 2], image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1], image[i + 1, j + 2],\
                image[i + 2, j - 2], image[i + 2, j - 1], image[i + 2, j], image[i + 2, j + 1], image[i + 2, j + 2]))
    return result

def AlphaMeanFilter(originalImage, d = 5):
    result = copy.copy(originalImage)
    row, col = originalImage.shape
    image = imagePreprocessing(originalImage)
    image = imagePreprocessing(image)
    for i in range(2, row + 2):
        for j in range(2, col + 2):
            listPix = (\
                image[i - 2, j - 2], image[i - 2, j - 1], image[i - 2, j], image[i - 2, j + 1], image[i - 2, j + 2],\
                image[i - 1, j - 2], image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1], image[i - 1, j + 2],\
                image[i, j - 2], image[i, j - 1], image[i, j], image[i, j + 1], image[i, j + 2],\
                image[i + 1, j - 2], image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1], image[i + 1, j + 2],\
                image[i + 2, j - 2], image[i + 2, j - 1], image[i + 2, j], image[i + 2, j + 1], image[i + 2, j + 2])
            listPix = sorted(listPix)
            listPix = listPix[round(d / 2) : round(d / 2) - d]
            result[i - 2, j - 2] = round(np.mean(listPix))
    return result