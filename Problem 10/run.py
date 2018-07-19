from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import thresholdSegmentAlgorithm
import averagingFilter
import boundaryFollowingAlgorithm
import principalComponentsAlgorithm

def main():
    '''
    originalImage = np.array(Image.open('./resource/noisy_stroke.tif'))
    m, n = originalImage.shape
    for i in range(m):
        for j in range(n):
            originalImage[i, j] = 255 if originalImage[i, j] > 100 else 0

    plt.subplot(2, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(2, 3, 2)
    l = 9
    averagingFilterImage = averagingFilter.averagingFilter(originalImage, l)
    plt.imshow(averagingFilterImage, cmap = plt.get_cmap('gray'))
    plt.title('%s * %s Averaging Mask' % (l, l))

    plt.subplot(2, 3, 3)
    ostuThresholdSegmentImage = thresholdSegmentAlgorithm.otsuThresholdSegment(averagingFilterImage)
    plt.imshow(ostuThresholdSegmentImage, cmap = plt.get_cmap('gray'))
    plt.title('Ostu Threshold Segment')

    plt.subplot(2, 3, 4)
    boundaryImage, gridImage, gridConnectedImage = boundaryFollowingAlgorithm.boundaryFollowing(ostuThresholdSegmentImage)
    plt.imshow(boundaryImage, cmap = plt.get_cmap('gray'))
    plt.title('Boundary')

    plt.subplot(2, 3, 5)
    plt.imshow(gridImage, cmap = plt.get_cmap('gray'))
    plt.title('Grid Boundary')

    plt.subplot(2, 3, 6)
    plt.imshow(gridConnectedImage, cmap = plt.get_cmap('gray'))
    plt.title('Grid Connected Boundary')

    plt.show()

    chainCode, differentCode = boundaryFollowingAlgorithm.getCode(gridConnectedImage)
    print(chainCode)
    print(differentCode)
    '''

    originalImageSet = []
    for i in range(1, 7):
        temp = Image.open('./resource/WashingtonDC_Band%s.tif' % i)
        originalImageSet.append(temp)
    reconstructsImageSet = principalComponentsAlgorithm.principalComponentsTransform(originalImageSet)

    for i in range(6):
        plt.subplot(1, 2, 1)
        plt.imshow(originalImageSet[i], cmap = plt.get_cmap('gray'))
        plt.title('Original Image %s' % (i + 1))

        plt.subplot(1, 2, 2)
        plt.imshow(reconstructsImageSet[i], cmap = plt.get_cmap('gray'))
        plt.title('Reconstruct Image %s' % (i + 1))

        plt.show()
if __name__ == '__main__':
    main()