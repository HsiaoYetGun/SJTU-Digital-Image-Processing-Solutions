from PIL import Image
import matplotlib.pylab as plt
import numpy as np

import histogramEqualizationAlgorithm

def main():
    originalImage = np.array(Image.open('./resource/Fig1.jpg').convert('L'))

    plt.subplot(1, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original Gray Scale Map')

    plt.subplot(1, 2, 2)
    enhanceImage, histogramEqualizationImage, grayCDFImage = histogramEqualizationAlgorithm.histogramProcessing(originalImage)
    plt.imshow(enhanceImage, cmap = plt.get_cmap('gray'))
    plt.title('Enhance Gray Scale Map')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.hist(originalImage.flatten(), 256)
    plt.title('Original Histogram')
    plt.ylabel('Histogram Count')

    plt.subplot(2, 2, 2)
    plt.hist(enhanceImage.flatten(), 256)
    plt.title('Enhance Histogram')
    plt.ylabel('Histogram Count')

    plt.subplot(2, 2, 3)
    plt.plot(histogramEqualizationImage.keys(), histogramEqualizationImage.values())
    plt.title('Histogram Equalization')
    plt.xlabel('Gray Value')
    plt.ylabel('Relative Frequency')

    plt.subplot(2, 2, 4)
    plt.plot(grayCDFImage.keys(), grayCDFImage.values())
    plt.title('Transform Function')
    plt.xlabel('Original Gray Value')
    plt.ylabel('Enhanced Gray Value')

    plt.show()

    originalImage = np.array(Image.open('./resource/Fig2.jpg').convert('L'))

    plt.subplot(1, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original Gray Scale Map')

    plt.subplot(1, 2, 2)
    enhanceImage, histogramEqualizationImage, grayCDFImage = histogramEqualizationAlgorithm.histogramProcessing(originalImage)
    plt.imshow(enhanceImage, cmap = plt.get_cmap('gray'))
    plt.title('Enhance Gray Scale Map')

    plt.show()

    plt.subplot(2, 2, 1)
    plt.hist(originalImage.flatten(), 256)
    plt.title('Original Histogram')
    plt.ylabel('Histogram Count')

    plt.subplot(2, 2, 2)
    plt.hist(enhanceImage.flatten(), 256)
    plt.title('Enhance Histogram')
    plt.ylabel('Histogram Count')

    plt.subplot(2, 2, 3)
    plt.plot(histogramEqualizationImage.keys(), histogramEqualizationImage.values())
    plt.title('Histogram Equalization')
    plt.xlabel('Gray Value')
    plt.ylabel('Relative Frequency')

    plt.subplot(2, 2, 4)
    plt.plot(grayCDFImage.keys(), grayCDFImage.values())
    plt.title('Transform Function')
    plt.xlabel('Original Gray Value')
    plt.ylabel('Enhanced Gray Value')

    plt.show()

if __name__ == '__main__':
    main()