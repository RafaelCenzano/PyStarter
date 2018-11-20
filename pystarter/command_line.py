import pystarter
import sys

def main():
    args = sys.argv[1:]
    for arg in args:
        print('passed argument :: {}'.format(arg))
