###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

import ImgProcess.ShowImage as show
import ImgProcess.FFT as fft
from ImgProcess_I.GrayImage import GrayImage, ColorImage
import cv2

path = parent + "/Examples/01_Page/RandomImage/jojomeme.jpg"

img = show.ReadImage(path)
img = GrayImage(img)
fft_img = fft.FFTSharpen02(img, 10, 10, is_show=True)

show.SaveImage(fft_img, "fft_img")

"""
python3 Image2Text.py
"""
