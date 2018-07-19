from PIL import Image
import matplotlib.pyplot as plt

import Frequency

def main():
    originalImage = Image.open('./resource/characters_test_pattern.tif')
    radius = 160

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(2, 2, 2)
    idealLowpassImage = Frequency.idealLowpass(originalImage, radius)
    plt.imshow(idealLowpassImage, cmap = plt.get_cmap('gray'))
    plt.title('Ideal Lowpass With Radius = %s' % radius)

    plt.subplot(2, 2, 3)
    butterworthLowpassImage = Frequency.butterworthLowpass(originalImage, radius, 2)
    plt.imshow(butterworthLowpassImage, cmap = plt.get_cmap('gray'))
    plt.title('Butterworth Lowpass With Radius = %s' % radius)

    plt.subplot(2, 2, 4)
    gaussianLowpassImage = Frequency.gaussianLowpass(originalImage, radius)
    plt.imshow(gaussianLowpassImage, cmap = plt.get_cmap('gray'))
    plt.title('Gaussian Lowpass With Radius = %s' % radius)

    plt.show()

    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    plt.subplot(2, 2, 2)
    idealHighpassImage = Frequency.idealHighpass(originalImage, radius)
    plt.imshow(idealHighpassImage, cmap = plt.get_cmap('gray'))
    plt.title('Ideal Highpass With Radius = %s' % radius)

    plt.subplot(2, 2, 3)
    butterworthHighpassImage = Frequency.butterworthHighpass(originalImage, radius, 2)
    plt.imshow(butterworthHighpassImage, cmap = plt.get_cmap('gray'))
    plt.title('Butterworth Highpass With Radius = %s' % radius)

    plt.subplot(2, 2, 4)
    gaussianHighpassImage = Frequency.gaussianHighpass(originalImage, radius)
    plt.imshow(gaussianHighpassImage, cmap = plt.get_cmap('gray'))
    plt.title('Gaussian Highpass With Radius = %s' % radius)

    plt.show()

if __name__ == '__main__':
    main()