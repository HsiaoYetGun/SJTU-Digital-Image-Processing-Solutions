from PIL import Image
import numpy as np
import matplotlib.pylab as plt

import BlurringDegradation
import AddNoise
import Filter

def main():
    originalImage = np.array(Image.open('./resource/book_cover.jpg').convert('L'))
    plt.subplot(2, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    degradationFunction = BlurringDegradation.getBlurringDegradationFunction(originalImage)
    originalFFT = np.fft.fft2(originalImage)
    blurringDegradationImageFFT = originalFFT * degradationFunction
    plt.subplot(2, 3, 2)
    plt.imshow(np.real(np.fft.ifft2(blurringDegradationImageFFT)), cmap = plt.get_cmap('gray'))
    plt.title('Blurring Degradation')

    mean = 0
    variance = 0.00005
    noiseFunction = AddNoise.addGaussianNoise(blurringDegradationImageFFT, mean, variance)
    plt.subplot(2, 3, 3)
    noiseFunctionFFT = np.fft.fft2(noiseFunction)
    noiseImageFFT = blurringDegradationImageFFT + noiseFunction
    plt.imshow(np.real(np.fft.ifft2(noiseImageFFT)), cmap = plt.get_cmap('gray'))
    plt.title('Gaussian Noise(Mean = %s, Variance = %s)' % (mean, variance))

    IF = Filter.inverseFilter(blurringDegradationImageFFT, degradationFunction)
    plt.subplot(2, 3, 5)
    invertFilterImage = np.real(np.fft.ifft2(IF))
    plt.imshow(invertFilterImage, cmap = plt.get_cmap('gray'))
    plt.title('Inverse Filter')

    IFFT = Filter.WienerDeconvolutionFilter(noiseImageFFT, noiseFunctionFFT, degradationFunction, originalFFT)
    resultImage = np.real(np.fft.ifft2(IFFT))
    plt.subplot(2, 3, 6)
    plt.imshow(resultImage, cmap = plt.get_cmap('gray'))
    plt.title('Wiener Deconvolution Filter(Mean = %s, Variance = %s)' % (mean, variance))

    plt.show()

if __name__ == '__main__':
    main()