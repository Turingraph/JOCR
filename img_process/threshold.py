import cv2
import numpy as np
from img_process.utility import set_px, get_default_option, u_odd, gray_img

message_00 = """
threshold class attribute.
1.  method = cv2.THRESH_BINARY
*	cv2.THRESH_BINARY         
*	cv2.THRESH_BINARY_INV
*	cv2.THRESH_TRUNC
*	cv2.THRESH_TOZERO
*	cv2.THRESH_TOZERO_INV
2.	thresh = None
*	if type(thresh) == int : activating customized threshold
*	if type(thresh) != int : activating Otsu threshold
3.	maxval = 255

threshold_adapt class attribute.
1.	method = cv2.THRESH_BINARY
*	cv2.THRESH_BINARY         
*	cv2.THRESH_BINARY_INV
*	cv2.THRESH_TRUNC
*	cv2.THRESH_TOZERO
*	cv2.THRESH_TOZERO_INV
2.	additional_method = cv2.ADAPTIVE_THRESH_MEAN_C
*	cv2.ADAPTIVE_THRESH_MEAN_C
*	cv2.ADAPTIVE_THRESH_GAUSSIAN_C
3.	ksize = 11
4.	constant = 2
3.	maxval = 255

Reference
*	https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576ac7e89a5e95490116e7d2082b3096b2b8
"""

message_01 = """
THRESHOLD MODE IN CV
1.  cv2.THRESH_BINARY
*   if px > thresh then px = maxval else px = 0
2.	cv2.THRESH_BINARY_INV
*	if px < thresh then px = maxval else px = 0
3.	cv2.THRESH_TRUNC
*	if px > thresh then px = thresh else px = px
4.	cv2.THRESH_TOZERO
*	if px > thresh then px = px else px = 0
5.	cv2.THRESH_TOZERO_INV
*	if px < thresh then px = px else px = 0
6.	cv2.ADAPTIVE_THRESH_MEAN_C
*	Calculating the mean value of the surround pixels within the square ksize (width=ksize) and use that mean value as the thresh
7.	cv2.ADAPTIVE_THRESH_GAUSSIAN_C
*	Calculating the "Gaussian" value of the surround pixels within the square ksize (width=ksize) and use that mean value as the thresh
8.	cv2.THRESH_OTSU
*	Consider an image with only two distinct image values (bimodal image), 
*	where the histogram would only consist of two peaks. 
*	A good threshold would be in the middle of those two values. 
*	Similarly, Otsu's method determines an optimal global threshold value from the image histogram.
*	Limitation of Otsu Method
*	1. If object ksize is much smaller compared to background ksize
*	2. Image is very noisy
*	3. Image contains ksize with different discrete intensities
*	https://youtu.be/jUUkMaNuHP8?si=QnxBvTdVhQW3VTqR

Reference
*	https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#ggaa9e58d2860d4afa658ef70a9b1115576ac7e89a5e95490116e7d2082b3096b2b8
"""

source = "Reported by img_process/threshold.py"

message_02 = (
    message_00
    + "\n"
    + "\n"
    + message_01
    + "\n"
    + "\n"
    + source
)

method_options = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
]

class threshold:
    def __init__(
        self,
        method: int = cv2.THRESH_BINARY,
        thresh: None | int = None,
        maxval: int = 255,
    ):
        self.method = get_default_option(
            input=method, 
            input_options=method_options, 
            message=message_02)
        self.thresh = None
        if type(thresh) == int:
            self.thresh = set_px(num=thresh)
        self.maxval = set_px(num=maxval)

    def edit(self, img: np.ndarray) -> np.ndarray:
        img = gray_img(img = img)
        if type(self.thresh) == int:
            return cv2.threshold(
                src=img.astype("uint8"), thresh=self.thresh, maxval=self.maxval, type=self.method
            )[1]
        else:
            return cv2.threshold(
                src=img.astype("uint8"), thresh=0, maxval=self.maxval, type=self.method + cv2.THRESH_OTSU
            )[1]


class threshold_adapt:
    def __init__(
        self,
        method: int = cv2.THRESH_BINARY,
        adaptive_method: int = cv2.ADAPTIVE_THRESH_MEAN_C,
        ksize: int = 11,
        constant: int = 2,
        maxval: int = 255,
    ):
        self.method = get_default_option(input=method, input_options=method_options, message=message_02)
        self.ksize = u_odd(num=ksize)
        self.constant = constant
        self.maxval = set_px(num=maxval)
        self.adaptive_method = get_default_option(
            input=adaptive_method,
            input_options=[cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C],
            message=message_02,
        )

    def edit(self, img: np.ndarray) -> np.ndarray:
        img = gray_img(img = img)
        return cv2.adaptiveThreshold(
            src=img,
            maxVal=self.maxval,
            adaptiveMethod=self.adaptive_method,
            thresholdType=self.method,
            blockSize=self.ksize,
            C=self.constant,
        )
