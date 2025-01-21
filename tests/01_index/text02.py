###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

from ColumnSegmentation import ColumnSegmentation
import ImgProcess.Show as show

path = "/Users/imac/Desktop/JOCR_SOBA/exPyDH02_Index/OriginalImage/img.jpeg"
img = show.ReadImage(path)
ColumnSegmentation(
    img,
    width=20,
    height=200,
    is_show=True,
    img_title="ColumnSegmentation",
    is_multiple_imgs=True,
)
"""
python3 text02.py
"""
