import pyautogui
import logging
import time
import constants

def hasEndingFeedback() -> bool:
    endOfLine = pyautogui.locateOnScreen('endOfLine.png', grayscale=True, confidence=0.9)
    if endOfLine:
        logging.info("Found feedback end of lesson")
        logging.info("Apparently missed ending arrow")
        return True
    else:
        return False


def hasEnding() -> bool:
    nextLesson = pyautogui.locateOnScreen('nextLesson.png', grayscale=True, confidence=0.9)
    if nextLesson:
        logging.info("Found ending of lesson")
        return True
    else:
        return False

def endLesson():

    nextLesson = pyautogui.locateOnScreen('nextLesson.png', grayscale=True, confidence=0.9)
    if not nextLesson:
        logging.warning("lesson end has disappeared, skipping")
        return
    pyautogui.click(x=nextLesson.left + 20, y=nextLesson.top + 7)

def waitForNewLesson():
    prevLesson = None
    while prevLesson is None:
        prevLesson = pyautogui.locateOnScreen('prevLesson.png', grayscale=True, confidence=0.9)