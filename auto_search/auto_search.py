import pyautogui
import time
import random
from util.util import click, refresh

chrome = [540, 420]
safari = [540, 440]


# Although there are numerous front end applications that does this, they are not able to detect
# events that are happening on screen, and some of them may not even have the option of randomized
# refresh intervals.
def auto_search(low, high, browser):
    while pyautogui.locateOnScreen("search_hit.png", grayscale=True, confidence=0.8) is None:
        refresh()
        # wait a bit between searches
        time.sleep(random.randint(low, high))
    click(browser[0], browser[1], 5, 5)


# auto_search(3, 5, safari)