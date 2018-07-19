import pywt

def waveTransform(wavelet, originalImage, threshold):
    coeffs = pywt.wavedec2(originalImage, wavelet = wavelet, level = 3)
    cA3, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs
    cDList = [cD1, cD2, cD3]
    for i in range(3):
        cD = cDList[i]
        for j in range(len(cD)):
            if cD[j].any() < threshold:
                cD[i][j] = 0
    transformedImage = pywt.waverec2(coeffs, wavelet = wavelet)
    return cA3, transformedImage