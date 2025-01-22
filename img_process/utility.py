import cv2
import numpy as np

def inverted_image(img: np.ndarray) -> np.ndarray:
    return cv2.bitwise_not(src=img)

def odd_area(num: int) -> int:
    num = int(num)
    if num < 3:
        return 3
    else:
        if num % 2 == 1:
            return num
        else:
            return num + 1

def set_px(num: int) -> int:
    num = int(num)
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else:
        return num

def get_default_option(input: any, input_options: list, message: str) -> any:
    if input not in input_options:
        print(message)
        return input_options[0]
    else:
        return input

def get_size(
    size: int | None, max_size: int | None = None, default_size: int = 0
) -> int:
    if type(size) == int:
        if max_size == None:
            max_size = size
        if size < 0:
            return 0
        elif size > max_size:
            return max_size
        else:
            return size
    else:
        return default_size

def gray_img(img: np.ndarray) -> np.ndarray:
    if len(img.shape) == 3:
        return cv2.cvtColor(src=img, code=cv2.COLOR_RGB2GRAY)
    elif len(img.shape) == 2:
        return np.copy(img)
    else:
        raise ValueError("Error: Invalid NumPy array. len(img.shape) must be 2 or 3.")

def color_img(img: np.ndarray) -> np.ndarray:
    if len(img.shape) == 3:
        img = np.copy(img)
    elif len(img.shape) == 2:
        img = cv2.cvtColor(src=img, code=cv2.COLOR_GRAY2RGB)
    else:
        raise ValueError("Error: Invalid NumPy array. len(img.shape) must be 2 or 3.")

"""
Reference
1. Tesseract OCR Tutorial
* https://nanonets.com/blog/ocr-with-tesseract/
2. How to Open an Image in Python with PIL
* https://youtu.be/UxYJxcdLrs0?si=biuELY46TWTwhqvX

"""
