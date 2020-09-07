import pyautogui
import time
import logging
import os
from collections import namedtuple
import Exceptions

import bigBoiStart
import animation
import constants
import multipleChoice
import nextLesson
import backupButtonDetection
try:
    os.remove(constants.SCROLLBAR_SCREENSHOT_NAME)
    os.remove(constants.BUTTON_DETECTION_SCREENSHOT_NAME)
except Exception:
    pass


time.sleep(2)
im = pyautogui.screenshot(constants.SCROLLBAR_SCREENSHOT_NAME, region=(1346, 71, 1359, 726))

logging.basicConfig(level=logging.DEBUG)
numSinceLastEvent = 0
checkScrollBar = 0
lastY = 0
class BackupButtonDetectionData:
    def __init__(self, active: bool, offsetX: int, offsetY: int):
        self.active = active
        self.offsetX = offsetX
        self.offsetY = offsetY

backupButtonDetectionData = BackupButtonDetectionData(False, constants.BUTTON_DETECTION_SCREENSHOT_AREA[0], 0)
while True:
    pyautogui.moveTo(100, 100)
    if animation.hasAnimation():
        numSinceLastEvent = 0
        animation.clickSpeedTextbox()
        animation.clickStart()
        animation.runAnimation()
        pyautogui.scroll(-10, x=1000, y=1000)
    elif backupButtonDetectionData.active and backupButtonDetection.hasButton(backupButtonDetectionData):
        backupButtonDetection.clickButton(backupButtonDetectionData)
        backupButtonDetection.shiftScreenshot(backupButtonDetectionData)
    elif multipleChoice.hasBubble() and not backupButtonDetectionData.active:
        numSinceLastEvent = 0
        bubbleLocation = multipleChoice.getBubbleLoc()
        multipleChoice.clickBubble()
        multipleChoice.scrollToNextBubble(bubbleLocation)
    elif bigBoiStart.hasBigBoiButton():
        loc = bigBoiStart.getBigBoiButton()
        bigBoiStart.clickBigBoiButton()
        bigBoiStart.scrollToNextBubble(loc)
    elif nextLesson.hasEnding():
        backupButtonDetectionData = BackupButtonDetectionData(False, constants.BUTTON_DETECTION_SCREENSHOT_AREA[0], 0)
        numSinceLastEvent = 0
        nextLesson.endLesson()
        nextLesson.waitForNewLesson()
    elif nextLesson.hasEndingFeedback():
        backupButtonDetectionData = BackupButtonDetectionData(False, constants.BUTTON_DETECTION_SCREENSHOT_AREA[0], 0)
        logging.info("Scrolling down")
        pyautogui.scroll(-200, x=1000, y=1000)
        logging.info("Clicked (hopefully) where hyperlink is. Since we couldn't find it")
        pyautogui.moveTo(x=1132, y=700)
        pyautogui.click()
        nextLesson.waitForNewLesson()
    else:
        logging.info("Nothing found")
        pyautogui.scroll(-200, x=1000, y=1000)
        numSinceLastEvent += 1
        if numSinceLastEvent == constants.NUM_ATTEMPTS_TIL_ERROR:
            logging.warning('may have become stuck?')
    checkScrollBar += 1
    if checkScrollBar == constants.NUM_ATTEMPTS_TIL_ERROR:
        checkScrollBar = 0
        scrollBar = pyautogui.locateOnScreen(constants.SCROLLBAR_SCREENSHOT_NAME, confidence=0.95)
        logging.info("Checking scrollbar")
        if scrollBar and not backupButtonDetectionData.active:
            backupButtonDetectionData.active = True
            logging.warning("No meaningful scrollbar progress detected, activating backup button detection")
            highestButton = multipleChoice.getBubbleLoc()
            if not highestButton:
                raise Exceptions.BackupButtonDetectionNoButton()
            backupButtonDetectionData.offsetY = highestButton.top
        else:
            os.remove(constants.SCROLLBAR_SCREENSHOT_NAME)
            im = pyautogui.screenshot(constants.SCROLLBAR_SCREENSHOT_NAME, region=(1346, 71, 1359 - 1346, 726 - 71))
            logging.info("Scrollbar progress detected")









