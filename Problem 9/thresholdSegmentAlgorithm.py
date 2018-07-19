import numpy as np
from PIL import Image

def globalThreshold(originalImage, deltLimit = 0):
    threshold = np.mean(originalImage)
    deltT = threshold
    while(deltT > deltLimit):
        g1 = originalImage[originalImage > threshold]
        g2 = originalImage[originalImage <= threshold]

        t1 = np.mean(g1)
        t2 = np.mean(g2)

        newThreshold = (t1 + t2) / 2
        deltT = np.abs(newThreshold - threshold)
        threshold = newThreshold

    return threshold

def globalThresholdSegment(originalImage):
    threshold = globalThreshold(originalImage)
    globalSegmentImage = originalImage.copy()
    globalSegmentImage[globalSegmentImage > threshold] = 255
    globalSegmentImage[globalSegmentImage <= threshold] = 0
    return globalSegmentImage


def getSigma(image, i):
    pNumH = np.sum(image.histogram()[: i + 1])
    pNumL = np.sum(image.histogram()[i + 1 :])

    mSumH = 0
    for j in range(1, i + 1):
        mSumH += j * image.histogram()[j]

    mSumL = 0
    for j in range(i + 1, 255):
        mSumL += j * image.histogram()[j]
    try:
        u0 = 1.0 * mSumH / pNumH
        u1 = 1.0 * mSumL / pNumL
        w0 = 1.0 * pNumH / (pNumH + pNumL)
    except:
        return 0

    w1 = 1.0 - w0
    u = (u0 - u1) ** 2
    sigma = w0 * w1 * u

    return sigma

def otsuThreshold(inputImage):
  threshold = 0
  gSigma = 0
  for i in range(1,255):
    sigma = getSigma(inputImage,i)
    if gSigma < sigma:
      gSigma = sigma
      threshold = i
  return threshold

def otsuThresholdSegment(originalImage):
    inputImage = Image.open('./resource/polymersomes.tif').convert("L")
    threshold = otsuThreshold(inputImage)
    otsuSegmentImage = originalImage.copy()
    otsuSegmentImage[otsuSegmentImage > threshold] = 255
    otsuSegmentImage[otsuSegmentImage <= threshold] = 0
    return otsuSegmentImage