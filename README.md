# Remote server tools

This project is a python based CLI for connecting to a remote server as well as uploading and downloading files or directories. 

## General information

The list of servers is stored locally in $HOME/.local/var
The python scripts were written using Python v3.8.10
The bash scripts were written using Bash v5.0.17(1)-release

## Required packages

This list contains the names of the packages that are required to run the scripts. The scripts have been tested using the packages with the specified versions.

   * scp v0.14.4
   * paramiko v2.11.0

## Installation

The setup.sh script should be run to set everything up. The necessary packages will be installed if they are missing. The scripts will be moved to $HOME/.local/bin and a file to contain the list of servers will be created at $HOME/.local/var. The completion script will be moved to the same directory as the server file. The directories are created if they do not exist.

To setup enter the following commands:

    $ git clone git@github.com:mathiasroesler/server_tools.git
    $ cd server_tools
    $ chmod +x setup.sh
    $ ./setup.sh

## Usage
###  Commands	

usage: server [COMMAND] [OPTION] 

There are seven available commands. To list the available commands use one of the following:

    $ server --help or server -h

* list, lists the available servers
	* usage: server list [-h] [-v] [--path PATH]
* add, adds a server to the list of available servers
	* usage: server add [-h] [--path PATH]
* remove,  removes a server from the list of available servers
	* usage: server remove [-h] [--path PATH]
* modify, modifies a server from the list of available servers
	* usage: server modify [-h] [--path PATH]
* connect, connects to a remote server.
	* usage: server connect [-h] [-p PORT] [-o [OPTIONS [OPTIONS ...]]] [-P PATH] server
* command, sends a command to a remote server.
	* usage: server command [-h] [-p PORT] [-o [OPTIONS [OPTIONS ...]]] [-O [O [O ...]]] [-P PATH] server command
* upload, uploads files or directories to a remote server
	* usage: server upload [-h] [-t TARGET] [-r] [-p PORT] [-o [OPTIONS [OPTIONS ...]]] [-P PATH] server source
* download, downloads files or directories from a remote server
	* usage: server download [-h] [-t TARGET] [-r] [-p PORT] [-o [OPTIONS [OPTIONS ...]]] [-P PATH] server source
	

For more information on a specific command run:

    $ server [COMMAND] --help or server [COMMAND] -h


### Examples

Begin with adding a server to the list of servers with the add command:

    $ server add
	
The script will prompt you for the required information. A user and host must be specified, the other parameters are optional. The default port value will be 22. 

You can then view the available servers with the list command:

	$ server list
	
The -v flag will provide more information (port number and additional options) when printing servers on screen. 

Connect to the server by using the numbering system: 

	$ server connect 1 
	
This will connect to the first server in the list. If you want to change the port value that is associated with the first server, you can specify it with the port option:

	$ server connect 1 --port 1234
	
You can also connect by providing a server name directly and specify a port number:

	$ server connect user@host --port 1234

If no port is provided, the default port number 22 will be used. 

The upload and download commands operate in a similar fashion to the connect command. There is only one supplementary argument that must be provided: the path to the file(s) to upload. 

	$ server upload 1 /path/to/files
	
To upload or download a directory recursively, use the --recursive flag

	$ server download 1 /path/to/files --recursive

Additional options can be added with the --options flag. The '-' symbol should be preceeded by a backslash '\' and followed by a space. The options flags do not handle long arguments that begin with '--'

	$ server connect 1 --options \- vX
