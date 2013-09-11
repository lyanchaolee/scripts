#!/bin/bash

echo "input the text"
read text
echo "you input is $text"


echo "Hurry up and input text"
if read -t 3 response; then
	echo "good, you are in time and input $response"
else 
	echo "timeout...."
fi

