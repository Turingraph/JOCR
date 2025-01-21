import pytesseract
import os
import numpy as np
import cv2

def get_img_text(img:str|np.ndarray) -> str:
    if type(img) == str:
        img = cv2.imread(filename=img)
    return pytesseract.image_to_string(image=img)

def save_text(
    text:str,
    title:str="text_result",
    folder:str="text_result",
    fileformat:str="txt",
    is_show:bool=False,
)-> None:
    # https://www.w3schools.com/python/python_file_write.asp
    # https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
    if not os.path.exists(path=folder):
        os.makedirs(name=folder)
    if fileformat[0] == ".":
        fileformat = fileformat[1:]
    path = os.path.join(a=folder, path=title + "." + fileformat)
    file = open(file=path, mode="w")
    file.write(s=text)
    file.close()
    if is_show == True:
        print(values=text)


def save_img_text(
    img:np.ndarray,
    title:str="textresult",
    folder:str="text_result",
    fileformat:str="txt",
    is_show:bool=False,
) -> None:
    # https://www.w3schools.com/python/python_file_write.asp
    # https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
    text = get_img_text(img=img)
    save_text(
        text=text, title=title, folder=folder, fileformat=fileformat, is_show=is_show
    )
