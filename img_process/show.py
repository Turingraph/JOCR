import cv2
import numpy as np
from PIL import Image 
import os

def Show(img:np.ndarray, title:str = 'image'):
    # https://stackoverflow.com/questions/74546171/image-is-too-big-for-opencv-imshow-window-how-do-i-make-it-smaller
    # https://www.geeksforgeeks.org/python-opencv-resizewindow-function/
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 500, 600)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Save(img:np.ndarray, img_title:str = 'Image', folder:str = 'Image', fileformat:str = 'jpg'):
    # https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
    if not os.path.exists(folder):
        os.makedirs(folder)
    if fileformat[0]=='.':
        fileformat = fileformat[1:]
    img_path = os.path.join(folder,img_title+'.'+fileformat)
    img.save(img_path)
