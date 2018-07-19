import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

import segmentAlgorithm
import marrHildrethAlgorithm
import cannyAlgorithm
import thresholdSegmentAlgorithm

def main():
    originalImage = np.array(Image.open('./resource/building.tif'))

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    robertsGxImage, robertsGyImage, robertsImage = segmentAlgorithm.Roberts(originalImage)
    plt.subplot(2, 2, 2)
    plt.imshow(robertsGxImage, cmap = plt.get_cmap('gray'))
    plt.title('Roberts gx')

    plt.subplot(2, 2, 3)
    plt.imshow(robertsGyImage, cmap = plt.get_cmap('gray'))
    plt.title('Roberts gy')

    plt.subplot(2, 2, 4)
    plt.imshow(robertsImage, cmap = plt.get_cmap('gray'))
    plt.title('Roberts')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    prewittGxImage, prewittGyImage, prewittImage = segmentAlgorithm.Prewitt(originalImage)
    plt.subplot(2, 2, 2)
    plt.imshow(prewittGxImage, cmap = plt.get_cmap('gray'))
    plt.title('Prewitt gx')

    plt.subplot(2, 2, 3)
    plt.imshow(prewittGyImage, cmap = plt.get_cmap('gray'))
    plt.title('Prewitt gy')

    plt.subplot(2, 2, 4)
    plt.imshow(prewittImage, cmap = plt.get_cmap('gray'))
    plt.title('Prewitt')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    sobelGxImage, sobelGyImage, sobelImage = segmentAlgorithm.Sobel(originalImage)
    plt.subplot(2, 2, 2)
    plt.imshow(sobelGxImage, cmap = plt.get_cmap('gray'))
    plt.title('Sobel gx')

    plt.subplot(2, 2, 3)
    plt.imshow(sobelGyImage, cmap = plt.get_cmap('gray'))
    plt.title('Sobel gy')

    plt.subplot(2, 2, 4)
    plt.imshow(sobelImage, cmap = plt.get_cmap('gray'))
    plt.title('Sobel')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(2, 2, 2)
    LoGImage, marrHildrethImage1, marrHildrethImage2 = marrHildrethAlgorithm.MarrHildreth(originalImage)
    plt.imshow(LoGImage, cmap = plt.get_cmap('gray'))
    plt.title('LoG Without Threshold')

    plt.subplot(2, 2, 3)
    plt.imshow(marrHildrethImage1, cmap = plt.get_cmap('gray'))
    plt.title('Marr-Hildreth Threshold = 0')

    plt.subplot(2, 2, 4)
    plt.imshow(marrHildrethImage2, cmap = plt.get_cmap('gray'))
    plt.title('Marr-Hildreth Threshold = 15% Max(LoGImage)')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(2, 2, 2)
    smoothImage, cannyImage = cannyAlgorithm.canny(Image.open('./resource/building.tif').convert('L'))
    plt.imshow(smoothImage, cmap = plt.get_cmap('gray'))
    plt.title('Smooth')

    plt.subplot(2, 2, 3)
    plt.imshow(marrHildrethImage2, cmap = plt.get_cmap('gray'))
    plt.title('Marr-Hildreth Threshold = 15% Max(LoGImage)')

    plt.subplot(2, 2, 4)
    plt.imshow(cannyImage, cmap = plt.get_cmap('gray'))
    plt.title('Canny')

    plt.show()

    originalImage = np.array(Image.open('./resource/polymersomes.tif'))

    plt.subplot(1, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(1, 3, 2)
    globalSegmentImage = thresholdSegmentAlgorithm.globalThresholdSegment(originalImage)
    plt.imshow(globalSegmentImage, cmap = plt.get_cmap('gray'))
    plt.title('Global Threshold Segment')

    plt.subplot(1, 3, 3)
    otsuSegmentImage = thresholdSegmentAlgorithm.otsuThresholdSegment(originalImage)
    plt.imshow(otsuSegmentImage, cmap = plt.get_cmap('gray'))
    plt.title('Otsu Threshold Segment')

    plt.show()

if __name__ == '__main__':
    main()