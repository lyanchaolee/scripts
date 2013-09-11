#!/bin/bash

function home_space {
	if [ $(id -u)==0 ]; then
		echo "hahaha"
		du -s /Users/* |sort -nr
		echo "haha"
	fi
}
home_space
exit 0
