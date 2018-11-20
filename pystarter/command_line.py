from pystarter import pystarter
import sys

def main():
    args = sys.argv[1:]
    for arg in args:
        print('passed argument :: {}'.format(arg))

    first_arg = sys.argv[1]

    if first_arg == 'version' or first_arg == 'V':
        print(pystarter.pystarterVersion())
