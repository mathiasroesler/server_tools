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
				rm -f $1
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
BIN_DEST="$HOME/.local/bin"
SERVER_DEST="$HOME/.local/var"
EXEC_SCRIPTS="upload download remote-connection"
SCRIPTS=""

chmod +x $EXEC_SCRIPTS

if [[ ! -d $BIN_DEST ]]; then
	echo "Creating $BIN_DEST"
	mkdir $BIN_DEST
fi

cd $BIN_DEST

check_existence "upload"
check_existence "download"
check_existence "remote-connection"
check_existence "server_functions"

cd $CUR_DIR

if [[ -n $SCRIPTS ]]; then
	cp $SCRIPTS $BIN_DEST
	echo "Copying $SCRIPTS to $BIN_DEST"; echo

else
	echo "Nothing to copy."; echo
	copy=false
fi

SCRIPTS=""
cd $HOME

check_existence "$SERVER_DEST/servers"

if [[ -z $SCRIPTS && $copy == false ]]; then
	echo "Nothing to replace."; echo
	echo "Nothing done."
	echo "Exiting."
	exit 0

elif [[ -z $SCRIPTS ]]; then
	echo "Nothing to replace."; echo

else
	if [[ ! -d $SERVER_DEST ]]; then
		echo "Creating $SERVER_DEST"
		mkdir $SERVER_DEST
	fi
	echo "Creating$SCRIPTS"; echo
	touch "$SERVER_DEST/servers"
fi

echo "Done."
exit 0

