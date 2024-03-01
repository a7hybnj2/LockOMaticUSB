#!/usr/bin/env python3
import Quartz
import time
import logging
# import sys
# import subprocess

# print(sys.executable)
# print(sys.version)

# installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode().strip()
# print(installed_packages)

# Check if the computer is locked

logging.basicConfig(filename='LockOMaticUSB.log', level=logging.INFO)


while True:
    session_info = Quartz.CGSessionCopyCurrentDictionary()
    is_locked = session_info and session_info.get("CGSSessionScreenIsLocked", 0) == 1

    logging.info(f'Time: {time.ctime()} - Is locked: {is_locked}')
    time.sleep(0.5)