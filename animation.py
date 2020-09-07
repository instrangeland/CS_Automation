import logging
import time
import constants
import pyautogui

from Exceptions import UnclickableException


def hasAnimation() -> bool:
    find2xSpeedCheck = pyautogui.locateOnScreen('check.png', confidence=0.9)
    if find2xSpeedCheck:
        return True
    else:
        return False

def clickSpeedTextbox():
    pyautogui.scroll(-40)
    find2xSpeedCheck = 0
    clickAttempts = 0
    while find2xSpeedCheck is not None:
        find2xSpeedCheck = pyautogui.locateOnScreen('check.png', confidence=0.9)
        if find2xSpeedCheck is None:
            logging.warning("function could not find animation for some reason")
            return
        logging.info("Found checkbox, clicking")
        clickAttempts += 1
        pyautogui.moveTo(find2xSpeedCheck.left + 5, find2xSpeedCheck.top + 5, duration=0)
        pyautogui.click()
        time.sleep(.4)
        find2xSpeedCheck = pyautogui.locateOnScreen('check.png', confidence=0.9)
        if find2xSpeedCheck:
            logging.info("Textbox Unclicked, on attempt " + clickAttempts)
        if clickAttempts == constants.NUM_ATTEMPTS_TIL_ERROR:
            logging.error("Textbox clicking not working")
            raise UnclickableException


def clickStart():
    start = pyautogui.locateOnScreen('start.png', grayscale=True, confidence=0.9)
    pyautogui.click(x=start.left + 20, y=start.top + 10)



def runAnimation():
    rightArrow = None
    reverseArrow = None
    while reverseArrow is None:
        rightArrow = None
        while rightArrow is None and reverseArrow is None:
            reverseArrow = pyautogui.locateOnScreen('backArrow.png', confidence=0.9)
            rightArrow = pyautogui.locateOnScreen('rightArrow.png', grayscale=True, confidence=0.9)
            time.sleep(0.4)
        if reverseArrow is None:
            print(rightArrow)
            pyautogui.click(x=rightArrow.left + 5, y=rightArrow.top + 5)
            pyautogui.moveRel(0, 40, duration=0)