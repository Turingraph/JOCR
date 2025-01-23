###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

import img_to_str.img_to_str as shw
from img_to_str.ReadColumn import SaveColumnText, SaveMultiColumnText

path = parent + "/Examples/02_Index/OriginalImage/img.jpeg"

ocrout = SaveMultiColumnText(
    path,
    width_and_height=[[20, 200]],
    is_show=True,
    title="TextFromImgWithColumns01",
)
ocrout = str(ocrout)
read.SaveText(ocrout, "textresult02")
