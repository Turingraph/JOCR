###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

from ocr.img_to_str import save_ocr_text
from include.img_process_rgb import img_process_rgb

path = [
    "/tests/00_page/img/img.jpg",
    "/tests/00_page/img_out/img_out.jpg",
]

name = ["origin", "modified"]

for i in range(len(path)):
    img = img_process_rgb(img = (parent + path[i])).img
    save_ocr_text(img=img, path=name[i])