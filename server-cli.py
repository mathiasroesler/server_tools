#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Main program and argument parser functions.
# Author: Mathias Roesler
# Last modified: 06/22

import os
import sys
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


def parser_modify_server(args):
    """ Calls modify_server() from the parser.

    See serverFunctions.modify_server for more details.
    """
    serverFunctions.modify_server(args.path)


def parser_connect_server(args):
    """ Calls command_server() from the parser with no command.

    See serverFunctions.connect_server for more details.
    """
    args.options = serverFunctions.clean_options(args.options)
    serverFunctions.command_server(args.path, args.server, args.port,
            args.options)


def parser_upload_server(args):
    """ Calls upload_server() from the parser.

    See serverFunctions.upload_server for more details.
    """
    args.options = serverFunctions.clean_options(args.options)
    serverFunctions.upload_server(args.path, args.server, args.port,
            args.options, args.source, args.target, args.recursive, args.quiet)


def parser_download_server(args):
    """ Calls download_server() from the parser.

    See serverFunctions.download_server for more details.
    """
    args.options = serverFunctions.clean_options(args.options)
    serverFunctions.download_server(args.path, args.server, args.port,
            args.options, args.source, args.target, args.recursive, args.quiet)


def parser_command_server(args):
    """ Calls command_server() from the parser.

    See serverFunctions.command_server for more details.
    """
    args.options = serverFunctions.clean_options(args.options)
    args.O = serverFunctions.clean_options(args.O)
    serverFunctions.command_server(args.path, args.server, args.port,
            args.options, args.command, args.O)



## Main program ##
if __name__ == "__main__":
    server_path = os.path.join(os.path.expanduser('~'), ".local/var/servers")

    parser = argparse.ArgumentParser(prog="server", description=
            "Handles remote server operations.")
    subparsers = parser.add_subparsers(title="available commands")
    
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
    remove_parser.add_argument("-P", "--path", type=str, default=server_path,
            help="path to a server list file")
    remove_parser.set_defaults(func=parser_remove_server) 
    
    # Modify subcommand parser
    modify_parser = subparsers.add_parser("modify", help=
            "Modify a server from the list of available servers")
    modify_parser.add_argument("-P", "--path", type=str, default=server_path,
            help="path to a server list file")
    modify_parser.set_defaults(func=parser_modify_server) 
    
    # Connect subcommand parser
    connect_parser = subparsers.add_parser("connect", help=
            "Connect to a remote server")
    connect_parser.add_argument("server", type=str, help=
            "server number or server name (user@host)")
    connect_parser.add_argument("-p", "--port", type=str, help="port number")
    connect_parser.add_argument("-o", "--options", type=str, default='', help=
            "additional arguments for connection", nargs='*')
    connect_parser.add_argument("-P", "--path", type=str, default=server_path,
            help="path to a server list file")
    connect_parser.set_defaults(func=parser_connect_server) 

    # Upload subcommand parser
    upload_parser = subparsers.add_parser("upload", help=
            "Upload file(s) to a remote server")
    upload_parser.add_argument("server", type=str, help=
            "server number or server name (user@host)")
    upload_parser.add_argument("source", type=str, nargs='+', help=
            "path to file(s) to upload")
    upload_parser.add_argument("-t", "--target", type=str, default='.', help=
            "path to file(s) destination on the server")
    upload_parser.add_argument("-r", "--recursive", action='store_true',
            help="upload file(s) recursively")
    upload_parser.add_argument("-p", "--port", type=str, help="port number")
    upload_parser.add_argument("-o", "--options", type=str, default='', help=
            "additional arguments for upload", nargs='*')
    upload_parser.add_argument("-P", "--path", type=str, default=server_path, 
            help="path to a server list file")
    upload_parser.add_argument("-q", "--quiet", action='store_true', help=
            "removes verbosity.")
    upload_parser.set_defaults(func=parser_upload_server) 

    # Download subcommand parser
    download_parser = subparsers.add_parser("download", help=
            "Download file(s) from a remote server")
    download_parser.add_argument("server", type=str, help=
            "server number or server name (user@host)")
    download_parser.add_argument("source", type=str, nargs='+', help=
            "path to file(s) to download")
    download_parser.add_argument("-t", "--target", type=str, default='.', help=
            "path to file(s) destination on the local machine")
    download_parser.add_argument("-r", "--recursive", action='store_true',
            help="download file(s) recursively")
    download_parser.add_argument("-p", "--port", type=str, help="port number")
    download_parser.add_argument("-o", "--options", type=str, default='', help=
            "additional arguments for download", nargs='*')
    
    download_parser.add_argument("-P", "--path", type=str, default=server_path, 
            help="path to a server list file")
    download_parser.add_argument("-q", "--quiet", action='store_true', help=
            "removes verbosity.")
    download_parser.set_defaults(func=parser_download_server) 
    
    # Command subcommand paers
    command_parser = subparsers.add_parser("command", help=
            "Executes a command on the remote server")
    command_parser.add_argument("server", type=str, help=
            "server number or server name (user@host)")
    command_parser.add_argument("command", type=str, help=
            "command to execute", nargs='+')
    command_parser.set_defaults(func=parser_command_server)
    command_parser.add_argument("-p", "--port", type=str, help="port number")
    command_parser.add_argument("-o", "--options", type=str, default='', help=
            "additional arguments for connection", nargs='*')
    command_parser.add_argument("-O", type=str, default='', nargs='*', help=
            "additional arguments for the command")
    command_parser.add_argument("-P", "--path", type=str, default=server_path, 
            help="path to a server list file")

    args = parser.parse_args() 

    try:
        args.func(args)

    except AttributeError:
        sys.stderr.write("Invalid usage\n")
        sys.stderr.write("Run 'server --help' for more information\n")
