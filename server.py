#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Server class.
# Author: Mathias Roesler
# Last modified: 06/22

import os
import argparse
import serverFunctions

def parser_list_servers(args):
    """ Calls list_servers() from the parser.

    See serverFunctions.list_servers for more details.
    """
    serverFunctions.list_servers(args.path, args.verbose)


def parser_add_server(args):
    """ Calls add_server() from the parser.

    See serverFunctions.add_server for more details.
    """
    serverFunctions.add_server(args.path)
    

def parser_remove_server(args):
    """ Calls remove_server() from the parser.

    See serverFunctions.remove_server for more details.
    """
    serverFunctions.remove_server(args.path)


## Main program ##
if __name__ == "__main__":
    server_path = os.path.join(os.path.expanduser('~'), ".local/var/servers")

    parser = argparse.ArgumentParser(prog="server", description=
            "Handles remote server operations.")
    subparsers = parser.add_subparsers(title="available subcommands")
    
    # List subcommand parser
    list_parser = subparsers.add_parser("list", help="List available servers")
    list_parser.add_argument("-v", "--verbose", action="store_true", help=
            "prints extra information")
    list_parser.add_argument("--path", type=str, default=server_path, help=
            "path to a server list file")
    list_parser.set_defaults(func=parser_list_servers)

    # Add subcommand parser
    add_parser = subparsers.add_parser("add", help=
            "Add a server to the list of available servers")
    add_parser.add_argument("--path", type=str, default=server_path, help=
            "path to a server list file")
    add_parser.set_defaults(func=parser_add_server) 

    # Remove subcommand parser
    remove_parser = subparsers.add_parser("remove", help=
            "Remove a server from the list of available servers")
    remove_parser.add_argument("--path", type=str, default=server_path, help=
            "path to a server list file")
    remove_parser.set_defaults(func=parser_remove_server) 


    args = parser.parse_args() 
    args.func(args)
