# Tools for common operations with remote servers

This project contains three scripts for common operations with remote server, namely:
- Copying files to the remote server,
- Downloading files from the remote server,
- Connecting to the remote server.

## General information

These scripts are to easily connect to, upload files to and download files from a remote server. They use either ssh or scp to connect the user to the server.

The used servers are stored in the .servers file located in the $HOME directory. Each line of the file corresponds to one server and is stored in the following fashion: user@host port options.
The options can be any option used with the scp and ssh utilies.

## Installation

The installation process will create a file to store the available servers and move the scripts to /usr/local/bin.

To install enter the following commands:

    $ git clone  https://github.com/mathiasroesler/server_tools.git
    $ cd server_tools
    $ chmod +x install.sh
    $ ./install.sh

Note: your password will be required to copy the files.
    
## Usage

Because the scripts are moved into the /usr/local/bin folder during the installation process, they can be called from any directory. 

The commands will search for the specified server in the .servers file. It is advised to use the line number associated with the desired server rather than typing the full name of the server. The latter option is also possible, however some option (such as the -d flag) require the line number method.
For example, to connect to the first server stored in the file simply use the command

    $ remote-connection 1
    
Or alternatively, if the first server in the list is `user@host`
    
    $ remote-connection user@host
    
You can specify a port number to connect to with the -p option and the any other flags to be used with the -o option. 

For example this command will connect to the server user@host at the port 6748 in verbose mode and use the 3des-cbc encryption, and upload file1 to ~/folder 

    $ upload -p 6748 -o "-vc 3des-cbc" user@host file1 ~/folder
    
This would be equivalent to the following command if the third line in the .servers file is user@host 6748 -vc 3des-cbc

    $ upload 3 file1 ~/folder
    
If you connect to a server that is not stored in the .servers file, you will be asked if you want to add it to the list. Alternatively, you can use the -a option to add a server to the file. 

The -h options will show all of the available options, and the -l and -L options list the servers stored in the .servers file.
