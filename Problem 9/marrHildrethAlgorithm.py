from scipy import signal
import numpy as np

def LoG(x, y, sigma):
    t = np.power(x, 2) + np.power(y, 2)
    res = (t - np.power(sigma, 2) * 1.0) / np.power(sigma, 4) * np.exp(- t / (2 * np.power(sigma, 2)))
    return res

def LoGThreshold(inputImage, threshold):
    m, n = inputImage.shape
    outputImage = inputImage.copy()
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            tmpList = []
            tmpList.append(np.sum(inputImage[i - 1 : i, j - 1 : j]))
            tmpList.append(np.sum(inputImage[i - 1 : i, j : j + 1]))
            tmpList.append(np.sum(inputImage[i : i + 1, j - 1 : j]))
            tmpList.append(np.sum(inputImage[i : i + 1, j : j + 1]))
            maxValue = max(tmpList)
            minValue = min(tmpList)
            if maxValue > threshold and minValue < threshold:
                outputImage[i, j] = 255
    return outputImage

def MarrHildreth(originalImage):
    maxPix = np.max(originalImage)
    minPix = np.min(originalImage)
    diff = maxPix - minPix
    originalImage = (originalImage - minPix) * 1.0 / diff
    n = 25
    sigma = 4
    w = np.zeros((n, n))
    center = (n - 1) / 2
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            y = i - center
            x = j - center
            w[i - 1, j - 1] = LoG(x, y, sigma)
    w = w * 1.0 / np.sum(w)
    LoGImage = originalImage - signal.convolve2d(originalImage, w, mode = 'same')

    marrHildrethImage1 = LoGThreshold(LoGImage, 0)
    threshold = 0.15 * np.max(LoGImage)
    marrHildrethImage2 = LoGThreshold(LoGImage, threshold)
    return LoGImage, marrHildrethImage1, marrHildrethImage2