#!/bin/sh

set -e

# Script to install lks-indicator
# assumes root powers

case "$1" in
	"--uninstall")
		rm /usr/bin/lks-indicator
		rm -r /usr/share/lks-indicator
		;;

	*)
		cp lock_keys_status.py /usr/bin/lks-indicator
		chmod a+x /usr/bin/lks-indicator
		mkdir -p /usr/share/lks-indicator/
		cp *.png /usr/share/lks-indicator/
		;;
esac
