#!/bin/bash

#########################################################
### Bash script to prepare system for the server tools. #  
### Last modified: 02/2021			      	#
### Author: Mathias Roesler		      	      	#
### Contact: mathias.roesler@univ-reims.fr    	      	#
#########################################################


function check_existence() {
	# Checks if the file exists.
	#
	# Arguments:
	# $1 -- file
	# Returns:
	#
	if [[ -f $1 ]]; then
		override $1

	else
		SCRIPTS="$SCRIPTS $1"
	fi

return 0
}

function override() {
	# Asks user to override an existing file or not.
	#
	# Arguments:
	# $1 -- present file
	# Returns:
	#
	echo "File $1 already exists at destination."
	echo "Do you want to override it? (y/n)"

	valid=false

	while [ $valid == false ]
	do
		read answer
		case $answer in
			y)
				SCRIPTS="$SCRIPTS $1"
				valid=true
				;;
			n)
				valid=true
				;;
			?)
				echo "Invalid response."
				echo "Please select y or n."
				;;
		esac
	done

return 0
}


NAME=`basename $0`
CUR_DIR=$(pwd)
DESTINATION="/usr/local/bin"
EXEC_SCRIPTS="upload download remote-connection"
SCRIPTS=""

chmod +x $EXEC_SCRIPTS

echo "Checking for existence of destination."
if [[ ! -d $DESTINATION ]]; then
	echo "$NAME: $DESTINATION does not exist."
	echo "Exiting"
	exit 1
fi

echo "Folder $DESTINATION exists."
echo ""

cd $DESTINATION

check_existence "upload"
check_existence "download"
check_existence "remote-connection"
check_existence "server_functions"

cd $CUR_DIR

if [[ -z $SCRIPTS ]]; then
	echo "Nothing to do."
	echo "Exiting."
	exit 0
fi

echo "Copying$SCRIPTS to $DESTINATION"
cp $SCRIPTS $DESTINATION

SCRIPTS=""
cd $HOME

check_existence ".servers"
touch "$HOME/.servers"

cd -
echo "Moving out of $CUR_DIR"
cd ../ 
printf "Now in "
pwd
echo "Removing $CUR_DIR"
rm -rf $CUR_DIR
echo "Done."
exit 0

