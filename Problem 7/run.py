from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import DiscreteCosineTransform
import WaveletsCompression

def main():
    originalImage = np.array(Image.open('./resource/lenna.tif'))
    row, col = originalImage.shape
    plt.subplot(2, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    zonalMaskSubImg = DiscreteCosineTransform.imageCompress(originalImage, "zonal mask")
    zonalMaskRestoreImage = DiscreteCosineTransform.imageRestore(zonalMaskSubImg, row, col)
    plt.subplot(2, 3, 2)
    plt.imshow(zonalMaskRestoreImage, cmap = plt.get_cmap('gray'))
    plt.title('Restore Image(zonal mask)')

    zonalMaskDifferenceImage = originalImage - zonalMaskRestoreImage
    plt.subplot(2, 3, 3)
    plt.imshow(zonalMaskDifferenceImage, cmap = plt.get_cmap('gray'))
    plt.title('Difference Image(zonal mask)')

    thresholdMaskSubImg = DiscreteCosineTransform.imageCompress(originalImage, "threshold mask")
    thresholdMaskRestoreImage = DiscreteCosineTransform.imageRestore(thresholdMaskSubImg, row, col)
    plt.subplot(2, 3, 5)
    plt.imshow(thresholdMaskRestoreImage, cmap = plt.get_cmap('gray'))
    plt.title('Restore Image(threshold mask)')

    thresholdDifferenceImage = originalImage - thresholdMaskRestoreImage
    plt.subplot(2, 3, 6)
    plt.imshow(thresholdDifferenceImage, cmap = plt.get_cmap('gray'))
    plt.title('Difference Image(threshold mask)')

    plt.show()

    haarTransformImage, haarReconstructImage = WaveletsCompression.waveTransform('haar', originalImage, threshold = 0)
    plt.subplot(1, 3, 1)
    plt.imshow(haarTransformImage, cmap = plt.get_cmap('gray'))
    plt.title('Haar Transform Image')

    plt.subplot(1, 3, 2)
    plt.imshow(haarReconstructImage, cmap = plt.get_cmap('gray'))
    plt.title('Haar Reconstruct Image')

    haarDifferenceImage = originalImage - haarReconstructImage
    plt.subplot(1, 3, 3)
    plt.imshow(haarDifferenceImage, cmap = plt.get_cmap('gray'))
    plt.title('Difference Image(Haar)')

    plt.show()

    daubechiesTransformImage, daubechiesReconstructImage = WaveletsCompression.waveTransform('db3', originalImage, threshold = 0)
    plt.subplot(1, 3, 1)
    plt.imshow(daubechiesTransformImage, cmap = plt.get_cmap('gray'))
    plt.title('Daubechies Transform Image')

    plt.subplot(1, 3, 2)
    plt.imshow(daubechiesReconstructImage, cmap = plt.get_cmap('gray'))
    plt.title('Daubechies Reconstruct Image')

    daubechiesDifferenceImage = originalImage - daubechiesReconstructImage
    plt.subplot(1, 3, 3)
    plt.imshow(daubechiesDifferenceImage, cmap = plt.get_cmap('gray'))
    plt.title('Difference Image(Daubechies)')

    plt.show()

    symletTransformImage, symletReconstructImage = WaveletsCompression.waveTransform('sym3', originalImage, threshold = 0)
    plt.subplot(1, 3, 1)
    plt.imshow(symletTransformImage, cmap = plt.get_cmap('gray'))
    plt.title('Symlet Transform Image')

    plt.subplot(1, 3, 2)
    plt.imshow(symletReconstructImage, cmap = plt.get_cmap('gray'))
    plt.title('Symlet Reconstruct Image')

    symletDifferenceImage = originalImage - symletReconstructImage
    plt.subplot(1, 3, 3)
    plt.imshow(symletDifferenceImage, cmap = plt.get_cmap('gray'))
    plt.title('Difference Image(Symlet)')

    plt.show()

    biorthogonalCDFTransformImage, biorthogonalCDFReconstructImage = WaveletsCompression.waveTransform('bior1.1', originalImage, threshold = 0)
    plt.subplot(1, 3, 1)
    plt.imshow(biorthogonalCDFTransformImage, cmap = plt.get_cmap('gray'))
    plt.title('biorthogonalCDF Transform Image')

    plt.subplot(1, 3, 2)
    plt.imshow(biorthogonalCDFReconstructImage, cmap = plt.get_cmap('gray'))
    plt.title('biorthogonalCDF Reconstruct Image')

    biorthogonalCDFDifferenceImage = originalImage - biorthogonalCDFReconstructImage
    plt.subplot(1, 3, 3)
    plt.imshow(biorthogonalCDFDifferenceImage, cmap = plt.get_cmap('gray'))
    plt.title('Difference Image(biorthogonalCDF)')

    plt.show()

if __name__ == "__main__":
    main()