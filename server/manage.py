#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json

# Setup
config_file = open("config",mode='r')
config_str = config_file.read()
CONFIG = json.loads(config_str)

PATH_FOLDER_FILES_CREATED = os.path.abspath(CONFIG["SAVE_LMK_TEST_FOLDER"])
PACKAGE_FOLDER = os.path.abspath(sys.path[0] + "\\..")

sys.path.append(PACKAGE_FOLDER)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cityselector.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()