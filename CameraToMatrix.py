#матрица из вебкамеры
from numpy import asarray
from PIL import Image
from random import randint
from ctypes import *
from cv2 import VideoCapture

Gradient = ["\033[0m\033[30m", "\033[0m\033[30m", "\033[0m\033[34m", "\033[0m\033[36m", "\033[0m\033[32m",
            "\033[0m\033[35m", "\033[0m\033[31m", "\033[0m\033[33m",
            "\033[30m\033[1m", "\033[34m\033[1m", "\033[36m\033[1m", "\033[32m\033[1m",
            "\033[35m\033[1m", "\033[31m\033[1m", "\033[33m\033[1m", "\033[37m\033[1m"]

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



SOURSE_DIR = r'C:\Users\zavgo\PycharmProjects\ImagePython\gif_kotik'
#gradient = " .:!/r(l1Z4H9W8$@" #[::-1]
#gradient = " `.;I1K#&@" #[::-1]
normalizing = 2
width = 332 #340
height = 74 #86
Sdvig_X = 0
#ii = 0

cap = VideoCapture(0)

while True:
    _, img = cap.read()

    NowImage = Image.fromarray(img)

    NowImage = NowImage.crop(Centr(NowImage.height, NowImage.width)).resize(
        [width, height]).transpose(Image.FLIP_LEFT_RIGHT)

    img = asarray(NowImage.convert('L'))
    img //= 16
    for i in img:
        for h in i:
            print(Gradient[h] + str(randint(0, 9)), end="")
        print("|")

    Coursore_to_start(0, 0)