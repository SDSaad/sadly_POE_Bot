import cv2
import numpy as np
import os
from PIL import Image, ImageGrab

img_path = r"currency_images\chaos_orb\10-chaos-orb.png"
slot_width = 49
slot_height = 49
trade_x = 327
trade_y = 224
src_width = 1920
src_height = 1080

# Stack number definition:
number_20 = cv2.imread(r"currency_images\numbers\20.png")
number_10 = cv2.imread(r"currency_images\numbers\10.png")
chaos_orb = cv2.imread(r"currency_images\currencies\chaos_orb\chaos.png")

def confere_troca_uma_vez(ini_x, ini_y, slot_width, slot_height):
    x = ini_x
    y = ini_y
    printscreen = ImageGrab.grab(bbox = (x, y, (slot_width + x), (slot_height + y))).save("printscreen.png")
    printscreen = cv2.imread("printscreen.png")
    number = cv2.matchTemplate(printscreen, chaos_orb, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    if np.amax(number) >= threshold:
        cv2.imshow('detected', printscreen)
        os.system("PAUSE")

confere_troca_uma_vez(trade_x, trade_y, slot_width, slot_height)

# def confere_troca(ini_x, ini_y, slot_width, slot_height):
#     x = ini_x
#     y = ini_y
#     currencies = []
#     while x < 950:
#         while y < 810:
#             printscreen = ImageGrab.grab(bbox = (x, y, slot_width, slot_height)).save("printscreen.png")
#             printscreen = cv2.imread("printscreen.png")
#             number = cv2.matchTemplate(printscreen, number_20, cv2.TM_CCOEFF_NORMED)
#             threshold = 0.95
#             loc = np.where(number >= threshold)





# def busca_imagem(img_path, src_width, scr_height, img_width, img_height):
#     x = 0
#     y = 0
#     count = 0
#     img_path = cv2.imread(img_path)
#     img_wid = img_width
#     img_hei = img_height
#     height_assist = img_height
#     while x < (src_width - img_wid):
#         while y < (scr_height - img_hei):
#             printscreen = ImageGrab.grab(bbox =(x, y, img_width, img_height)).save("printscreen.png")
#             printscreen = cv2.imread("printscreen.png")
#             if img_path.shape == printscreen.shape:
#                 diff = cv2.subtract(img_path, printscreen)
#                 b, g, r = cv2.split(diff)
#                 if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) and cv2.countNonZero(r):
#                     count += 1
#             y += 1
#             print(y)
#             img_height += 1
#         x += 1
#         print(x)
#         img_width += 1
#         y = 0
#         img_height = height_assist
#     return count

# chaos = busca_imagem(img_path, src_width, src_height, img_width, img_height)
# print(chaos)