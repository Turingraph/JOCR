import cv2
import numpy as np
from img_process.show import show, save
from img_process.zoom import remove_borders, zoom, create_borders, crop
from img_process.rotate import rotate
# https://www.reddit.com/r/vscode/comments/19eqplp/python_typing_issue_unsupported_operand_types_for/?rdt=43767
from typing import Self

class img_process:
    def __init__(self, img: any):
        self.img = img
    ########################################################################################################################################################
    # read img
    # img_process/show.py

    def show(self, title: str = "img_out") -> None:
        show(img=self.img, title=title)

    def save(
        self,
        title: str = "img_out",
        folder: str = "img_out",
        fileformat: str = "jpg",
    ) -> None:
        save(img=self.img, title=title, folder=folder, fileformat=fileformat)

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
