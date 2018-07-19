from PIL import Image
import matplotlib.pylab as plt
import numpy as np
import Laplacian
import Sobel
import AveragingFilter
import MatixOperate

def imagePreprocess(input):
    row, col = input.shape
    output = np.zeros((row + 2, col + 2))
    for i in range(row):
        output[i, 0] = input[i, 0]
        output[i, col] = input[i, col - 1]
        for j in range(col):
            output[i + 1, j + 1] = input[i, j]
    for j in range(col):
        output[0, j] = input[0, j]
        output[row, j] = input[row - 1, j]
    return output

def main():
    originalImage = np.array(Image.open('./resource/skeleton_orig.tif'))
    plt.subplot(2, 4, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    preprocessImage = imagePreprocess(originalImage)
    row, col = originalImage.shape
    laplaceImage = np.zeros((row, col))
    Laplacian.laplace(preprocessImage, laplaceImage)
    plt.subplot(2, 4, 2)
    plt.imshow(laplaceImage, cmap=plt.get_cmap('gray'))
    plt.title('Laplacian')

    sharpenedImage = Laplacian.sharp(laplaceImage, originalImage)
    plt.subplot(2, 4, 3)
    plt.imshow(sharpenedImage, cmap=plt.get_cmap('gray'))
    plt.title('Sharpen')

    sobelImage = Sobel.SobelOperators(preprocessImage, mode = 'abs') #mode can choose 'abs' or 'square-root', default is 'abs'
    plt.subplot(2, 4, 4)
    plt.imshow(sobelImage, cmap=plt.get_cmap('gray'))
    plt.title('Sobel')

    tempImage = imagePreprocess(preprocessImage)
    preprocessAveragingFilterImage = imagePreprocess(tempImage)
    averagingFilterImage = AveragingFilter.averagingFilter(preprocessAveragingFilterImage, 5, 5)
    plt.subplot(2, 4, 5)
    plt.imshow(averagingFilterImage, cmap=plt.get_cmap('gray'))
    plt.title('Sobel With 5 * 5 Averaging Filter')

    maskProductImage = MatixOperate.product(sharpenedImage, averagingFilterImage)
    plt.subplot(2, 4, 6)
    plt.imshow(maskProductImage, cmap=plt.get_cmap('gray'))
    plt.title('Mask Product')

    maskSumImage = MatixOperate.sum(originalImage, maskProductImage)
    plt.subplot(2, 4, 7)
    plt.imshow(maskSumImage, cmap=plt.get_cmap('gray'))
    plt.title('Mask Sum')

    powerLawImage = MatixOperate.powerLawTransformation(maskSumImage, c = 1, gamma = 0.5)
    plt.subplot(2, 4, 8)
    plt.imshow(powerLawImage, cmap=plt.get_cmap('gray'))
    plt.title('Power Law')

    plt.show()

if __name__ == '__main__':
    main()