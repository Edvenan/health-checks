#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
	""" Returns  True if the computer has a pending reboot. """
	return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_precent):
	""" Returns True if there isn't enough disk space, False otherwise. """
	du = shutil.disk_usage(disk)
	# Calculate the percentage of free space
	percent_free = 100 * du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb
		return True
	return False

def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	if check_disk_full(disk="/",min_gb= 2, min_percent= 10):
		print("Disk full.")
		sys.exit(1)
	# by using the name of the parameters when we call the function, we can even
	# alter the order of the values and the code will still work
	print("Everything ok.")
	sys.exit(0)

main()