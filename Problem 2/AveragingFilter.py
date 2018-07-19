import numpy as np

def getMean(input, a, b, x, y):
    dx = x / 2
    dy = y / 2
    list = []
    for i in range(a - dx, a + dx + 1):
        for j in range(b - dy, b + dy + 1):
            list.append(input[i, j])
    return int(np.mean(list))

def averagingFilter(input, x, y):
    row, col = input.shape
    result = np.zeros((row - 4, col - 4))
    for i in range(2, row - 2):
        for j in range(2, col - 2):
            result[i - 2, j - 2] = getMean(input, i, j, x, y)
    return result