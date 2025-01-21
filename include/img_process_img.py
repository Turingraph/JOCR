import cv2
import numpy as np
from img_process.show import show, save
from img_process.zoom import remove_borders, zoom, create_borders, crop
from img_process.rotate import rotate

class img_process_img:
    def __init__(self, img: np.ndarray | str):
        if type(img) == str:
            self.img = cv2.imread(filename=img)
        elif len(img.shape) == 3:
            self.img = np.copy(a=img)
        elif len(img.shape) == 2:
            self.img = cv2.cvtColor(src=img, code= cv2.COLOR_GRAY2RGB)
        else:
            print(values="Error: the input img is invalid.")
            print(
                values="len(img.shape) in [2, 3] or type(img) == str should be true."
            )
            print(
                values="Reported by include/img_process_img.py/class img_process_img/def __init__()"
            )

    ########################################################################################################################################################
    # read img
    # img_process/show.py

    def get_img(self) -> np.ndarray:
        return self.img

    def get_color_img(self) -> np.ndarray:
        return img_process_img(img=self.img)

    def show(self, title: str = "image") -> None:
        show(img=self.img, title=title)

    def save(
        self,
        img_title: str = "image",
        folder: str = "image",
        fileformat: str = "jpg",
    ) -> None:
        save(img=self.img, img_title=img_title, folder=folder, fileformat=fileformat)

    def shape(self) -> tuple:
        return self.img.shape

    ########################################################################################################################################################
    # edit img
    # img_process/(zoom.py, rotate.py)

    def zoom(self, zooms: int = 1) -> None:
        self.img = zoom(img=self.img, zoom=zooms)

    def remove_borders(self) -> None:
        self.img = remove_borders(img=self.img)

    def crop(
        self,
        x: int | None = None,
        y: int | None = None,
        width: int | None = None,
        height: int | None = None,
    ) -> None:
        self.img = crop(img=self.img, x=x, y=y, width=width, height=height)

    def create_borders(self, size: int = 50) -> None:
        self.img = create_borders(img=self.img, size=size)

    def rotate(self, angle: int | None = None) -> None:
        self.img = rotate(img=self.img, angle=angle)
