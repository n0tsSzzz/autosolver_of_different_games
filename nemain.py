import time
from PIL import Image
import pyautogui
import keyboard
from python_imagesearch.imagesearch import imagesearch
import math
import numpy as np
import math


zxc = [[4]] 
j = 1
# while True:
#     main_img = Image.open('main_figure.png')
#     main_pos = imagesearch(main_img, 'main_figure.png')
#     print(main_pos)

# while True:
#     img = Image.open('figure.png')
#     pos = imagesearch(img, 'figure.png')
#     print(pos)

while True:
    img = Image.open('figure.png')
    pos = imagesearch(img, 'figure.png')

    if pos[0] == -1:
        print(f"main_image not found {j}")
        #print(main_pos[0], main_pos[1], pos[0], pos[1])
        j += 1
        continue
    else:
        dx = pos[0] - 704
        dy = pos[1] - 795

        angle_rad = math.atan2(dy, dx)
        angle_deg = angle_rad * 180 / math.pi

        if -22.5 <= angle_deg < 22.5:
            keys = [2]
        elif 22.5 <= angle_deg < 67.5:
            keys = [2, 13]
        elif 67.5 <= angle_deg < 112.5:
            kes = [13]
        elif 112.5 <= angle_deg < 157.5:
            keys = [0, 13]
        elif 157.5 <= angle_deg <= 180 or -180 <= angle_deg < -157.5:
            keys = [0]
        elif -157.5 <= angle_deg < -112.5:
            keys = [0, 1]
        elif -112.5 <= angle_deg < -67.5:
            keys = [1]
        elif -67.5 <= angle_deg < -22.5:
            keys = [2, 1]
        if keys != zxc[0]:
            print(keys, zxc[0])
            print(pos[0], pos[1], angle_deg)
            for elem in zxc[0]:
                keyboard.release(elem)
            for key in keys:
                keyboard.press(key)
# while not cube_cords:
    # cube_cords = pyautogui.locateOnScreen("figure.png", grayscale=True, confidence=0.5)
    # print(1)

