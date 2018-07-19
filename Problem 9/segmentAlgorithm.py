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

def upperShift(originalImage):
    U = np.zeros(originalImage.shape)
    U[: U.shape[0] - 1, :] = originalImage[1 : originalImage.shape[0], :]
    U[U.shape[0] - 1, :] = U[U.shape[0] - 2, :]
    return U

def downShift(originalImage):
    D = np.zeros(originalImage.shape)
    D[1 :, :] = originalImage[: originalImage.shape[0] - 1, :]
    D[0, :] = D[1, :]
    return D

def leftShift(originalImage):
    L = np.zeros(originalImage.shape)
    L[:, : L.shape[1] - 1] = originalImage[:, 1 : originalImage.shape[1]]
    L[:, L.shape[1] - 1] = L[:, L.shape[1] - 2]
    return L

def rightShift(originalImage):
    R = np.zeros(originalImage.shape)
    R[:, 1 :] = originalImage[:, : originalImage.shape[1] - 1]
    R[:, 0] = R[:, 1]
    return R

def Roberts(originalImage):
    U = upperShift(originalImage)
    L = leftShift(originalImage)
    UL = leftShift(U)

    gx = np.abs(UL - originalImage)
    gy = np.abs(U - L)
    M = gx + gy

    return gx, gy, M

def Prewitt(originalImage):
    U = upperShift(originalImage)
    D = downShift(originalImage)
    L = leftShift(originalImage)
    R = rightShift(originalImage)

    UL = leftShift(U)
    UR = rightShift(U)
    DL = leftShift(D)
    DR = rightShift(D)

    gx = np.abs(UR + U + UL - DR - D - DL)
    gy = np.abs(DL + L + UL - DR - R - UR)
    M = gx + gy

    return gx, gy, M

def Sobel(originalImage):
    U = upperShift(originalImage)
    D = downShift(originalImage)
    L = leftShift(originalImage)
    R = rightShift(originalImage)

    UL = leftShift(U)
    UR = rightShift(U)
    DL = leftShift(D)
    DR = rightShift(D)

    gx = np.abs(UR + 2 * U + UL - DR - 2 * D - DL)
    gy = np.abs(DL + 2 * L + UL - DR - 2 * R - UR)
    M = gx + gy

    return gx, gy, M