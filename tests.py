import pyautogui
import time

time.sleep(3)
bubble = pyautogui.locateOnScreen('bubble.png', confidence=0.8)
pyautogui.click(x=bubble.left + 13, y=bubble.top + 7)