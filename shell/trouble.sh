#!/bin/bash -x

number="1"

echo $number
set +x
if [ $number = "1" ]; then
	echo "Number equals 1"
else
	echo "Number does not equals 1"
fi

