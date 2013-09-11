#!/bin/bash

TITLE="System Information for $HOSTNAME"
RIGHT_NOW=$(date +"%x %r %Z")
TIME_STAMP="Updated on $RIGHT_NOW by $USER"

#######Functions
system_info()
{
	echo "<h2>Sytem release info</h2>"
	echo "<p>Function not yet implemented</p>"
} #end of system_info

show_uptime()
{
	echo "<h2>System update</h2>"
	echo "<pre>"
	uptime
	echo "</pre>"
} #end of show_uptime

drive_space()
{
	echo "<h2>Filesystem space</h2>"
	echo "<pre>"
	df
	echo "</pre>"
} # end of drive_space

home_space()
{
	if [ "$(id -u)" = "0" ]; then
		echo "<h2>Home directory space by user</h2>"
		echo "<pre>"
		echo "Bytes Directory"
		du -s /Users/lyc/* |sort -nr
	fi
} # end of home_space

#### Main
cat <<- _OF_
	<html>
	<head>
		<title>$TITLE</title>
	</head>
	<body>
		<h1>$TITLE</h1>
		<p>$TIME_STAMP</p>
		$(system_info)
		$(show_uptime)
		$(drive_space)
		$(home_space)
	</body>	
	</html>
_OF_










