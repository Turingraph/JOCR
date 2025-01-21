import cv2
import numpy as np
from include.img_process_img import img_process_img
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
from img_process.threshold import threshold, threshold_adapt
from img_process.kernel_2d import sharp_kernel_2d
from img_process.fft_2d import fft_blur, fft_sharp, get_fft, get_fft_image
from img_process.utility import inverted_image


class img_process_gray(img_process_img):
    def __init__(self, img:np.ndarray | str):
        self.img = img
        super().__init__(self.img)
        if type(img) == str:
            self.img = cv2.cvtColor(src=cv2.imread(img), code=cv2.COLOR_BGR2GRAY)
        elif len(img.shape) == 3:
            self.img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
        elif len(img.shape) == 2:
            self.img = np.copy(a=img)
        else:
            print(values="Error: the input img is invalid.")
            print(
                values="len(img.shape) in [2, 3] or type(img) == str should be true."
            )
            print(
                values="Reported by include/img_process_gray.py/class img_process_gray/def __init__()"
            )

    ########################################################################################################################################################
    # img_process/morphology.py

    def remove_noice(self) -> None:
        self.img = remove_noise(img=self.img)

    def thin_font(self) -> None:
        self.img = thin_font(img=self.img)

    def thick_font(self) -> None:
        self.img = thick_font(img=self.img)

    def dilate(self, kernel: np.ndarray = np.ones(shape=(5, 5), dtype= np.uint8)) -> None:
        self.img = dilate(img=self.img, kernel= kernel)

    def erode(self, kernel: np.ndarray = np.ones(shape=(5, 5), dtype=np.uint8)) -> None:
        self.img = erode(img=self.img, kernel=kernel)

    def opening(self, kernel: np.ndarray = np.ones(shape=(5, 5), dtype=np.uint8)) -> None:
        self.img = opening(img=self.img, kernel=kernel)

    def canny(self, c1: int = 100, c2: int = 200) -> None:
        self.img = canny(img=self.img, c1=c1, c2=c2)

    def detect_contour_img(
        self,
        threshold_px: None | int = None,
        kernel: np.ndarray = np.ones(shape=(2, 30)),
        kernel_area: int = 9,
    ) -> None:
        self.img = detect_contour_img(
            img=self.img,
            threshold_px=threshold_px,
            kernel=kernel,
            kernel_area=kernel_area,
        )

    ########################################################################################################################################################
    # img_process/threshold.py

    def threshold(
        self,
        method: int = cv2.THRESH_BINARY,
        threshold_px: int | None = None,
        max_px: int = 255,
    ) -> None:
        transformation = threshold(method=method, threshold_px=threshold_px, max_px=max_px)
        self.img = transformation.edit(img=self.img)

    def threshold_adapt(
        self,
        method: int = cv2.THRESH_BINARY,
        adaptive_method: int = cv2.ADAPTIVE_THRESH_MEAN_C,
        kernel_area: int = 11,
        constant: int = 2,
        max_px: int = 255,
    ) -> None:
        transformation = threshold_adapt(
            method=method, adaptive_method=adaptive_method, kernel_area=kernel_area, constant=constant, max_px=max_px
        )
        self.img = transformation.edit(img=self.img)

    ########################################################################################################################################################
    # img_process/kernel_2D.py

    def sharp_filter2d(
        self, ls: list[float] = [-0.1, -5], center_px: int | None = None
    ) -> None:
        kernel2d = sharp_kernel_2d(ls=ls, center_px=center_px)
        self.img = cv2.filter2D(src=self.img, ddepth=-1, kernel=kernel2d)

    ########################################################################################################################################################
    # img_process/blur.py

    def mean_blur(self, kernel_area: int = 15, scalar: None | int = None) -> None:
        self.img = mean_blur(img=self.img, kernel_area=kernel_area, scalar=scalar)

    def gauss_blur(self, kernel_area: int = 15) -> None:
        self.img = gauss_blur(img=self.img, kernel_area=kernel_area)

    def bilateral_blur(self, kernel_area: int = 15, effect: int = 75) -> None:
        self.img = bilateral_blur(img=self.img, kernel_area=kernel_area, effect=effect)

    ########################################################################################################################################################
    # img_process/fft_2d.py

    def fft_blur(
        self, row: int, col: int, freq: int = 0, mode: int = cv2.MORPH_RECT
    ) -> None:
        self.img = fft_blur(img=self.img, row=row, col= col, freq=freq, mode=mode)

    def fft_sharp(
        self, row: int, col: int, freq: int = 0, mode: int = cv2.MORPH_RECT
    ) -> None:
        self.img = fft_sharp(img=self.img, row=row, col=col, freq=freq, mode=mode)

    def get_fft(self) -> np.ndarray:
        return get_fft(img=self.img)

    # https://stackoverflow.com/questions/61636701/is-there-a-way-in-a-class-function-to-return-an-instance-of-the-class-itself
    def get_fft_image(self) -> "img_process_gray":
        return img_process_gray(img=get_fft_image(img=self.img))

    def get_fft_array(self) -> np.ndarray:
        return get_fft_image(img=self.img)

    ########################################################################################################################################################
    # img_process/utility.py

    def inverted_image(self) -> None:
        self.img = inverted_image(img=self.img)
