#!/usr/local/bin/python3

import os
import signal
import sys
# NOTE: getpass is for the logout command. I'm not using it but I'm leaving it here for reference.
# import getpass
import fcntl
import time

# Import the config file
import config

# Lock file
lock_file = '/tmp/monitor.lock'
lock_file = open(lock_file, 'w')

# Pause file
if config.pause_path == '~':
    home_dir = os.path.expanduser("~")
    pause_file = os.path.join(home_dir, config.pause_filename)
else:
    pause_file = os.path.join(config.pause_path, config.pause_filename)

try:
    fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print("Another instance of the script is running. Exiting.")
    sys.exit(1)

# Define the signal handler function
def signal_handler(sig, frame):
    if sig == signal.SIGINT:
        print('You pressed Ctrl+C!')
    elif sig == signal.SIGTERM:
        print('Received SIGTERM!')
    elif sig == signal.SIGQUIT:
        print('Received SIGQUIT!')
    else:
        print('Received signal:', sig)
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)


output = os.popen(config.device_check_command).read().strip()

if config.device_id == "":
    print("No Yubikey serial number provided. Please provide a serial number between the quotes for variable yubikey_sn.")
    # Find the position of "Serial: " in the output
    start = output.find("Serial: ")
    # If "Serial: " is found, extract the serial number
    if start != -1:
        serial_number = output[start + len("Serial: "):].strip()
        print("The connected Yubikey serial number is:", serial_number)
    else:
        print("Serial number not found, please connect a Yubikey and try again.")
    sys.exit(0)

while (1):
    if not os.path.exists(pause_file):
        time.sleep(.5)
        output = os.popen(config.device_check_command).read().strip()
        if config.debug:
            print(output)
        if config.device_id not in output:
            if not(config.test):
                os.system(config.lock_command)
            else:
                print("Yubikey not found. Locking screen(pretend).")
    else:
        time.sleep(1)
        if config.debug:
            print("Pause file found. Paused.")