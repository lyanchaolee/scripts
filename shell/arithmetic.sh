#!/bin/bash

first_num=0
second_num=0

echo -n "Pls input first number >>"
read first_num
echo -n "Pls input second number >>"
read second_num

echo "first_num+second_num = $(($first_num+$second_num))"
echo "first_num-second_num = $(($first_num-$second_num))"
echo "first_num*second_num = $(($first_num*$second_num))"
echo "first_num%second_num = $(($first_num%$second_num))"
echo "first_num/second_num = $(($first_num/$second_num))"

echo "first_num pow second_num = $(($first_num**$second_num))"


