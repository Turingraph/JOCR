###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

from img_to_str.show import save_img_text
from include.img_process_img import img_process_img

path = [
    "/tests/00_page/img/img.jpg",
    "/tests/00_page/img_out/img_out.jpg",
]

name = ["origin", "modified"]

for i in range(len(path)):
    img = img_process_img(img = (parent + path[i])).img
    save_img_text(img=img, title=name[i])

"""
python3 Image2Text.py
"""
