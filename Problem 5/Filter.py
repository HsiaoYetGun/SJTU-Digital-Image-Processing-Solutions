import copy
import numpy as np

def inverseFilter(originalImage, degradationFunction):
    row, col = originalImage.shape
    res = copy.copy(originalImage)
    for i in range(row):
        for j in range(col):
            res[i, j] /= degradationFunction[i, j]
    return res

def WienerDeconvolutionFilter(G, Sn, H, Sf):
    HConjugate = np.conjugate(H)
    HSpectrum = np.real(H * HConjugate)
    SnConjugate = np.conjugate(Sn)
    SnSpectrum = np.real(Sn * SnConjugate)
    SfConjugate = np.conjugate(Sf)
    SfSpectrum = np.real(Sf * SfConjugate)
    row, col = G.shape
    F_hat = np.zeros((row, col), dtype = np.complex)
    for u in range(row):
        for v in range(col):
            F_hat[u, v] = G[u, v] * HSpectrum[u, v] / ((HSpectrum[u, v] + SnSpectrum[u, v] / SfSpectrum[u, v]) * H[u, v])
    return F_hat