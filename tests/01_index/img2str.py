###############################################################################################################

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
parent = os.path.dirname(parent)
sys.path.append(parent)

###############################################################################################################

import ReadText as read
from ReadColumn import SaveColumnText, SaveMultiColumnText

path = parent + "/Examples/02_Index/OriginalImage/img.jpeg"

ocrout = SaveMultiColumnText(
    path,
    width_and_height=[[20, 200]],
    is_show=True,
    title="TextFromImgWithColumns01",
)
ocrout = str(ocrout)
read.SaveText(ocrout, "textresult02")

"""
python3 Main.py
"""
