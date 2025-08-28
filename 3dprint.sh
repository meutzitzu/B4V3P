#!/bin/bash
RED='\033[0;31m'
GRN='\033[0;32m'
RST='\033[0m'


gcodename=$1

echo $gcodename

if [[ -f "$gcodename" ]]
then
	echo $gcodename
	echo -e "\nGCODE acquired.\n ${GRN} \nRENDERING ... ${RST}"
		#pronsole -e "connect" -e "block_until_online" -e "upload $gcodename target.g" -e "sdprint target.g" -e "disconnect" -e "exit" > printnfo.txt
		#cat printnfo.txt
		printcore -v /dev/ttyUSB0 $gcodename >> printlog.txt
else
	echo -e "\n ${RED}ERROR: Failed to acquire gcode file${RST}"
fi

echo DONE
