import numpy as np

def getStartPoint(originalImage, s1, s2):
    m, n = originalImage.shape
    for i in range(s1, m):
        for j in range(s2, n):
            if originalImage[i, j] == 255:
                x = i
                y = j
                return x, y

def getNextPoint(originalImage, bx_i, by_i, cx_i, cy_i):
    dx = [0, -1, -1, -1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, -1, -1, 0, 1]
    bx = bx_i
    by = by_i
    cx = cx_i
    cy = cy_i
    m, n = originalImage.shape
    for i in range(8):
        if bx + dx[i] == cx and by + dy[i] == cy:
            for j in range(i + 1, i + 8):
                tx = bx + dx[j]
                ty = by + dy[j]
                if tx >= 0 and tx < m and ty >= 0 and ty < n:
                    if originalImage[tx, ty] == 255:
                        bx = tx
                        by = ty
                        di = j
                        if di >= 8:
                            di -= 8
                        break
                cx = tx
                cy = ty
            break
    return bx, by, cx, cy, di

def boundaryFollowing(originalImage):
    m, n = originalImage.shape
    boundaryImage = np.zeros((m, n))

    startX, startY = getStartPoint(originalImage, 110, 220)
    bx = startX
    by = startY
    cx = startX
    cy = startY - 1
    b1x, b1y, c1x, c1y, discard = getNextPoint(originalImage, bx, by, cx, cy)

    while(1):
        boundaryImage[bx, by] = 255
        bx, by, cx, cy, discard = getNextPoint(originalImage, bx, by, cx, cy)
        if bx == startX and by == startY:
            b2x, b2y, c2x, c2y, discard = getNextPoint(originalImage, bx, by, cx, cy)
            if b1x == b2x and b1y == b2y:
                break

    density = 20
    gridImage = np.zeros((m, n))
    gridRows = np.floor(m / density)
    gridCols = np.floor(n / density)
    gridConnectedImage = np.zeros((gridRows, gridCols))

    for i in range(m):
        for j in range(n):
            if boundaryImage[i, j] == 255:
                gridX = np.floor(gridRows * (i + 1) / m)
                gridY = np.floor(gridCols * (j + 1) / n)
                bigGridX = np.floor(gridX / gridRows * m)
                bigGridY = np.floor(gridY / gridCols * n)
                gridConnectedImage[gridX, gridY] = 255
                gridImage[bigGridX, bigGridY] = 255

    return boundaryImage, gridImage, gridConnectedImage

def getCode(gridImage):
    chainCode = []
    differentCode = []
    cnt = 0
    startX, startY = getStartPoint(gridImage, 10, 4)
    bx = startX
    by = startY
    cx = startX
    cy = startY - 1
    b1x, b1y, c1x, c1y, discard = getNextPoint(gridImage, bx, by, cx, cy)
    while 1:
        bx, by, cx, cy, di = getNextPoint(gridImage, bx, by, cx, cy)
        cnt += 1
        chainCode.append(di)
        if cnt >= 2:
            tmp = chainCode[cnt - 1] - chainCode[cnt - 2]
            if tmp < 0:
                tmp += 8
            differentCode.append(tmp)
        if bx == startX and by == startY:
            b2x, b2y, c2x, c2y, discard = getNextPoint(gridImage, bx, by, cx, cy)
            if b2x == b1x and b2y == b1y:
                break

    tmp = chainCode[0] - chainCode[cnt - 1]
    if tmp < 0:
        tmp += 8
    differentCode.append(tmp)

    return chainCode, differentCode