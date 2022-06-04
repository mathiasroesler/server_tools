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

    print("Instructions:")
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

    print("Server added successfully.")


def remove_server(file_path):
    """ Removes a server from the list of servers
    
    Arguments:
    file_path -- str, path to file containing the servers.

    Returns:

    """
    server_list = get_servers(file_path)
    list_servers(server_list, True)

    server_ids = ''
    new_server_list = []
    
    print("Instructions: ")
    print(" Select server numbers only.")
    print(" Separate servers with a comma and no space.")
    print(" Type q to quit.\n")

    try:
        while server_ids == '':
            server_ids = input("Select servers: ")

            if server_ids == 'q':
                exit(0)

    except KeyboardInterrupt:
        print("")
        exit(1)

    server_ids = [int(value) for value in server_ids.split(',')]

    for i in range(len(server_list)):
        if i+1 not in server_ids:
            new_server_list.append(server_list[i])

    with open(file_path, 'w') as f_handle:
        for item in new_server_list:
            f_handle.write(item)

    if len(server_list) == len(new_server_list):
        print("No servers removed.")

    elif len(server_ids) > 1:
        print("Servers removed successfully.")

    else:
        print("Server removed successfully.")


def modify_server(file_path):
    """ Modifies a server from the list of servers.

    Arguments:
    file_path -- str, path to file containing the servers.

    Returns:

    """
    server_list = get_servers(file_path)
    list_servers(server_list, True)

    server_id = ''
    modify_flag = False

    print("Instructions: ")
    print(" Select one task number only.")
    print(" Press enter to leave field unchanged.")
    print(" Type q to quit.\n")

    try:
        while server_id == '':
            server_id = input("Select server: ")

            if server_id == 'q':
                exit(0)

    except KeyboardInterrupt:
        print("")
        exit(1)

    server_object = Server(server_list[int(server_id)-1]) 

    user = ask_input("User", modify=True)
    if user != '':
        server_object.set_user(user)
        modify_flag = True

    host = ask_input("Host", modify=True)
    if host != '':
        server_object.set_host(host)
        modify_flag = True

    port = ask_input("Port", modify=True)
    if port != '':
        server_object.set_port(port)
        modify_flag = True

    options = ask_input("Options", modify=True)
    if options != '':
        server_object.set_options(options)
        modify_flag = True

    comment = ask_input("Comment", modify=True)
    if comment != '':
        server_object.set_comment(comment)
        modify_flag = True

    if not modify_flag:
        print("Server not modified.")

    else:
        server_list[int(server_id)-1] = server_object.__str__()

        with open(file_path, 'w') as f_handle:
            for item in server_list:
                f_handle.write(item)

        print("Server modified successfully.")
    

def ask_input(prompt, exit_char='q', modify=False):
    """ Asks for user input.

    If exit_char is provided then the function exits.
    Arguments:
    prompt -- str, prompt for the user.
    exit_char -- str, character to type for immediate exit.
    modify -- boolean, True if the function is used to 
        modify a server,
        default value: False.

    Returns:
    answer -- str, user answer.

    """
    try:
        answer = input("{}: ".format(prompt))

        if not modify:
            if prompt == "Host" or prompt == "User":
                while answer == '':
                    print("A {} must be provided.\n".format(prompt.lower()))
                    answer = input("{}: ".format(prompt))

                    if answer == exit_char:
                        exit(0)

        elif answer == exit_char:
                exit(0)

    except KeyboardInterrupt:
        print("")
        exit(1)

    return answer
