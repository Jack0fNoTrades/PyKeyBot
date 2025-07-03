import time
import pyautogui
import random
from util.util import click, refresh

movement_list = ["left", "right", "up", "down"]
desired_x_start_1 = 740
desired_y_start_1 = 760
x_factor_1 = 50
y_factor_1 = 30
desired_x_start_2 = 690
desired_y_start_2 = 665
x_factor_2 = 80
y_factor_2 = 10
timeout = 50


def play2048():
    # start game
    click(desired_x_start_1, desired_y_start_1, x_factor_1, y_factor_1)
    # select and press arrow keys at random until the game shows the game over page
    while pyautogui.locateOnScreen("game_over.png", grayscale=True, confidence=0.8) is None:
        choice = random.randint(0, 3)
        pyautogui.press(movement_list[choice])


def reload():
    refresh()
    # (510, 620) are the coordinates of the button
    click(510, 620, 10, 10)
    pyautogui.scroll(-5)


def wait():
    while(pyautogui.locateOnScreen("playbutton.png", grayscale=True, confidence=0.8)) is None:
        time.sleep(1)


# sleep for 3 seconds to allow time to manually bring game window in focus
def execute():
    time.sleep(4)
    reload()
    # wait for loading to finish
    wait()
    win_counter = 0
    rounds_played = 0
    # we only need 3 successful games per run
    # add timeout in case detection doesn't work(so should not have to update detection target ever again)
    while win_counter < 3 and rounds_played < timeout:
        rounds_played += 1
        play2048()
        # detect if the most recent game is successful
        if pyautogui.locateOnScreen("2SB.png", grayscale=True, confidence=0.5) is not None:
            win_counter += 1
        # reload game
        click(desired_x_start_2, desired_y_start_2, x_factor_2, y_factor_2)
        # Add additional wait in response to the new version of 2048 sometimes breaking the program
        time.sleep(3)
        # wait for the game to reload
        wait()
