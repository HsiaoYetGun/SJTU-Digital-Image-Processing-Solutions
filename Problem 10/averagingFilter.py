import numpy as np

def imagePreprocess(input):
    row, col = input.shape
    output = np.zeros((row + 2, col + 2))
    for i in range(row):
        output[i, 0] = input[i, 0]
        output[i, col] = input[i, col - 1]
        for j in range(col):
            output[i + 1, j + 1] = input[i, j]
    for j in range(col):
        output[0, j] = input[0, j]
        output[row, j] = input[row - 1, j]
    return output

def getMean(input, a, b, l):
    d = int(l / 2)
    list = []
    for i in range(a - d, a + d + 1):
        for j in range(b - d, b + d + 1):
            list.append(input[i, j])
    return int(np.mean(list))

def averagingFilter(input, l):
    d = l - 1
    for i in range(d):
        input = imagePreprocess(input)
    row, col = input.shape
    result = np.zeros((row - 2 * d, col - 2 * d))
    for i in range(d, row - d):
        for j in range(d, col - d):
            result[i - d, j - d] = getMean(input, i, j, l)
    return result