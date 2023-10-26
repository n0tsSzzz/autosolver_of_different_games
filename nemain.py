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
        if zxc[0] != [1]:
            keyboard.release(0)
            keyboard.release(1)
            keyboard.release(2)
            keyboard.release(13)
            keyboard.press(1)
            zxc[0] = [1]
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
            keys = [2, 1]
        elif 67.5 <= angle_deg < 112.5:
            kes = [1]
        elif 112.5 <= angle_deg < 157.5:
            keys = [0, 1]
        elif 157.5 <= angle_deg <= 180 or -180 <= angle_deg < -157.5:
            keys = [0]
        elif -157.5 <= angle_deg < -112.5:
            keys = [0, 13]
        elif -112.5 <= angle_deg < -67.5:
            keys = [13]
        elif -67.5 <= angle_deg < -22.5:
            keys = [2, 13]
        if keys != zxc[0]:
            print(keys, zxc[0])
            print(pos[0], pos[1], angle_deg)
            for elem in zxc[0]:
                keyboard.release(elem)
            for key in keys:
                keyboard.press(key)
            zxc[0] = keys
# while not cube_cords:
    # cube_cords = pyautogui.locateOnScreen("figure.png", grayscale=True, confidence=0.5)
    # print(1)



# def imagesearch(image, name_image: str, precision=0.8):
#     with mss.mss() as sct:
#         #im = sct.grab(sct.monitors[0])
#         im = sct.grab({'left': 0, 'top': 0, 'width': 765, 'height': 700})
#         if is_retina:
#             image.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
#         # im.save('testarea.png') #useful for debugging purposes, this will save the captured region as "testarea.png"
#         img_rgb = np.array(im)
#         img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#         template = cv2.imread(name_image, 0)
#         if template is None:
#             raise FileNotFoundError('Image file not found: {}'.format(image))
#         template.shape[::-1]

#         res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#         if max_val < precision:
#             return [-1, -1]
#         return max_loc