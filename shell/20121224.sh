#!/bin/bash

home_space()
{
	echo "<h2>Home directory space by user</h2>"
	echo "<pre>"
	format="%8s%10s %-s\n"
	printf "$format" "Dirs" "Files" "Blocks" "Directory"
	printf "$format" "----" "-----" "------" "---------"
	if [ $(id -u) = "0" ]; then
		dir_list="/Users/*"
	else
		dir_list=$HOME
	fi
	for home_dir in $dir_list/*; do
		total_dirs=$(find $home_dir -type d|wc -l)
		total_files=$(find $home_dir -type f|wc -l)
		total_clocks=$(du -s $home_dir)
		printf "$format" $total_dirs $total_files $total_blocks
	done	
	
}

system_info()
{
	if ls /etc/*release 1>/dev/null 2>&1; then
		echo "<h2>System release info</h2>"
		echo "<pre>"
		for i in /etc/*release; do
			head -n 1 $i
		done
		uname -orp
		echo "</pre>"
	fi
}
echo $(home_space)
echo $(system_info)
