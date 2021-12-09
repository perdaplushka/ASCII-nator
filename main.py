from ctypes import *
import cv2

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]

def Coursore_to_start(r, c):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))



import numpy as np
from PIL import Image, ImageChops

SOURSE_DIR = r'C:\Users\zavgo\PycharmProjects\ImagePython\gif_kotik'
gradient = " .:!/r(l1Z4H9W8$@" #[::-1]
normalizing = 2
width = 338 #340
height = 82 #86
Sdvig_X = 0
ii = 0

cap = cv2.VideoCapture(0)

while True:
    a, img = cap.read()

    NowImage = Image.fromarray(img)

    NowImage = NowImage.crop([0 + Sdvig_X, 0, NowImage.height * 1.92 + Sdvig_X, NowImage.height]).resize(
        [width, height])

    img = np.asarray(NowImage.convert('L'))
    img //= 16
    for i in img:
        for h in i:
            print(gradient[h], end="")
        print("|")
    print(Sdvig_X)
    Coursore_to_start(0, 0)
    ii += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
