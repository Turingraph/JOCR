###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

import ReadText as read

path = [
    "/Examples/01_Page/Img/img.jpg",
    "/Examples/01_Page/ImgOut/OtsuBinaryPx.jpg",
    "/Examples/01_Page/ImgOut/ThickFont.jpg",
]

name = ["Original", "OtsuBinaryPx", "ThickFont"]

for i in range(len(path)):
    read.SaveTextFromImage(parent + path[i], name[i])

"""
python3 Image2Text.py
"""
