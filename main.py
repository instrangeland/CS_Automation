import pyautogui
import cv2
import time

while True:
    find2xSpeedCheck = None
    pyautogui.PAUSE = 0.2
    pyautogui.moveTo(x=200, y=500)
    while find2xSpeedCheck is None:
        for bubble in pyautogui.locateAllOnScreen('bubble.png', confidence=0.8):
            pyautogui.click(x=bubble.left + 13, y=bubble.top + 7)
        time.sleep(0.1)
        for bubble in pyautogui.locateAllOnScreen('otherBubble.png', confidence=0.8):
            pyautogui.click(x=bubble.left + 13, y=bubble.top + 7)
            print("hi")
        endOfLine = pyautogui.locateOnScreen('endOfLine.png', grayscale=True, confidence=0.9)
        if endOfLine is not None:
            pyautogui.click(x = 1309, y = 43)
        nextLesson = pyautogui.locateOnScreen('nextLesson.png', grayscale=True, confidence=0.9)
        if nextLesson is not None:
            pyautogui.click(x=nextLesson.left + 20, y=nextLesson.top + 7)
            prevLesson = None
            while prevLesson is None:
                prevLesson = pyautogui.locateOnScreen('prevLesson.png', grayscale=True, confidence=0.9)
        bubbleCheck = pyautogui.locateOnScreen('bubble.png', confidence=0.8)
        find2xSpeedCheck = pyautogui.locateOnScreen('check.png', grayscale=True, confidence=0.9)
        wrongNotAnswer = pyautogui.locateOnScreen('wrongNotAnswer.png', grayscale=True, confidence=0.9)
        if find2xSpeedCheck is None and (wrongNotAnswer is None or bubbleCheck is None):
            pyautogui.press('pagedown')
    pyautogui.scroll(-10, x=1000, y=1000)
    find2xSpeedCheck = pyautogui.locateOnScreen('check.png')
    pyautogui.moveTo(find2xSpeedCheck.left + 5, find2xSpeedCheck.top + 5, duration=0)  #
    pyautogui.click()

    start = pyautogui.locateOnScreen('start.png', grayscale=True, confidence=0.9)
    pyautogui.click(x=start.left + 20, y=start.top + 10)

    right = None
    reverse = None
    while reverse is None:
        right = None
        while right is None and reverse is None:
            reverse = pyautogui.locateOnScreen('backArrow.png', confidence=0.9)
            right = pyautogui.locateOnScreen('rightArrow.png', grayscale=True, confidence=0.9)
            time.sleep(0.4)
        if reverse is None:
            print(right)
            pyautogui.click(x=right.left + 5, y=right.top + 5)
            pyautogui.moveRel(0, 40, duration=0)
