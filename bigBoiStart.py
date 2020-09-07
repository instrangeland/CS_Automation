import pyautogui
import logging
import time
import constants
import os
def hasBigBoiButton() -> bool:
    endOfLine = pyautogui.locateOnScreen('bigBoiStart.png', grayscale=True, confidence=0.9)
    if endOfLine:
        logging.info("Found bigBoiStart")
        return True
    else:
        return False

def clickBigBoiButton():
    logging.info("Clicking bigBoiStart")
    bigBoiStart = pyautogui.locateOnScreen('bigBoiStart.png', confidence=0.9, grayscale=True)
    if not bigBoiStart:
        logging.warning("bubble end has disappeared, skipping")
        return
    pyautogui.moveTo(bigBoiStart.left + 13, bigBoiStart.top + 8, duration=0)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.move(200, 0)

def getBigBoiButton():
    return pyautogui.locateCenterOnScreen('bigBoiStart.png', confidence=0.9, grayscale=True)

def scrollToNextBubble(buttonLocation):
    logging.info("Scrolling to next button")
    scroll = int(-(buttonLocation[0] + buttonLocation[1] -150))
    logging.debug("Bubble scroll = "+str(scroll))
    pyautogui.scroll(scroll, x=1000, y=1000)