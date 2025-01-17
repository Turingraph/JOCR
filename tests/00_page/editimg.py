###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

from ImgProcess_I.GrayImage import GrayImage
import cv2

path = parent + '/Examples/01_Page/Img/img.jpg'

img = GrayImage(path)
img.Zoom(-1.23)
img.Rotate()
img.Threshold()
img.Show()

'''
python3 EditImage.py
'''