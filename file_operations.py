from log_manager import setup
import os
from datetime import date

logger = setup.get_logger(__name__)

def find_files_first(search_path):
    t = 0
    for path in os.scandir(search_path):
        if path.is_file():
            t = t + 1
        else:
            t = t + 0
    return t


##find_files is used to search path and subfolders for particular file
def find_files_second(file_name, search_path):
    t = 0
    for root, dir, files in os.walk(search_path, topdown=True):
        if file_name in files:

            t = t + 1
        else:
            t = t + 0

    return t


