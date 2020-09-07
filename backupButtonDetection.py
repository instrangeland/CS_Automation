import pyautogui
import logging
import time
import constants
import os

def getLocalScreenshotArea(backupButtonDetectionData):
    localScreenshotArea = constants.BUTTON_DETECTION_SCREENSHOT_AREA
    differenceInHeight = backupButtonDetectionData.offsetY - localScreenshotArea[1]
    localScreenshotArea = list(localScreenshotArea)
    localScreenshotArea[1] = backupButtonDetectionData.offsetY
    localScreenshotArea[3] -= differenceInHeight
    localScreenshotArea = tuple(localScreenshotArea)
    return localScreenshotArea

def shiftScreenshot(backupButtonDetectionData):
    backupButtonDetectionData.offsetY += 30


def getButtonCoord(backupButtonDetectionData):
    topButton = pyautogui.locate('bubble.png', constants.BUTTON_DETECTION_SCREENSHOT_NAME)
    logging.info("Got location at "+str(pyautogui.center(topButton)))
    return pyautogui.center(topButton)

def hasButton(backupButtonDetectionData) -> bool:
    if not backupButtonDetectionData.active:
        return False
    else:
        localScreenshotArea = getLocalScreenshotArea(backupButtonDetectionData)
        try:
            os.remove(constants.BUTTON_DETECTION_SCREENSHOT_NAME)
        except Exception:
            pass
        pyautogui.screenshot(constants.BUTTON_DETECTION_SCREENSHOT_NAME, region=localScreenshotArea)
        topButton = pyautogui.locate('bubble.png', constants.BUTTON_DETECTION_SCREENSHOT_NAME)
        if topButton:
            logging.info("Backup button detection: found button")
            return True
        else:
            return False

def clickButton(backupButtonDetectionData):
    topButton = pyautogui.locate('bubble.png', constants.BUTTON_DETECTION_SCREENSHOT_NAME)
    centered = pyautogui.center(topButton)
    y = centered.y + backupButtonDetectionData.offsetY
    x = centered.x + backupButtonDetectionData.offsetX
    pyautogui.moveTo(x, y)
    pyautogui.click()

