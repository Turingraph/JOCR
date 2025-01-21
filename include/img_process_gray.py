import cv2
import numpy as np
from img_process.img_process_img import img_process_img
from img_process.blur import mean_blur, gauss_blur, bilateral_blur
from img_process.morphology import (
    thin_font,
    thick_font,
    remove_noise,
    dilate,
    erode,
    opening,
    canny,
)
from img_process.contour import detect_contour_img
from img_process.threshold import threshold, adaptive_threshold
from img_process.kernel2d import sharp_kernel2d
from img_process.fft2d import fft_blur, fft_sharp, get_fft, get_fft_image
from img_process.utility import inverted_image


class GrayImage(img_process_img):
    def __init__(self, img):
        self.img = img
        super().__init__(self.img)
        if type(img) == str:
            self.img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
        elif len(img.shape) == 3:
            self.img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif len(img.shape) == 2:
            self.img = np.copy(img)
        else:
            print("Error: the input img is invalid.")
            print(
                "len(img.shape) in [2, 3] or type(img) == str should be true."
            )
            print(
                "Reported by ImageProcessing_Biew / GrayImage.py / class GrayImage / def __init__(self, img)"
            )

    ########################################################################################################################################################
    # Morphology.py

    def RemoveNoice(self):
        self.img = RemoveNoise(self.img)

    def ThinFont(self):
        self.img = ThinFont(self.img)

    def ThickFont(self):
        self.img = ThickFont(self.img)

    def Dilate(self, kernel: np.ndarray = np.ones((5, 5), np.uint8)):
        self.img = Dilate(self.img, kernel)

    def Erode(self, kernel: np.ndarray = np.ones((5, 5), np.uint8)):
        self.img = Erode(self.img, kernel)

    def Opening(self, kernel: np.ndarray = np.ones((5, 5), np.uint8)):
        self.img = Opening(self.img, kernel)

    def Canny(self, c1: int = 100, c2: int = 200):
        self.img = Canny(self.img, c1, c2)

    def DetectContourImg(
        self,
        threshold_px: None | int = None,
        kernel: np.ndarray = np.ones((2, 30)),
        kernel_area: int = 9,
    ):
        self.img = DetectContourImg(
            self.img,
            threshold_px,
            kernel,
            kernel_area,
        )

    ########################################################################################################################################################
    # Threshold.py

    def Threshold(
        self,
        method: int = cv2.THRESH_BINARY,
        threshold_px: int | None = None,
        max_px: int = 255,
    ):
        transformation = Threshold(method, threshold_px, max_px)
        self.img = transformation.Edit(self.img)

    def AdaptiveThreshold(
        self,
        method: int = cv2.THRESH_BINARY,
        adaptive_method: int = cv2.ADAPTIVE_THRESH_MEAN_C,
        kernel_area: int = 11,
        constant: int = 2,
        max_px: int = 255,
    ):
        transformation = AdaptiveThreshold(
            method, adaptive_method, kernel_area, constant, max_px
        )
        self.img = transformation.Edit(self.img)

    ########################################################################################################################################################
    # Kernel2D.py

    def SharpFilter2D(
        self, ls: list[float] = [-0.1, -5], center_px: int | None = None
    ):
        kernel2d = SharpKernel2D(ls, center_px)
        self.img = cv2.filter2D(self.img, -1, kernel2d)

    ########################################################################################################################################################
    # Blur.py

    def MeanBlur(self, kernel_area: int = 15, scalar: None | int = None):
        self.img = MeanBlur(self.img, kernel_area, scalar)

    def GaussBlur(self, kernel_area: int = 15):
        self.img = GaussBlur(self.img, kernel_area)

    def BilateralBlur(self, kernel_area: int = 15, effect: int = 75):
        self.img = BilateralBlur(self.img, kernel_area, effect)

    ########################################################################################################################################################
    # FFT2D.py

    def FFTBlur(
        self, row: int, col: int, freq: int = 0, mode: int = cv2.MORPH_RECT
    ):
        self.img = FFTBlur(self.img, row, col, freq=freq, mode=mode)

    def FFTSharp(
        self, row: int, col: int, freq: int = 0, mode: int = cv2.MORPH_RECT
    ):
        self.img = FFTSharp(self.img, row, col, freq=freq, mode=mode)

    def GetFFT(self):
        return GetFFT(self.img)

    def GetFFTImage(self):
        return GrayImage(GetFFTImage(self.img))

    def GetFFTArray(self):
        return GetFFTImage(self.img)

    ########################################################################################################################################################
    # ImageUtility.py

    def InvertedImage(self):
        self.img = InvertedImage(self.img)
