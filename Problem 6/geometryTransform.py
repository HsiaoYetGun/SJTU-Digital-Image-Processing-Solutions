import numpy as np

def interpolateTransform(originalImage, x, y, method):
    m, n = originalImage.size
    pix = originalImage.load()

    a = np.floor(x)
    b = np.floor(y)

    if method == 'nearest':
        px = a if x - a < 0.5 else a + 1
        py = b if y - b < 0.5 else b + 1

        if px < 0 or px >= m or py < 0 or py >= n:
            return 0
        else:
            return pix[px, py]
    elif method == 'bilinear':
        res = [0, 0, 0, 0]
        if a >= 0 and a < m:
            if b >= 0 and b < n:
                res[0] = pix[a, b]
            if b + 1 >= 0 and b + 1 < n:
                res[1] = pix[a, b+1]

        if a + 1 >= 0 and a + 1 < m:
            if b >= 0 and b < n:
                res[2] = pix[a+1, b]
            if b + 1 >= 0 and b + 1 < n:
                res[3] = pix[a+1, b+1]

        res1 = res[0] + (res[1] - res[0]) * (y - b)
        res2 = res[2] + (res[3] - res[2]) * (y - b)

        return res1 + (res2 - res1) * (x - a)

def rotateOperate(originalImage, angle, method):
    m, n = originalImage.size
    ox = m / 2
    oy = n / 2
    rotateImage = originalImage.copy()
    dest = rotateImage.load()

    for i in range(m):
        for j in range(n):
            x = (i - ox) * np.cos(np.radians(-angle)) - (j - oy) * np.sin(np.radians(-angle)) + ox
            y = (i - ox) * np.sin(np.radians(-angle)) + (j - oy) * np.cos(np.radians(-angle)) + oy
            dest[i, j] = int(interpolateTransform(originalImage, x, y, method) )

    return rotateImage

def translateOperate(originalImage, delta, method):
    m, n = originalImage.size
    translateImage = originalImage.copy()
    dest = translateImage.load()

    for i in range(m):
        for j in range(n):
            x = i - delta
            y = j - delta
            dest[i, j] = int(interpolateTransform(originalImage, x, y, method) )

    return translateImage

def scaleOperate(originalImage, scalingX, scalingY, method):
    m, n = originalImage.size
    scaleImage = originalImage.copy()
    dest = scaleImage.load()
    ox = m / 2
    oy = n / 2

    for i in range(m):
        for j in range(n):
            x = (i - ox) / scalingX + ox
            y = (j - oy) / scalingY + oy
            dest[i, j] = int(interpolateTransform(originalImage, x, y, method) )

    return scaleImage