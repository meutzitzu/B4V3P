#!/bin/bash
RED='\033[0;31m'
GRN='\033[0;32m'
RST='\033[0m'

filename="${1%.*}"

gcodename=$filename
gcodename+=".gcode"

if [[ "$1" != *.gcode ]]
then
	echo -e "\nSTL mesh file detected." "${GRN} \nSLICING ... ${RST}"
	prslic3r --load /home/low/tools/prslic3r/configs/Ender3_draft+supports.ini -g $1 -o $gcodename

fi


echo $gcodename

if [[ -f "$gcodename" ]]
then
	echo -e "\nGCODE acquired.\n ${GRN} \nRENDERING ... ${RST}"
	blender -b -P ../B4V3P.py -- --file $gcodename + ".gcode"

	imagename=$filename
	imagename+=".jpg"
	
	#sxiv -b $imagename &
else
	echo -e "\n ${RED}ERROR: Failed to acquire gcode file"
fi

#pronsole -e "connect" -e "block_until_online" -e "upload $gcodename target.g" -e "sdprint target.g" -e "disconnect" -e "exit" > printnfo.txt

#cat printnfo.txt

#printcore -v /dev/ttyACM0 $gcodename >> printlog.txt

echo done
