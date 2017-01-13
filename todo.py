#!/usr/bin/env python3

import sys

def init(args):
    if len(args) <= 1:
        print("Must provide name of todo list")
        exit(1)

    print("Initializing: " + args[1])

def list():
    print("Listing")

def default():
    print("Command not found")


def execute(command):
    return {
    "init": init,
    "i": init,
    "list": list
    }.get(command, default)

args = sys.argv[1:]
execute(args[0])(args)




# parser = argparse.ArgumentParser()
# >>> subparsers = parser.add_subparsers()
# >>> checkout = subparsers.add_parser('checkout', aliases=['co'])
# >>> checkout.add_argument('foo')
# >>> parser.parse_args(['checkout', 'bar'])
# Namespace(foo='bar')

# class Todo(object):
#     def __init__(self):
#         parser = argparse.ArgumentParser(
#             description='A simple command line todo application.',
#             usage='''Usage Example'''
#         )
#
#         # subparsers = parser.add_subparsers()
#         # init = subparsers.add_parser('init', aliases=['i'])
#         # init.add_argument('list')
#
#         parser.add_argument('command', help='Subcommand to run')
#
#         args = parser.parse_args(sys.argv[1:2])
#         # if not hasattr(self, args.command):
#         #     print("Bad Command")
#         #     parser.print_help()
#         #     exit(1)
#         getattr(self, args.command)()
#
#     def init(self):
#         parser = argparse.ArgumentParser(
#             description='Initialize a new todo list'
#         )
#
#         parser.add_argument('list')
#
#         args = parser.parse_args(sys.argv[2:])
#         print('Initializing list: ' + sys.argv[2])
#
#     def list(self):
#         parser = argparse.ArgumentParser(
#             description='List all todo lists to the console'
#         )
#
#         parser.add_argument('list')
#
#         args = parser.parse_args(sys.argv[2:])
#         print('Listing lists: ' + sys.argv[2])
#
#
# if __name__ == '__main__':
#     Todo()

# import yaml
# import sys, getopt
#
# print("Starting Application")
#
# # opt, args = getopt.getopt(sys.argv[1:], '')
#
# # print(opt, args)
#
# # for opt, arg in args
#
# args = sys.argv[1:]
# for arg in args:
#     if arg in ("init", "i"):
#         print("Initialize")
#     elif arg in ("list", "ls"):
#         print("List")
#     else:
#         print("Invalid Command")
