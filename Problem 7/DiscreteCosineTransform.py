import numpy as np

zonalMask = [[1, 1, 1, 1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

t = [[16, 11, 10, 16, 24, 40, 51, 61],
     [12, 12, 14, 19, 26, 58, 60, 55],
     [14, 13, 16, 24, 40, 57, 69, 56],
     [14, 17, 22, 29, 51, 87, 80, 62],
     [18, 22, 37, 56, 68, 109, 103, 77],
     [24, 35, 55, 64, 81, 104, 113, 92],
     [49, 64, 78, 87, 103, 121, 120, 101],
     [72, 92, 95, 98, 112, 100, 103, 99]]

def DCT(subImage):
    row , col = subImage.shape
    A = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            c = np.sqrt(1 / 8) if i == 0 else np.sqrt(2 / 8)
            A[i, j] = c * np.cos(np.pi * (j + 0.5) * i / 8)
    res = np.dot(A, subImage)
    res = np.dot(res, A.T)
    return res

def IDCT(subImage):
    row, col = subImage.shape
    A = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            c = np.sqrt(1 / 8) if i == 0 else np.sqrt(2 / 8)
            A[i, j] = c * np.cos(np.pi * (j + 0.5) * i / 8)
    res = np.dot(A.T, subImage)
    res = np.dot(res, A)
    return res

def divideImage(originalImage):
    row, col = originalImage.shape
    row8 = row // 8
    col8 = col // 8
    resList = []
    for i in range(row8):
        for j in range(col8):
            resList.append(originalImage[i * 8 : (i + 1) * 8, j * 8 : (j + 1) * 8])
    return resList

def coefficientDiscard(img, mask, threshold):
    resImg = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            if mask[i][j] > threshold:
                resImg[i, j] = img[i, j]
    return resImg

def imageCompress(orginalImage, method):
    divImg = divideImage(orginalImage)
    DCTImg = []
    for img in divImg:
        DCTSubImg = DCT(img)
        if method == 'zonal mask':
            DiscardImg = coefficientDiscard(DCTSubImg, zonalMask, 0)
            DCTImg.append(DiscardImg)
        elif method == 'threshold mask':
            DiscardImg = coefficientDiscard(DCTSubImg, DCTSubImg / t, 1 / 2 / 255)
            DCTImg.append(DiscardImg)
    return DCTImg

def imageRestore(transformedImg, row, col):
    restoreImg = []
    for img in transformedImg:
        restoreImg.append(np.round(IDCT(img)))
    row8 = row // 8
    col8 = col // 8
    temp = []
    for i in range(row8):
        temp.append(np.column_stack(restoreImg[i * col8 : (i + 1) * col8]))
    res = np.row_stack(temp)
    return res