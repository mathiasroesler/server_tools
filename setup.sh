#!/bin/bash

PACKAGES=("scp" "paramiko")
SCRIPTS=("serverFunctions.py" "server-cli.py" "server")
SERVER_DEST="$HOME/.local/var"
EXEC_DEST="$HOME/.local/bin"
SERVER_FILE="$SERVER_DEST/servers"

echo "Server program setup"


# Install any required packages
for PACKAGE in "${PACKAGES[@]}"
do
	PRESENT=$(pip3 list | grep $PACKAGE)

	if [[ -z $PRESENT ]]; then
		echo "Required package $PACKAGE missing."
		pip3 install $PACKAGE
	fi
done


# Check if directory exists and move scripts to destination
if [[ ! -d $EXEC_DEST ]]; then
	echo "Creating directory $EXEC_DEST"
	mkdir $EXEC_DEST
fi

echo "Copying scripts to $EXEC_DEST"

for SCRIPT in "${SCRIPTS[@]}"
do
	cp $SCRIPT $EXEC_DEST
done

# Add executable rights to scripts that need it
chmod +x "$EXEC_DEST/server" 
chmod +x "$EXEC_DEST/server-cli.py"


# Check if directory exists and create servers file if needed
if [[ ! -d $SERVER_DEST ]]; then
	echo "Creating directory $SERVER_DEST"
	mkdir $SERVER_DEST
fi

if [[ ! -f $SERVER_FILE ]]; then
	echo "Creating server file at $SERVER_DEST"
       	touch $SERVER_FILE	
fi

echo "Setup done"
