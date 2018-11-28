from .pystarter import *
import sys

def main():
    args = sys.argv[1:]
    first_arg = sys.argv[1].lower()

    if first_arg == '--version' or first_arg == '-v':
        print(pystarterVersion())

    elif first_arg == '--help' or first_arg == '-h':
        print(pystarterCommands())

    elif first_arg == 'create':
        try:
            second_arg = sys.argv[2].lower()
        except ValueError:
            second_arg = None

        if second_arg == 'python':
            pass
        elif second_arg == 'git':
            pass
        elif second_arg == None:
            pass
        else:
            pass

    else:
        print(pystarterCommands())
