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


## Main program ##
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="server", description=
            "Handles remote server operations.")
    subparsers = parser.add_subparsers(title="available subcommands")
    
    # List subcommand parser
    list_parser = subparsers.add_parser('list', help=
            "List available servers")
    list_parser.add_argument("-v", "--verbose", action="store_true", help=
            "prints extra information")
    list_parser.add_argument("--path", type=str, default=
        os.path.join(os.path.expanduser('~'), ".local/var/servers", help=
            "path to a server list file"))
    list_parser.set_defaults(func=parser_list_servers)

    args = parser.parse_args() 
    args.func(args)
