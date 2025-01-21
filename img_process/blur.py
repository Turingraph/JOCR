import cv2
import numpy as np
from utility import odd_kernel_area

def mean_blur(
        img: np.ndarray, 
        kernel_area: int = 15, 
        scalar: None | int | float = None
    ) -> np.ndarray:
    # Update each pixel value to average pixel value with in the kernel_area to Blur image
    kernel_area = odd_kernel_area(num=kernel_area)
    if scalar == None:
        scalar = (1 / kernel_area) ** 2
    kernel = scalar * np.ones(shape=(kernel_area, kernel_area))
    # https://youtu.be/KuXjwB4LzSA?si=mt-leKGKjpMnJGfg
    # https://www.geeksforgeeks.org/python-opencv-filter2d-function/
    return cv2.filter2D(
        src=img, 
        ddepth=-1, 
        kernel=kernel
    )

def gauss_blur(
        img: np.ndarray, 
        kernel_area: int = 15
    ) -> np.ndarray:
    # Blur the image based in the pixel with in kernel_area using Gaussian function
    # https://www.geeksforgeeks.org/python-image-blurring-using-opencv/
    kernel_area = odd_kernel_area(kernel_area)
    return cv2.GaussianBlur(src=img, ksize=(kernel_area, kernel_area), float=0)

def bilateral_blur(
    img: np.ndarray, kernel_area: int = 15, effect: int = 75
) -> np.ndarray:
    # Remove the noise and preserve the edge.
    # https://youtu.be/LjbYKWAQA5s?si=1br6Rl9OYkTZQPJB
    # https://www.tutorialspoint.com/opencv/opencv_bilateral_filter.htm
    kernel_area = odd_kernel_area(kernel_area)
    return cv2.bilateralFilter(
        src=img, d=kernel_area, sigmaColor=effect, sigmaSpace=effect
    )
