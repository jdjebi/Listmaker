import os
import sys
import json

config_file = open("config",mode='r')
config_str = config_file.read()

CONFIG = json.loads(config_str)

LMK_DATA_DIR = CONFIG["LMK_DATA_DIR"]
CONFIG["GUI_LMK_VIEWER"] = os.path.abspath(CONFIG["GUI_LMK_VIEWER"])
CORE_FOLDER = "python_core/lmk/lmk1"
PATH_FOLDER_FILES_CREATED = CONFIG["SAVE_LMK_TEST_FOLDER"]

sys.path.append(os.path.join(sys.path[0],CORE_FOLDER))