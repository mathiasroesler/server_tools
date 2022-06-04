#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Server class.
# Author: Mathias Roesler
# Last modified: 06/22

import os
import sys
import subprocess


class Server:
    ## Init method ##
    def __init__(self, server_args):
        """ Initialise server object.

        Arguments:
        server_args -- list[str], arguments from the server,
            0: user@host
            1: port number
            2: options

        Returns:
        server -- Server, server object.
        
        """
        # Split comment from other args.
        tmp_parsed_server_args = server_args.split('#') 
        self.comment = tmp_parsed_server_args[1]

        # Split server, port and options.
        tmp_parsed_server_args = tmp_parsed_server_args[0].split(' ') 
        self.port = tmp_parsed_server_args[1]
        self.options = tmp_parsed_server_args[2] # '' if no options.

        # Split user and host.
        tmp_parsed_server_args = tmp_parsed_server_args[0].split('@')
        self.user = tmp_parsed_server_args[0]
        self.host = tmp_parsed_server_args[1]


    def __str__(self):
        """ Overloaded __str__ function.

        Arguments:

        Returns:
        server_str -- str, information of server in str format.

        """
        return ' '.join(['@'.join([self.user, self.host]), 
                self.port, 
                self.options, 
                self.comment])


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

        Arguments:
        new_user -- str, new server user.

        Returns:

        """
        self.user = new_user


    def set_host(self, new_host):
        """ Sets the server host.

        Arguments:
        new_host -- str, new server host.

        Returns:

        """
        self.host = new_host


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
            subprocess.run(["ssh", arguments, '@'.join([self.user, self.host])])

        except KeyboardInterrupt:
            sys.stderr.write("Connection to {}@{} canceled.\n".format(
                self.user, self.host))

