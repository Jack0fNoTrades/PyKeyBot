import time
import pyautogui
import random
from util.util import click, refresh

time.sleep(1)
print(pyautogui.locateOnScreen("2SB.png", grayscale=True, confidence=0.5) is not None)