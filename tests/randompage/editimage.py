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
import ImgProcess.RemoveNoise as RemoveNoise
import ImgProcess.Convolution as con
import ImgProcess.FFT as fft

from ImgProcess.Zoom import RemoveBorders,Zoom
from ImgProcess.FontSize import ThickFont
from ImgProcess.Rotation import Rotate

from ImgProcess_I.GrayImage import GrayImage

from PIL import Image
import cv2

path = [
    parent + '/Examples/01_Page/Img/img_o.jpg',
    parent + '/Examples/01_Page/Img/img_r.jpeg',
    parent + '/Examples/01_Page/ImgRand/OriginalJojoSoba.jpg',
    parent + '/Examples/01_Page/ImgRand/BinaryPx_210.jpg',
    parent + '/Examples/01_Page/ImgRand/jojomeme.jpg'
]
img_o = show.ReadImage(path[0])
img = Zoom(img_o,1.23)
img = Rotate(img)
img = GrayImage(img)
#show.ShowImage(img)

ost_img = thresh.OtsuSet0Px(img)
ost_img = thresh.BinaryPx(img,200)
#show.SaveImage(ost_img,'ost_img')

#fft_img = fft.FFTSharpen01(img,10,10)
#show.SaveImage(fft_img,'fft_img')

thick_img = ThickFont(ost_img)
thick_img = ThickFont(thick_img)
show.ShowImage(thick_img)

#fft_img = fft.FFTBlur03(ost_img,10,10)
#show.ShowImage(fft_img)

#erode_img = con.Sharpen(img)
#erode_img = ThickFont(erode_img)
#show.ShowImage(erode_img)'''

'''
python3 EditImage.py
'''