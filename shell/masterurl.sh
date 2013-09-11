#!/bin/bash

SLAVE_NUM=$1
MASTER_URL_ALL="haha,heihei,fuck"

if [ "1" -eq "$SLAVE_NUM" ]; then
	MASTER_URL=$(echo "$MASTER_URL_ALL"|awk -F'[,]' '{print $1}')
elif [ "2" -eq "$SLAVE_NUM" ]; then
	MASTER_URL=$(echo "$MASTER_URL_ALL"|awk -F'[,]' '{print $2}')
else

	MASTER_URL=$(echo "$MASTER_URL_ALL"|awk -F'[,]' '{print $3}')
fi
echo $MASTER_URL
