from include.img_process_gray import img_process_gray
from include.img_process_rgb import img_process_rgb
from include.img_process import img_process
from img_process.utility import check_img, get_rgb, get_size, rgb_img
from img_process.contour import get_contours, sort_contours
import numpy as np
import cv2
import copy

class boxes_img:
    def __init__(self, 
                img: img_process| np.ndarray | str,
                thresh_px: int = 0,
                kernel: np.ndarray = np.ones(shape=(2, 30)),
                ksize: int = 9):
        if type(img) == img_process:
            img = img.img
        elif type(img) == str:
            img = cv2.imread(filename=img)
            if img is None:
                raise ValueError(f"Error: The file at path '{img}' could not be loaded.")
        elif type(img) == np.ndarray:
            img = check_img(img)
        else:
            raise TypeError("Error: Input img must be img_process, np.ndarray or str")
        self.origin_img = img_process_rgb(img = rgb_img(img))
        self.marked_img = copy.deepcopy(self.origin_img)
        img = img_process_gray(img=img)
        img.contour_img(
            thresh_px=thresh_px,
            kernel=kernel,
            ksize=ksize)
        self.dilate_img = img
        self.all_boxes = get_contours(img=self.dilate_img.img)
        self.boxes = []
        # self.multi_ocr = ''
        # self.one_ocr = ''

    def select_boxes(
            self, 
            min_w:int = 0,
            max_w:int|None = None,
            min_h:int = 0,
            max_h:int|None = None,
            ) -> None:
        min_w = get_size(size=min_w, maxval=self.marked_img.img.shape[1])
        min_h = get_size(size=min_h, maxval=self.marked_img.img.shape[0])
        max_w = get_size(size=max_w, maxval=self.marked_img.img.shape[1],default_size=self.marked_img.img.shape[1])
        max_h = get_size(size=max_h, maxval=self.marked_img.img.shape[0],default_size=self.marked_img.img.shape[0])
        self.all_boxes = get_contours(img=self.dilate_img.img)
        self.boxes = []
        for i in self.all_boxes:
            x, y, w, h = cv2.boundingRect(i)
            if ((w > min_w and h > min_h) 
                and (w < max_w and h < max_h)):
                self.boxes.append(i)

    def sort_boxes(self, reverse: bool = False, method: int = 4)->None:
        self.boxes = sort_contours(contour=self.boxes, reverse=reverse, method=method)

    def show_boxes(self,
            rgb:list[int]|int|None = None, title:str="boxes_img.show_boxes()"
            ) -> None:
        self.marked_img = copy.deepcopy(self.origin_img)
        for i in self.boxes:
            x, y, w, h = cv2.boundingRect(i)
            self.marked_img.rectangle(rgb=rgb,x=x, y=y, w=w, h=h)
        self.marked_img.show(title=title)

    def get_boxes(self) -> list:
        out_img_arr = []
        for i in self.boxes:
            x, y, w, h = cv2.boundingRect(i)
            out_img = self.origin_img.img[y:y + h, x:x + w]
            out_img = img_process_rgb(img = out_img)
            out_img_arr.append(out_img)
        return out_img_arr

    def save_boxes(self,path: list[str] | str = ["img_out", "img_out", "jpg"]) -> list:
        count = 0
        if isinstance(path, str):
            path = ["img_out", path, "jpg"]
        for i in self.boxes:
            x, y, w, h = cv2.boundingRect(i)
            out_img = self.origin_img.img[y:y + h, x:x + w]
            out_img = img_process_rgb(img = out_img)
            count_stars = str(count)
            if count < 10:
                count_stars = '0' + count_stars
            out_img.save_img(path=[path[0], path[1]+"_" + count_stars, path[2]])
            count += 1

    # def ocr(self):
    #     for i in self.boxes:
    #         out_img = self.origin_img.img[y:y + h, x:x + w]