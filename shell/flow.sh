#!/bin/bash

if [ -f '~/.bash_profile' ]; then
	echo "there is !"
else
	echo "does not exist !"
fi


if [ `id -u` == 0 ]; then
	echo "this is root"
else
	echo "this is not root"
fi

if [ `id -u` != 0 ]; then
	echo "you are not kind" >&2
	exit 1
fi
