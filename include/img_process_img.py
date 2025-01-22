import cv2
import numpy as np
from include.img_process import img_process
# https://www.reddit.com/r/vscode/comments/19eqplp/python_typing_issue_unsupported_operand_types_for/?rdt=43767
from typing import Self

class img_process_img(img_process):
    def __init__(self, img: Self | np.ndarray | str):
        if type(img) == Self:
            self.img = np.copy(img.img)
        elif type(img) == str:
            self.img = cv2.imread(filename=img)
            if self.img is None:
                raise ValueError(f"Error: The file at path '{img}' could not be loaded.")
        elif type(img) == np.ndarray:
            if len(img.shape) == 3:
                self.img = np.copy(img)
            elif len(img.shape) == 2:
                self.img = cv2.cvtColor(src=img, code=cv2.COLOR_GRAY2RGB)
            else:
                raise ValueError("Error: Invalid NumPy array. len(img.shape) must be 2 or 3.")
        else:
            raise TypeError("Error: Input must be an instance of 'img_process_img', a NumPy array, or a file path.")

    def get_gray_img(self):
        return cv2.cvtColor(src=self.img, code=cv2.COLOR_RGB2GRAY)
    
    def get_color_img(self):
        return self.img
