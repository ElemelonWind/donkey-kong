import pyautogui
import pytesseract as pt
from PIL import Image
import cv2 as cv
import numpy as np
import time

# PARAMETERS:
SSX = 592
SSY = 215
SSWIDTH = 720
SSHEIGHT = 450
CELLWIDTH = 90
CELLHEIGHT = 90
CONTINUEX = 942
CONTINUEY = 580

screenshot = pyautogui.screenshot(region=(SSX, SSY, SSWIDTH, SSHEIGHT))  # Capture a specific region
pt.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# divide in 8x5 grid
gridinfo = [[0 for x in range(8)] for y in range(5)]
for y in range(5):
    for x in range(8):
        # cropped = screenshot.crop((x * CELLWIDTH, y * CELLHEIGHT, (x+1)*CELLWIDTH, (y+1)*CELLHEIGHT))
        cropped = cv.imread(f'cell_{x}_{y}.png')
        cell = np.array(cropped)
        cell = cv.imread(f'cell_{x}_{y}.png')
        hsv = cv.cvtColor(cell, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, np.array([255, 255, 245]), np.array([255, 15, 255]))
        cell[mask>0] = (0, 0, 0)
        blur = cv.blur(cell, (5, 5))
        # if cell has a number, save it in gridinfo
        data_1_char = pt.image_to_string(cell, lang='eng', config='--psm 10 -c tessedit_char_whitelist=0123456789', nice=0, output_type='string', timeout=5)
        data_2_char = pt.image_to_string(cell, lang='eng', config='--psm 13 -c tessedit_char_whitelist=0123456789', nice=0, output_type='string', timeout=5)
        data_3_char = pt.image_to_string(cell, lang='eng', config='--psm 8 -c tessedit_char_whitelist=0123456789', nice=0, output_type='string', timeout=5)
        
        if data_1_char.strip().isdigit():
            # print("1", data_1_char)
            gridinfo[y][x] = int(data_1_char)
            # print("1", data_1_char, data_2_char, data_3_char)
        elif data_2_char.strip().isdigit():
            # print("2", data_2_char)
            gridinfo[y][x] = int(data_2_char)
            # print("2", data_1_char, data_2_char, data_3_char)
        elif data_3_char.strip().isdigit():
            # print("3", data_3_char)
            gridinfo[y][x] = int(data_3_char)
            # print("3", data_1_char, data_2_char, data_3_char)

# find order to click
order = sorted([(gridinfo[y][x], x, y) for y in range(5) for x in range(8) if gridinfo[y][x] > 0], key=lambda x: x[0])
for o in order:
    pyautogui.click(SSX + o[1] * CELLWIDTH + CELLWIDTH // 2, SSY + o[2] * CELLHEIGHT + CELLHEIGHT // 2)

time.sleep(0.1)
pyautogui.click(CONTINUEX, CONTINUEY)
time.sleep(0.1)