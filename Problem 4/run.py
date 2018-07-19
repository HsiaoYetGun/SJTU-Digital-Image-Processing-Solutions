from PIL import Image
import matplotlib.pylab as plt
import numpy as np

import AddNoise
import MeanFilters

def main():
    originalImage = np.array(Image.open('./resource/Circuit.tif'))
    plt.subplot(2, 2, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    gaussianNoiseImage = AddNoise.addNoisy("Gaussian", originalImage)
    plt.subplot(2, 2, 2)
    plt.imshow(gaussianNoiseImage, cmap = plt.get_cmap('gray'))
    plt.title('Gaussian Noise')

    arithmeticMeanImage = MeanFilters.ArithmeticMeanFilter3(gaussianNoiseImage)
    plt.subplot(2, 2, 3)
    plt.imshow(arithmeticMeanImage, cmap = plt.get_cmap('gray'))
    plt.title('Arithmetic Mean Filter')

    geometricMeanImage = MeanFilters.GeometricMeanFilter3(gaussianNoiseImage)
    plt.subplot(2, 2, 4)
    plt.imshow(geometricMeanImage, cmap = plt.get_cmap('gray'))
    plt.title('Geometric Mean Filter')

    plt.show()

    pepperNoiseImage = AddNoise.addNoisy("Pepper", originalImage)
    plt.subplot(2, 2, 1)
    plt.imshow(pepperNoiseImage, cmap = plt.get_cmap('gray'))
    plt.title('Pepper Noise')

    saltNoiseImage = AddNoise.addNoisy("Salt", originalImage)
    plt.subplot(2, 2, 2)
    plt.imshow(saltNoiseImage, cmap = plt.get_cmap('gray'))
    plt.title('Salt Noise')

    contraharmonicMeanImage1 = MeanFilters.ContraharmonicMeanFilter(pepperNoiseImage, 1.5)
    plt.subplot(2, 2, 3)
    plt.imshow(contraharmonicMeanImage1, cmap = plt.get_cmap('gray'))
    plt.title('Pepper Noise Use Contraharmonic Mean Filter Q = 1.5')


    contraharmonicMeanImage2 = MeanFilters.ContraharmonicMeanFilter(saltNoiseImage, -1.5)
    plt.subplot(2, 2, 4)
    plt.imshow(contraharmonicMeanImage2, cmap = plt.get_cmap('gray'))
    plt.title('Salt Noise Use Contraharmonic Mean Filter Q = -1.5')

    plt.show()

    contraharmonicMeanImage3 = MeanFilters.ContraharmonicMeanFilter(pepperNoiseImage, -1.5)
    plt.subplot(1, 2, 1)
    plt.imshow(contraharmonicMeanImage3, cmap = plt.get_cmap('gray'))
    plt.title('Pepper Noise Use Contraharmonic Mean Filter Q = -1.5')

    contraharmonicMeanImage4 = MeanFilters.ContraharmonicMeanFilter(saltNoiseImage, 1.5)
    plt.subplot(1, 2, 2)
    plt.imshow(contraharmonicMeanImage4, cmap = plt.get_cmap('gray'))
    plt.title('Salt Noise Use Contraharmonic Mean Filter Q = 1.5')

    plt.show()

    NoiseImage = AddNoise.addNoisy("Salt", originalImage)
    saltAndPepperNoiseImage = AddNoise.addNoisy("Pepper", NoiseImage)
    plt.subplot(2, 2, 1)
    plt.imshow(saltAndPepperNoiseImage, cmap = plt.get_cmap('gray'))
    plt.title('Salt And Pepper Noise')

    medianImage = MeanFilters.MedianFilter(saltAndPepperNoiseImage)
    plt.subplot(2, 2, 2)
    plt.imshow(medianImage, cmap = plt.get_cmap('gray'))
    plt.title('1st Median Filter')

    medianImage = MeanFilters.MedianFilter(medianImage)
    plt.subplot(2, 2, 3)
    plt.imshow(medianImage, cmap = plt.get_cmap('gray'))
    plt.title('2nd Median Filter')

    medianImage = MeanFilters.MedianFilter(medianImage)
    plt.subplot(2, 2, 4)
    plt.imshow(medianImage, cmap = plt.get_cmap('gray'))
    plt.title('3rd Median Filter')

    plt.show()

    maxImage = MeanFilters.MaxFilter(pepperNoiseImage)
    plt.subplot(1, 2, 1)
    plt.imshow(maxImage, cmap = plt.get_cmap('gray'))
    plt.title('Max Filter')

    minImage = MeanFilters.MinFilter(saltNoiseImage)
    plt.subplot(1, 2, 2)
    plt.imshow(minImage, cmap = plt.get_cmap('gray'))
    plt.title('Min Filter')

    plt.show()

    uniformNoiseImage = AddNoise.addNoisy('Uniform', originalImage, variance = 800)
    plt.subplot(2, 3, 1)
    plt.imshow(uniformNoiseImage, cmap = plt.get_cmap('gray'))
    plt.title('Uniform Noise')

    unifSaltNoiseImage = AddNoise.addNoisy('Salt', uniformNoiseImage)
    unifSaltPepperNoiseImage = AddNoise.addNoisy('Pepper', unifSaltNoiseImage)
    plt.subplot(2, 3, 2)
    plt.imshow(unifSaltPepperNoiseImage, cmap = plt.get_cmap('gray'))
    plt.title('Uniform Salt Pepper Noise')

    arithmeticMeanImage5 = MeanFilters.ArithmeticMeanFilter5(unifSaltPepperNoiseImage)
    plt.subplot(2, 3, 3)
    plt.imshow(arithmeticMeanImage5, cmap = plt.get_cmap('gray'))
    plt.title('Arithmetic Mean Filter')

    geometricMeanImage5 = MeanFilters.GeometricMeanFilter5(unifSaltPepperNoiseImage)
    plt.subplot(2, 3, 4)
    plt.imshow(geometricMeanImage5, cmap = plt.get_cmap('gray'))
    plt.title('Geometric Mean Filter')

    medianImage5 = MeanFilters.MedianFilter5(unifSaltPepperNoiseImage)
    plt.subplot(2, 3, 5)
    plt.imshow(medianImage5, cmap = plt.get_cmap('gray'))
    plt.title('Median Filter')

    alphaTrimmedMeanFilter = MeanFilters.AlphaMeanFilter(unifSaltPepperNoiseImage, 5)
    plt.subplot(2, 3, 6)
    plt.imshow(alphaTrimmedMeanFilter, cmap = plt.get_cmap('gray'))
    plt.title('Alpha Trimmed Mean Filter')

    plt.show()

if __name__ == "__main__":
    main()