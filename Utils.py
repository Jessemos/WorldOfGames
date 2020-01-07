import sys
import os
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    if sys.platform.startswith('linux'):
        clear = lambda: os.system('clear')  # on Windows System
    if sys.platform.startswith('win32'):
        clear = lambda: os.system('cls')  # on Windows System
    if clear is not None:
        clear()


