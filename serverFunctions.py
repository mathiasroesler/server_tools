#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Server class and helper functions.
# Author: Mathias Roesler
# Last modified: 06/22


import os
import sys
import getpass
import subprocess
from scp import SCPClient
from paramiko import SSHClient


##################
## Server class ##
##################


class Server:
    ## Init method ##
    def __init__(self, server_elems):
        """ Initialise server object.

        Arguments:
        server_elems -- list[str], elems of a server object,
            0: user@host
            1: port number
            2: options
            3: comment

        Returns:
        server -- Server, server object.
        
        """
        # Split comment from other args.
        tmp_parsed_server_elems = server_elems.split('#') 
        self.comment = tmp_parsed_server_elems[1]

        # Split server, port and options.
        tmp_parsed_server_elems = tmp_parsed_server_elems[0].split(' ') 
        self.port = tmp_parsed_server_elems[1]
        self.options = tmp_parsed_server_elems[2] # '' if no options.

        # Split user and host.
        tmp_parsed_server_elems = tmp_parsed_server_elems[0].split('@')
        self.user = tmp_parsed_server_elems[0]
        self.host = tmp_parsed_server_elems[1]
        self.server_name = '@'.join([self.user, self.host])


    def __str__(self):
        """ Overloaded __str__ function.

        Arguments:

        Returns:
        server_str -- str, information of server in str format.

        """
        server_args = ' '.join([self.server_name,
                self.port, 
                self.options,
                '']) 

        return '#'.join([server_args, self.comment])


    ## Getters ##
    def get_user(self):
        """ Gets the server user.

        Arguments:

        Returns:
        user -- str, server user.

        """
        return self.user


    def get_host(self):
        """ Gets the server host.

        Arguments:

        Returns:
        host -- str, server host.

        """
        return self.host


    def get_server_name(self):
        """ Gets the server name.

        Argument:

        Returns:
        server_name -- str, server name.

        """
        return self.server_name


    def get_port(self):
        """ Gets the server port number.

        Arguments:

        Returns:
        port -- str, server port number.

        """
        return self.port


    def get_options(self):
        """ Gets the server options.

        Arguments:

        Returns:
        options -- str, server options.

        """
        return self.options


    def get_comment(self):
        """ Gets the server comment.

        Arguments:

        Returns:
        comment -- str, server comment.

        """
        return self.comment


    ## Setters ##
    def set_user(self, new_user):
        """ Sets the server user.

        Resets the server name as well.
        Arguments:
        new_user -- str, new server user.

        Returns:

        """
        self.user = new_user
        self.server_name = '@'.join([self.user, self.host])


    def set_host(self, new_host):
        """ Sets the server host.

        Resets the server name as well.
        Arguments:
        new_host -- str, new server host.

        Returns:

        """
        self.host = new_host
        self.server_name = '@'.join([self.user, self.host])


    def set_port(self, new_port):
        """ Sets the server port number.

        Arguments:
        new_port -- str, new server port number.

        Returns:

        """
        self.port = new_port


    def set_options(self, new_options):
        """ Sets the server options.

        Arguments:
        new_options -- str, new server options.

        Returns:

        """
        self.options = new_options


    def set_comment(self, new_comment):
        """ Sets the server comment.

        Arguments:
        new_comment -- str, new server comment.

        Returns:

        """
        self.comment = new_comment


    ## Methods ##
    def connect(self):
        """ Connects to the remote server via ssh.

        Arguments:

        Returns:

        """
        if self.options != '':
            arguments = ' '.join(["-p " + self.port, self.options])

        else:
            arguments = "-p " + self.port

        try:
            subprocess.run(["ssh", arguments, self.server_name])

        except KeyboardInterrupt:
            sys.stderr.write("Connection to {}@{} canceled.\n".format(
                self.user, self.host))
            exit(1)


    def upload(self, file_path, dest_path='.', recursive=False):
        """ Uploads the file(s) to the server.

        Arguments:
        file_path -- str or list[str], path file or list of paths
            of files to upload.
        dest_path -- str, path to file(s) destination,
            default value: '.'.
        recursive -- boolean, uploads files recursively if True,
            defaut value: False.

        Returns:

        """
        with SSHClient() as ssh:
            ssh.load_system_host_keys()
            password_prompt = "{}@{}'s password: ".format(
                    self.user, self.host)

            try:
                password = getpass.getpass(password_prompt)

            except KeyboardInterrupt:
                sys.stderr.write("\nConnection to {}@{} canceled.\n".format(
                    self.user, self.host))
                exit(1)

            ssh.connect(self.get_host(), 
                    port=int(self.get_port()), 
                    username=self.get_user(), 
                    password=password)


            with SCPClient(ssh.get_transport()) as scp:
                try:
                    if recursive:
                        scp.put(file_path, remote_path=dest_path, 
                                recursive=recursive)

                    else:
                        scp.put(file_path, remote_path=dest_path)

                except FileNotFoundError:
                    sys.stderr.write("{}: No such file or directory.\n".format(
                        file_path))
                    exit(2)


    def download(self, file_path, dest_path='.', recursive=False):
        """ Downloads the file(s) to the server.

        Arguments:
        file_path -- str or list[str], path file or list of paths
            of files to download.
        dest_path -- str, path to file(s) destination,
            default value: '.'.
        recursive -- boolean, downloads files recursively if True,
            defaut value: False.

        Returns:

        """
        with SSHClient() as ssh:
            ssh.load_system_host_keys()
            password_prompt = "{}@{}'s password: ".format(
                    self.user, self.host)

            try:
                password = getpass.getpass(password_prompt)

            except KeyboardInterrupt:
                sys.stderr.write("\nConnection to {}@{} canceled.\n".format(
                    self.user, self.host))
                exit(1)

            ssh.connect(self.get_host(), 
                    port=int(self.get_port()), 
                    username=self.get_user(), 
                    password=password)


            with SCPClient(ssh.get_transport()) as scp:
                try:
                    if recursive:
                        scp.get(file_path, remote_path=dest_path, 
                                recursive=recursive)

                    else:
                        scp.get(file_path, remote_path=dest_path)

                except FileNotFoundError:
                    sys.stderr.write("{}: No such file or directory.\n".format(
                        file_path))
                    exit(2)

######################
## Server functions ##
######################

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


def list_servers(file_path, verbose=False):
    """ Lists all the server from the server list.

    Arguments:
    file_path -- str, path to file containing the servers.

    Returns:

    """
    server_list = get_servers(file_path)

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
    list_servers(file_path, True)

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
    list_servers(file_path, True)

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
    list_servers(file_path, True)

    server_id = ''
    modify_flag = False

    print("Instructions: ")
    print(" Select one server number only.")
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
