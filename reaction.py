import pyautogui
import time

time.sleep(5)

# Get the current mouse position
x, y = pyautogui.position()

count = 0
while count < 10:

    # Get the pixel color at the mouse position
    if pyautogui.pixel(x, y) == (206, 38, 54):
        continue
    
    # print(pyautogui.pixel(x, y))
    pyautogui.click(x, y)
    count += 1