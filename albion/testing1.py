from PIL import ImageGrab, ImageOps
from numpy import *
from time import sleep
import pyautogui as py

POSITIONS               = []
ALREADYLOOTED_COLORSUM  = 8053
## Below 10000 should be no item ##
AVGX_DIST               = 80
AVGY_DIST               = 85
BASEX_PX_COORD          = 840
BASEY_PX_COORD          = 425

bodyX = 880
bodyY = 485


## todo: fill positions


for i in range(3):
    if i >= 1:
        bodyY += 75
        if i == 3:
            py.scroll(-1)
            bodyY = 485
        elif i == 6:
            py.scroll(1)
            bodyY = 485
    py.moveTo(bodyX,bodyY)
    sleep(2)
    print("i: " + str(i) + "  " + str(py.position()))
    for j in range(2):
        bodyX += 75
        py.moveTo(bodyX, bodyY)
        print("j: " + str(j) + "  " + str(py.position()))
        if j == 1:
            bodyX = 880

# x = 840
# y = 425
# side = 65
# box = (x,y,x+side,y+side)
# box2 = (920, 425, 920+side, 425+side)
# box3 = (840, 510, 840+side, 510+side)

# image = ImageGrab.grab(box)
# image.save('img1.png')
# gray = ImageOps.grayscale(image)
# colorArr = array(gray.getcolors())
# colorValue = colorArr.sum()

# image2 = ImageGrab.grab(box2)
# image2.save('img2.png')
# gray2 = ImageOps.grayscale(image2)
# colorArr2 = array(gray2.getcolors())
# colorValue2 = colorArr2.sum()

# image3 = ImageGrab.grab(box3)
# image3.save('img3.png')
# gray3 = ImageOps.grayscale(image3)
# colorArr3 = array(gray3.getcolors())
# colorValue3 = colorArr3.sum()


# print("slot 1: " + str(colorValue) + "\n" + "slot 2: " + str(colorValue2) + "\n" + "slot 3: " + str(colorValue3) + "\n")