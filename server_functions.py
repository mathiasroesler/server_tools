#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Functions used by server.py 
# Author: Mathias Roesler
# Last modified: 06/22


import os
import sys


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
