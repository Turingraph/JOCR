import numpy as np
from ImgProcess_I.GrayImage import GrayImage
from ImgProcess_I.Image import Image
from ImgProcess.Contour import DetectContourImg


class TableImage:
    def __init__(
        self,
        img: np.ndarray,
        threshold_px: None | int = None,
        kernel: np.ndarray = np.ones((2, 30)),
        kernel_area: int = 9,
    ):
        self.img = Image(img)
        self.dilate_img = DetectContourImg(
            self.img, threshold_px, kernel, kernel_area
        )
