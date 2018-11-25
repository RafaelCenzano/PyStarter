from .pystarter import *
import sys

def main():
    args = sys.argv[1:]
    first_arg = sys.argv[1]

    if first_arg == 'version' or first_arg == 'V':
        print(pystarterVersion())
