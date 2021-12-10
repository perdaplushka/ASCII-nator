from ctypes import *
import cv2

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]

def Coursore_to_start(r, c):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

def Centr(image_Height, image_Width):
    if image_Height * 1.92 >= image_Width:
        return [-(image_Height * 1.92 - image_Width) // 2, 0, image_Height * 1.92 - (image_Height * 1.92 - image_Width) // 2, image_Height]
    return [0, 0, image_Width, image_Height] #не работает, нужно для горизонтальных видео.


import numpy as np
from PIL import Image

SOURSE_DIR = r'C:\Users\zavgo\PycharmProjects\ImagePython\gif_kotik'
#gradient = " .:!/r(l1Z4H9W8$@" #[::-1]
gradient = " `.;I1K#&@" #[::-1]
normalizing = 2
width = 338 #340
height = 82 #86
Sdvig_X = 0
ii = 0

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    NowImage = Image.fromarray(img)

    NowImage = NowImage.crop(Centr(NowImage.height, NowImage.width)).resize(
        [width, height]).transpose(Image.FLIP_LEFT_RIGHT)

    img = np.asarray(NowImage.convert('L'))
    img //= 26
    for i in img:
        for h in i:
            print(gradient[h], end="")
        print("|")
    Coursore_to_start(0, 0)
    ii += 1

