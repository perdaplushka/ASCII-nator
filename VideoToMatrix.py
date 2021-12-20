#матрица из видео
from numpy import asarray
from PIL import Image
from random import randint
from ctypes import *
from cv2 import VideoCapture
from pyautogui import screenshot

Gradient = ["\033[0m\033[30m", "\033[0m\033[30m", "\033[0m\033[34m", "\033[0m\033[36m", "\033[0m\033[32m",
            "\033[0m\033[35m", "\033[0m\033[31m", "\033[0m\033[33m",
            "\033[30m\033[1m", "\033[34m\033[1m", "\033[36m\033[1m", "\033[32m\033[1m",
            "\033[35m\033[1m", "\033[31m\033[1m", "\033[33m\033[1m", "\033[37m\033[1m"]
SOURSE_DIR = r'C:\Users\zavgo\PycharmProjects\ImagePython\video'
#gradient = " .:!/r(l1Z4H9W8$@" #[::-1]
#gradient = " `.;I1K#&@" #[::-1]
normalizing = 535 / 270
width = 332 #340
height = 74 #86
Sdvig_X = 0
ii = 0

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]

def Coursore_to_start(r, c):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

def Centr(image_Height, image_Width):
    if image_Height * normalizing >= image_Width:
        return [-(image_Height * normalizing - image_Width) // 2, 0, image_Height * normalizing - (image_Height * normalizing - image_Width) // 2, image_Height]
    return [0, 0, image_Width, image_Height] #не работает, нужно для вертикальных видео.

for VideoNomber in range(1, 5):
    cap = VideoCapture(SOURSE_DIR + f"/video{VideoNomber}.mp4")

    S_S_Nomber = 0
    while True:

        _, img = cap.read()

        if img is None:
            break

        NowImage = Image.fromarray(img)

        NowImage = NowImage.crop(Centr(NowImage.height, NowImage.width)).resize(
            [width, height])#.transpose(Image.FLIP_LEFT_RIGHT)

        img = asarray(NowImage.convert('L'))
        img //= 16
        #g = 0
        for i in img:
            #if g >= ii:
            for h in i:
                print(Gradient[h] + str(randint(0, 9)), end="")
            print("|")
            #g += 1


        screenshot(f"video/disko{VideoNomber}/{S_S_Nomber}.png")
        S_S_Nomber += 1

        Coursore_to_start(0, 0)
        #эффект из тиктока
        #Coursore_to_start(ii, 0)
        #ii += 1
        #if ii == len(img):
        #    break