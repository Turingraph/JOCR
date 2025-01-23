from ocr.flag_options import get_oem, get_psm
from ocr.img_to_str import img_to_str
#from ocr.osd import osd
from ocr.save_text import save_text
import numpy as np
from include.img_process import img_process

class ocr:
    def __init__(
            self,
            lang:str = "eng",
            psm:str|int|None = 3,
            oem:str|int|None = 3,
            timeout:int = 0,
            config:str = ''
            ):
        self.output = ''
        self.lang = lang
        self.psm = get_psm(psm)
        self.oem = get_oem(oem)
        self.timeout = timeout
        self.config = config

    def save_text(self, img:np.ndarray|img_process, path: list[str] | str = ["str_out", "str_out", "txt"]):
        if isinstance(img, img_process):
            img = img.img
        self.output = img_to_str(
            img=img,
            lang = self.lang,
            config=self.psm + ' ' + self.oem + ' ' + self.config,
            timeout=self.timeout
        )
        save_text(self.output, path)


