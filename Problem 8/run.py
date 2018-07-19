from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import morphologyAlgorithm

def main():
    originalImage = Image.open('./resource/Fig0929(a)(text_image).tif').convert('1')

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    B = np.ones((51, 1))
    erosionImage = morphologyAlgorithm.erosionOperate(originalImage, B)
    plt.subplot(2, 2, 2)
    plt.imshow(erosionImage, cmap = plt.get_cmap('gray'))
    plt.title('Erosion')

    openingOriginalImage = morphologyAlgorithm.dilationOperate(originalImage, B)
    plt.subplot(2, 2, 3)
    plt.imshow(openingOriginalImage, cmap = plt.get_cmap('gray'))
    plt.title('Opening Original')

    B = np.ones((3, 3))
    reconstructionImage = morphologyAlgorithm.reconstructionOperate(originalImage, erosionImage, B)
    plt.subplot(2, 2, 4)
    plt.imshow(reconstructionImage, cmap = plt.get_cmap('gray'))
    plt.title('Reconstruction Opening')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(2, 2, 2)
    complementImage = morphologyAlgorithm.complementOperate(originalImage)
    plt.imshow(complementImage, cmap = plt.get_cmap('gray'))
    plt.title('Complement')

    B = np.ones((3, 3))
    plt.subplot(2, 2, 3)
    maskImage, fillingHolesImage = morphologyAlgorithm.holeFillingOperate(originalImage, B)
    plt.imshow(maskImage, cmap = plt.get_cmap('gray'))
    plt.title('Mark')

    plt.subplot(2, 2, 4)
    plt.imshow(fillingHolesImage, cmap = plt.get_cmap('gray'))
    plt.title('Filling Holes')

    plt.show()

    B = np.ones((3, 3))
    plt.subplot(1, 2, 1)
    maskImage2, borderClearingImage = morphologyAlgorithm.borderClearing(originalImage, B)
    plt.imshow(maskImage2, cmap = plt.get_cmap('gray'))
    plt.title('Mark')

    plt.subplot(1, 2, 2)
    plt.imshow(borderClearingImage, cmap = plt.get_cmap('gray'))
    plt.title('Border Clearing')

    plt.show()


if __name__ == '__main__':
    main()