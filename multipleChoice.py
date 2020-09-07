import pyautogui
import logging
import time
import constants

def hasBubble() -> bool:
    bubble = pyautogui.locateOnScreen('bubble.png', confidence=0.9, grayscale=True)
    if bubble:
        return True
        logging.info("Has bubble")
    else:
        return False


def clickBubble():
    logging.info("Clicking bubble")
    bubble = pyautogui.locateOnScreen('bubble.png', confidence=0.9, grayscale=True)
    if not bubble:
        logging.warning("bubble end has disappeared, skipping")
        return
    pyautogui.moveTo(bubble.left + 13, bubble.top + 8, duration=0)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.move(200, 0)

def getBubbleLoc():
    return pyautogui.locateOnScreen('bubble.png', confidence=0.9, grayscale=True)

def scrollToNextBubble(bubbleLocation):
    logging.info("Scrolling to next bubble")
    scroll = int(-(bubbleLocation.top + bubbleLocation.height -150))
    logging.debug("Bubble scroll = "+str(scroll))
    pyautogui.scroll(scroll, x=1000, y=1000)

