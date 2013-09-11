#!/bin/bash

number=1

set -x
if [ $number="1" ]; then
	echo "Number equals 1"
else 
	echo "Number does not equal 1"
fi
set +x

echo -n "Enter some text >"
read text
echo "You entered: $text"


echo -n "Hurry up and type something! >"
if read -t 3 response; then
	echo "Great, you made it in time with $response! "
else 
	echo "Sorry, you are too slow! "
fi

