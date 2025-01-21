import cv2
import numpy as np
from utility import odd_kernel_area, get_default_option


def get_contours(dilate_img: np.ndarray) -> list:
    contours, hierarchy = cv2.findContours(
        image=dilate_img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE
    )
    return contours


def detect_contour_img(
    img: np.ndarray,
    threshold_px: None | int = None,
    kernel: np.ndarray = np.ones(shape=(2, 30)),
    kernel_area: int = 9,
) -> np.ndarray:
    kernel_area = odd_kernel_area(num=kernel_area)
    img = cv2.GaussianBlur(src=img, ksize=(kernel_area, kernel_area), sigmaY=0)
    if threshold_px != None:
        img = cv2.threshold(
            src=img, thresh=threshold_px, maxval=255, type=cv2.THRESH_BINARY
        )[1]
    img = cv2.threshold(
        src=img,
        thresh=0,
        maxval=255,
        type=cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU,
    )[1]
    img = cv2.dilate(src=img, kernel=kernel, iterations=1)
    return img


def sort_contours(
    contour: list, is_reverse: bool = False, method: int = 4
) -> list:
    message = """
    method: str | int = 4
    * 0 = x
    * 1 = y
    * 2 = width
    * 3 = height
    * 4 = size
    """
    method = get_default_option(
        input=method, input_options=[4, 0, 1, 2, 3], message=message
    )
    if method in [0, 1, 2, 3]:
        return sorted(
            iterate=contour,
            key=lambda x: cv2.boundingRect(array=x)[method],
            reverse=is_reverse,
        )
    return sorted(
        iterate=contour,
        key=lambda x: cv2.contourArea(array=x),
        reverse=is_reverse,
    )
