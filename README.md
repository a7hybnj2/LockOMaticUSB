# YubiKey Logout Monitor

This Python script monitors for the presence of a specific YubiKey. If the YubiKey is removed, the script locks the screen.

## Prerequisites

- Python 3
- YubiKey Manager CLI (`ykman`)

## Usage

1. Clone this repository:

	```bash
	git clone https://github.com/yourusername/yubikey-logout-monitor.git
	cd yubikey-logout-monitor
	```

2. Edit the `config.py` script and set the `device_id` variable to the serial number of your YubiKey. If you don't know the serial number of your YubiKey, you can run the script with an empty `device_id` and it will print the serial number of the connected YubiKey.

3. Run the script:

	```python
	python monitor.py
	```

	The script will now monitor for the presence of your YubiKey. If you remove the YubiKey, the script will lock the screen.

4. Implement your preferred method to automatically start the script. Examples include:

	- `@reboot` in cron
	- plist & launchctl
	- login items

## Notes

- This script is currently configured for macOS. If you're using a different operating system, you might need to modify the `device_check_command` and `lock_command` commands. Some alternative commands for Linux are included in the script, but they are commented out.
- The script uses a lock file (`/tmp/LockOMaticUSB.lock`) to ensure that only one instance of the script is running at a time.
- The script registers handlers for the `SIGINT`, `SIGTERM`, and `SIGQUIT` signals. If it receives one of these signals, it will print a message and exit.
- The `debug` variable controls whether the script prints debug information. If `debug` is `True`, the script will print messages when it checks for the YubiKey and when it locks the screen. If `debug` is `False`, the script will not print these messages.
- The `test` variable controls whether the script actually locks the screen. If `test` is `True`, the script will print a message instead of locking the screen when the YubiKey is removed. If `test` is `False`, the script will lock the screen when the YubiKey is removed.