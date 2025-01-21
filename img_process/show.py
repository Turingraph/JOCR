import cv2
import numpy as np
import os

def show(img: np.ndarray, title: str = "image") -> None:
    # https://stackoverflow.com/questions/74546171/image-is-too-big-for-opencv-imshow-window-how-do-i-make-it-smaller
    # https://www.geeksforgeeks.org/python-opencv-resizewindow-function/
    cv2.namedWindow(winname=title, flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winname=title, width=500, height=600)
    cv2.imshow(winname=title, mat=img)
    cv2.waitKey(delay=0)
    cv2.destroyAllWindows()

def save(
    img: np.ndarray,
    img_title: str = "Image",
    folder: str = "Image",
    fileformat: str = "jpg",
) -> None:
    # https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
    if not os.path.exists(path=folder):
        os.makedirs(name=folder)
    if fileformat[0] == ".":
        fileformat = fileformat[1:]
    # https://docs.python.org/3/library/os.path.html
    img_path = os.path.join(path = folder, paths=img_title + "." + fileformat)
    # https://numpy.org/doc/2.1/reference/generated/numpy.save.html
    np.save(file = img_path, arr = img)
