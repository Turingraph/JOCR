###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

import ImgProcess.ShowImage as show
import ImgProcess.Threshold as thresh
import ImgProcess.Convolution as con
import ImgProcess.FFT as fft
import ImgProcess.Contour as tour

from ImgProcess.RemoveNoise import RemoveNoice
from ImgProcess.FontSize import ThickFont
from ImgProcess.Rotation import Rotate
from ImgProcess.GrayImage import GrayImage
from ImgProcess.Zoom import RemoveBorders,Zoom

from PIL import Image
import cv2
import numpy as np

path = parent + '/Examples/02_Index/OriginalImage/img.jpeg'
img = show.ReadImage(path)
img = Zoom(img,1)

show.ShowImage(img)

img = tour.DefaultDilateImage(img,kernel = np.ones((13,3)))
show.ShowImage(img)
show.SaveImage(img,'DefaultDilateImage13x3')

color_img = tour.DrawDilateContours(dilate_img=img,is_show=True)
show.SaveImage(color_img,'ColorDefaultDilateImage13x3')

'''
python3 Preprocess.py
'''