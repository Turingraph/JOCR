###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

import cv2
from ImgProcess_I.GrayImage import GrayImage
from ImgProcess_I.Image import Image

img_path = parent + "/Examples/FFT/Image/jojomeme.jpg"
img = Image(img)
img.Show("Color")
img = GrayImage(img)
img.Show("B&W")
img.FFTSharp(img, 20, 10, is_show=True)
img.Show(fft_img, "sharp")

"""
python3 EditImage.py
"""
