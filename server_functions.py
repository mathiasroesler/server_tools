#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Functions used by server.py 
# Author: Mathias Roesler
# Last modified: 06/22


import os
import sys
from server import Server


def get_servers(file_path):
    """ Gets the servers from the file.

    Arguments:
    file_path -- str, path to file containing the servers.

    Returns:
    server_list -- list[str], list of servers from the file.

    """
    if not os.path.exists(file_path):
        sys.stderr.write("Error: {} does not exist.\n".format(file_path))
        sys.stderr.write("Exiting.\n")
        exit(1)

    elif not os.path.isfile(file_path):
        sys.stderr.write("Error: {} is not a file.\n".format(file_path))
        sys.stderr.write("Exiting.\n")
        exit(2)

    with open(file_path, 'r') as f_handle:
        server_list = f_handle.readlines()
    
    return server_list


def list_servers(server_list, verbose=False):
    """ Lists all the server from the server list.

    Arguments:
    server_list -- list[str], list of servers.

    Returns:

    """
    print("Currently available servers:")

    for i in range(len(server_list)):
        server_object = Server(server_list[i])
        print(" {}: {}".format(str(i+1), server_object.get_server_name()))

        if verbose:
            print("    Port: {}".format(server_object.get_port()))
            print("    Options: {}".format(server_object.get_options()))

        print("    Comment: {}".format(server_object.get_comment()))
     

def add_server(file_path):
    """ Adds a server to the list of servers.

    Arguments:
    file_path -- str, path to file containing the servers.

    Returns:

    """
    server_list = get_servers(file_path)
    list_servers(server_list, True)

    print("\nInstructions:")
    print(" Provide the user, host, port, options and comment.")
    print(" A user and host must be provided.")
    print(" Press q to quit.")
    print(" Press enter to provide default values.")
    print(" Default port: 22 | Default options: '' | Default comment: ''i\n")
    
    user = ask_input("User")
    host = ask_input("Host")
    port = ask_input("Port")
    options = ask_input("Options")
    comment = ask_input("Comment")

    if port == '':
        port = "22"

    with open(file_path, 'a') as f_handle:
        server_name = '@'.join([user, host])
        server_args = ' '.join([server_name,
                port, 
                options,
                '']) 

        f_handle.write('#'.join([server_args, comment + '\n']))


def ask_input(prompt, exit_char='q'):
    """ Asks for user input.

    If exit_char is provided then the function exits.
    Arguments:
    prompt -- str, prompt for the user.
    exit_char -- str, character to type for immediate exit.

    Returns:
    answer -- str, user answer.

    """
    try:
        answer = input("{}: ".format(prompt))

        if prompt == "Host" or prompt == "User":
            while answer == exit_char or answer == '':
                if answer == exit_char:
                    exit(0)

                print("A {} must be provided.\n".format(prompt.lower()))
                answer = input("{}: ".format(prompt))

        else:
            if answer == exit_char:
                exit(0)

    except KeyboardInterrupt:
        print("")
        exit(1)

    return answer
