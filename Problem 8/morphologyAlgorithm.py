import numpy as np

def erosionOperate(originalImage, B):
    m, n = originalImage.size
    erosionImage = originalImage.copy()
    a, b = B.shape
    x2 = int(b / 2)
    y2 = int(a / 2)

    inputPixMatrix = originalImage.load()
    outputPixMatrix = erosionImage.load()

    for x in range(m):
        for y in range(n):
            if inputPixMatrix[x, y] != 0:
                flag = False
                for i in range(-x2, x2 + 1):
                    for j in range(-y2, y2 + 1):
                        if x + i < 0 or x + i >= m or y + j < 0 or y + j >= n:
                            flag = True
                            break
                        if B[j + y2][i + x2] == 1 and inputPixMatrix[x + i, y + j] == 0:
                                flag = True
                                break
                    if flag == True:
                        outputPixMatrix[x, y] = 0
                        break

    return erosionImage

def dilationOperate(originalImage, B):
    m, n = originalImage.size
    dilationImage = originalImage.copy()
    a, b = B.shape
    x2 = int(b / 2)
    y2 = int(a / 2)

    inputPixMatrix = originalImage.load()
    outputPixMatrix = dilationImage.load()

    for x in range(m):
        for y in range(n):
            if inputPixMatrix[x, y] == 0:
                flag = False
                for i in range(-x2, x2 + 1):
                    for j in range(-y2, y2 + 1):
                        if x + i < 0 or x + i >= m or y + j < 0 or y + j >= n:
                            continue
                        if B[j + y2][i + x2] == 1 and inputPixMatrix[x + i, y + j] != 0:
                            flag = True
                            break
                    if flag == True:
                        outputPixMatrix[x, y] = 255
                        break

    return dilationImage

def reconstructionOperate(originalImage, erosionImage, B):
    m, n = erosionImage.size
    reconstructionImage = erosionImage.copy()

    erosionPixs = erosionImage.load()
    originalPixs = originalImage.load()
    outputPixMatrix = reconstructionImage.load()

    a, b = B.shape
    x2 = int(b / 2)
    y2 = int(a / 2)

    while 1:
        flag1 = True
        for x in range(m):
            for y in range(n):
                if originalPixs[x, y] == 0:
                    if erosionPixs[x, y] != 0:
                        flag1 = False
                    outputPixMatrix[x, y] = 0
                    continue
                if erosionPixs[x, y] == 0:
                    flag2 = False
                    for i in range(-x2, x2 + 1):
                        for j in range(-y2, y2 + 1):
                            if x + i < 0 or x + i >= m or y + j < 0 or y + j >= n:
                                continue
                            if B[j + y2][i + x2] == 1 and erosionPixs[x + i, y + j] != 0:
                                flag2 = True
                                break
                        if flag2 == True:
                            outputPixMatrix[x, y] = 255
                            flag1 = False
                            break
        if flag1 == True:
            break
        erosionImage = reconstructionImage.copy()
        erosionPixs = erosionImage.load()

    return reconstructionImage

def borderClearing(originalImage, B):
    m, n = originalImage.size
    markImage = originalImage.copy()
    borderClearingImage = originalImage.copy()

    originalPixs = originalImage.load()
    borderClearingPixs = borderClearingImage.load()
    markPixs = markImage.load()

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                markPixs[i, j] = originalPixs[i, j]
            else:
                markPixs[i, j] = 0

    borderImage = reconstructionOperate(originalImage, markImage, B)
    borderPixs = borderImage.load()
    for i in range(m):
        for j in range(n):
            borderClearingPixs[i, j] = borderClearingPixs[i, j] - borderPixs[i, j]

    return markImage, borderClearingImage

def complementOperate(originalImage):
    complementImage = originalImage.copy()
    complementPixs = complementImage.load()

    m, n = complementImage.size
    for i in range(m):
        for j in range(n):
            complementPixs[i, j] = 255 - complementPixs[i, j]

    return complementImage

def holeFillingOperate(originalImage, B):
    m, n = originalImage.size
    markImage = originalImage.copy()
    maskImage = originalImage.copy()

    inputPixMatrix = originalImage.load()
    markPixs = markImage.load()
    maskPixs = maskImage.load()

    for x in range(m):
        for y in range(n):
            if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                markPixs[x, y] = 255 - inputPixMatrix[x, y]
            else:
                markPixs[x, y] = 0
            maskPixs[x, y] = 255 - inputPixMatrix[x, y]

    fillingHolesImage = reconstructionOperate(maskImage, markImage, B)
    outputPixMatrix = fillingHolesImage.load()

    for x in range(m):
        for y in range(n):
            outputPixMatrix[x, y] = 255 - outputPixMatrix[x, y]

    return markImage, fillingHolesImage