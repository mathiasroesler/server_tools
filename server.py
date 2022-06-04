#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Server class.
# Author: Mathias Roesler
# Last modified: 06/22

import os
import sys


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
        self.options = tmp_parsed_server_args[2] # ' ' if no options.

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
