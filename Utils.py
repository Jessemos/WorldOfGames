import sys
import os
from datetime import datetime

SCORES_FILE_NAME = "Scores.txt"
FILES_PATH = "Resources/Files/"
BAD_RETURN_CODE = -1


def screen_cleaner():
    if sys.platform.startswith('linux'):
        clear = lambda: os.system('clear')  # on Windows System
    if sys.platform.startswith('win32'):
        clear = lambda: os.system('cls')  # on Windows System
    if clear is not None:
        clear()
        print("Screen should be cleared...")


def time_stamp():
    date_time_obj = datetime.now()
    time_stamp_str = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
    return time_stamp_str

