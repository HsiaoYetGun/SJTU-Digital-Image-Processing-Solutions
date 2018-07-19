import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import geometryTransform

def main():
    originalImage = Image.open('./resource/ray_trace_bottle.tif')

    plt.subplot(1, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    rotateImage1 = geometryTransform.rotateOperate(originalImage, 45, 'nearest')
    plt.subplot(1, 3, 2)
    plt.imshow(rotateImage1, cmap = plt.get_cmap('gray'))
    plt.title('Rotate By Nearest Method')

    rotateImage2 = geometryTransform.rotateOperate(originalImage, 45, 'bilinear')
    plt.subplot(1, 3, 3)
    plt.imshow(rotateImage2, cmap = plt.get_cmap('gray'))
    plt.title('Rotate By Bilinear Method')

    plt.show()

    plt.subplot(1, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    delta = 100
    translateImage1 = geometryTransform.translateOperate(originalImage, delta, 'nearest')
    plt.subplot(1, 3, 2)
    plt.imshow(translateImage1, cmap = plt.get_cmap('gray'))
    plt.title('Translate By Nearest Method(delta = %s)' % delta)

    translateImage2 = geometryTransform.translateOperate(originalImage, delta, 'bilinear')
    plt.subplot(1, 3, 3)
    plt.imshow(translateImage2, cmap = plt.get_cmap('gray'))
    plt.title('Translate By Bilinear Method(delta = %s)' % delta)

    plt.show()

    scalingX = 0.9
    scalingY = 1.1
    plt.subplot(1, 3, 1)
    plt.imshow(originalImage, cmap = plt.get_cmap('gray'))
    plt.title('Original')

    scaleImage1 = geometryTransform.scaleOperate(originalImage, scalingX, scalingY, 'nearest')
    plt.subplot(1, 3, 2)
    plt.imshow(scaleImage1, cmap = plt.get_cmap('gray'))
    plt.title('Scale By Nearest Method(scalingX = %s, scalingY = %s)' % (scalingX, scalingY))

    scaleImage2 = geometryTransform.scaleOperate(originalImage, scalingX, scalingY, 'bilinear')
    plt.subplot(1, 3, 3)
    plt.imshow(scaleImage2, cmap = plt.get_cmap('gray'))
    plt.title('Scale By Bilinear Method(scalingX = %s, scalingY = %s)' % (scalingX, scalingY))

    plt.show()

if __name__ == '__main__':
    main()