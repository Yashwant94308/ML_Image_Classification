import numpy as np
import pywt
import cv2
from matplotlib import pyplot as plt


def w2d(img, mode='haar', level=1):
    imArray = img

    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)

    imArray = np.float32(imArray)
    imArray /= 255

    coeffs = pywt.wavedec2(imArray, mode, level=level)

    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0

    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)

    return imArray_H


# imgpa = './test_images/virat1.jpg'
# imgp = cv2.imread(imgpa)
# a = w2d(imgp, 'db1', 5)
# plt.imshow(a, cmap='gray')
# plt.show()
