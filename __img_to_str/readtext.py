import pytesseract
import os
from utility import path2_image


def get_img_text(img):
    # https://youtu.be/4u_wp6d_s6_g4?si=pu_v_tz_bm6vt_lt4l_xl
    img = path2_image(img)
    return pytesseract.image_to_string(img)


def print_img_text(img):
    text = get_img_text(img)
    print(text)


def save_text(
    text,
    title="text_result",
    folder="text_result",
    fileformat="txt",
    is_show=false,
):
    # https://www.w3schools.com/python/python_file_write.asp
    # https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
    if not os.path.exists(folder):
        os.makedirs(folder)
    if fileformat[0] == ".":
        fileformat = fileformat[1:]
    path = os.path.join(folder, title + "." + fileformat)
    file = open(path, "w")
    file.write(text)
    file.close()
    if is_show == true:
        print(text)


def save_img_text(
    img,
    title="textresult",
    folder="text_result",
    fileformat="txt",
    is_show=false,
):
    # https://www.w3schools.com/python/python_file_write.asp
    # https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
    text = get_img_text(img)
    save_text(
        text, title=title, folder=folder, fileformat=fileformat, is_show=is_show
    )
