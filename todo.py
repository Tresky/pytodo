#!/usr/bin/env python3

import sys
import argparse

def init(args):
    print('INITIALIZE')
    print(args)

def add(args):
    print('ADD TASK')
    print(args)

def list(args):
    print('LIST')
    print(args)

# Create the argument parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')

# Each subcommand has its own sub-parsers.
# Arguments with dashes (-, --) are considered optional.
# Arguments sans-dashes are required to be present.

# Add a parser for the 'init' subcommand
init_parser = subparsers.add_parser('init', aliases=['i'], help='init help')
init_parser.add_argument('list', type=str, help='Name of the list to initialize')
init_parser.set_defaults(func=init)

# Add a parser for the 'add' subcommand
add_parser = subparsers.add_parser('add', aliases=['a'], help='add help')
add_parser.add_argument('list', type=str, help='Name of the list to add to')
add_parser.add_argument('task', type=str, help='What is the task that needs to be done?')
add_parser.add_argument('-i', action='store_true', help='Open the interactive task editor')
add_parser.set_defaults(func=add)

# Add a parser for the 'list' subcommand
list_parser = subparsers.add_parser('list', aliases=['ls'], help='list help')
list_parser.add_argument('--list', type=str, help='Display the contents of a todo list')
list_parser.set_defaults(func=list)

# Parse the arguments and call the correct function
args = parser.parse_args(sys.argv[1:])
args.func(args)
