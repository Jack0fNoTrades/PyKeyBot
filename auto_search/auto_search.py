import pyautogui
import time
import random
from util.util import click, refresh

chrome = ["chrome", 540, 420]
safari = ["safari", 540, 450, 540, 350]


# Although there are numerous front end applications that does this, they are not able to detect
# events that are happening on screen, and some of them may not even have the option of randomized
# refresh intervals.
def auto_search(low, high, browser):
    while pyautogui.locateOnScreen("search_hit.png", grayscale=True, confidence=0.8) is None:
        refresh()
        # wait a bit between searches
        time.sleep(random.randint(low, high))
    if browser[0] == "chrome":
        click(browser[1], browser[2], 5, 5)
    else:
        click(browser[1], browser[2], 5, 5)
        click(browser[3], browser[4], 5, 5)


# auto_search(3, 5, safari)