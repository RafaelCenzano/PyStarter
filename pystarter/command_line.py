from .pystarter import *
import sys

def main():
    args = sys.argv[1:]
    first_arg = sys.argv[1]

    if first_arg.lower() == '--version' or first_arg.lower() == '-v':
        print(pystarterVersion())

    elif first_arg.lower() == '--help' or first_arg.lower() == '-h':
        print(pystarterCommands())

    else:
        print(pystarterCommands())
