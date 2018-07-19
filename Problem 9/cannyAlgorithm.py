import scipy.ndimage as ndi
import scipy as sp
import numpy
from PIL import Image

def canny(img):
    sigma = 4
    imgdata = numpy.array(img, dtype = float)
    gaussianImage = ndi.filters.gaussian_filter(imgdata, sigma)

    emptyImage = Image.new('L', img.size)
    gradientX = numpy.array(emptyImage, dtype = float)
    gradientY = numpy.array(emptyImage, dtype = float)

    sobelX = [[-1,0,1],
               [-2,0,2],
               [-1,0,1]]
    sobelY = [[-1,-2,-1],
               [0,0,0],
               [1,2,1]]

    m = img.size[1]
    n = img.size[0]

    for x in range(1, m - 1):
        for y in range(1, n - 1):
            px = (sobelX[0][0] * gaussianImage[x - 1][y - 1]) + (sobelX[0][1] * gaussianImage[x][y - 1]) + \
                (sobelX[0][2] * gaussianImage[x + 1][y - 1]) + (sobelX[1][0] * gaussianImage[x - 1][y]) + \
                (sobelX[1][1] * gaussianImage[x][y]) + (sobelX[1][2] * gaussianImage[x + 1][y]) + \
                (sobelX[2][0] * gaussianImage[x - 1][y + 1]) + (sobelX[2][1] * gaussianImage[x][y + 1]) + \
                (sobelX[2][2] * gaussianImage[x + 1][y + 1])

            py = (sobelY[0][0] * gaussianImage[x - 1][y - 1]) + (sobelY[0][1] * gaussianImage[x][y - 1]) + \
                (sobelY[0][2] * gaussianImage[x + 1][y - 1]) + (sobelY[1][0] * gaussianImage[x - 1][y]) + \
                (sobelY[1][1] * gaussianImage[x][y]) + (sobelY[1][2] * gaussianImage[x + 1][y]) + \
                (sobelY[2][0] * gaussianImage[x - 1][y + 1]) + (sobelY[2][1] * gaussianImage[x][y + 1]) + \
                (sobelY[2][2] * gaussianImage[x + 1][y + 1])
            gradientX[x][y] = px
            gradientY[x][y] = py

    gradientImageMag = sp.hypot(gradientX, gradientY)
    gradientImageDir = sp.arctan2(gradientY, gradientX)

    for x in range(m):
        for y in range(n):
            if (gradientImageDir[x][y] < 22.5 and gradientImageDir[x][y] >= 0) or \
            (gradientImageDir[x][y] >= 157.5 and gradientImageDir[x][y] < 202.5) or \
            (gradientImageDir[x][y] >= 337.5 and gradientImageDir[x][y] <= 360):
                gradientImageDir[x][y] = 0
            elif (gradientImageDir[x][y] >= 22.5 and gradientImageDir[x][y] < 67.5) or \
                (gradientImageDir[x][y] >= 202.5 and gradientImageDir[x][y] < 247.5):
                gradientImageDir[x][y] = 45
            elif (gradientImageDir[x][y] >= 67.5 and gradientImageDir[x][y] < 112.5)or \
                (gradientImageDir[x][y] >= 247.5 and gradientImageDir[x][y] < 292.5):
                gradientImageDir[x][y] = 90
            else:
                gradientImageDir[x][y] = 135


    magSup = gradientImageMag.copy()

    for x in range(1, m - 1):
        for y in range(1, n - 1):
            if gradientImageDir[x][y] == 0:
                if (gradientImageMag[x][y] <= gradientImageMag[x][y + 1]) or \
                    (gradientImageMag[x][y] <= gradientImageMag[x][y - 1]):
                    magSup[x][y] = 0
            elif gradientImageDir[x][y] == 45:
                if (gradientImageMag[x][y] <= gradientImageMag[x - 1][y + 1]) or \
                    (gradientImageMag[x][y] <= gradientImageMag[x + 1][y - 1]):
                    magSup[x][y] = 0
            elif gradientImageDir[x][y] == 90:
                if (gradientImageMag[x][y] <= gradientImageMag[x + 1][y]) or \
                    (gradientImageMag[x][y] <= gradientImageMag[x - 1][y]):
                    magSup[x][y] = 0
            else:
                if (gradientImageMag[x][y] <= gradientImageMag[x + 1][y + 1]) or \
                    (gradientImageMag[x][y] <= gradientImageMag[x - 1][y - 1]):
                    magSup[x][y] = 0

    maxGrayValue = numpy.max(magSup)
    th = 0.1 * maxGrayValue
    tl = 0.04 * maxGrayValue


    gnh = numpy.zeros((m, n))
    gnl = numpy.zeros((m, n))

    for x in range(m):
        for y in range(n):
            if magSup[x][y] >= th:
                gnh[x][y] = magSup[x][y]
            if magSup[x][y] >= tl:
                gnl[x][y] = magSup[x][y]
    gnl = gnl - gnh


    def traverse(i, j):
        x = [-1, 0, 1, -1, 1, -1, 0, 1]
        y = [-1, -1, -1, 0, 0, 1, 1, 1]
        for k in range(8):
            if gnh[i + x[k]][j + y[k]] == 0 and gnl[i + x[k]][j + y[k]] != 0:
                gnh[i + x[k]][j + y[k]] = 1
                traverse(i + x[k], j + y[k])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if gnh[i][j]:
                gnh[i][j] = 1
                traverse(i, j)

    return gaussianImage, gnh