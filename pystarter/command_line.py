from .pystarter import *
import sys
from os import path, mkdir, listdir, remove
from platform import system
from shutil import rmtree, move

def main():
    args = sys.argv[1:]
    first_arg = sys.argv[1].lower()

    # Version command
    if first_arg == '--version' or first_arg == '-v':
        print(pystarterVersion())

    # Help command
    elif first_arg == '--help' or first_arg == '-h':
        print(pystarterCommands())

    # Main command to create needed files and things
    elif first_arg == 'create':
        try:
            second_arg = sys.argv[2].lower()
        except ValueError:
            second_arg = None

        if second_arg != 'python' or second_arg != 'git' or second_arg != None:
            print('''
The command is used like this:
pystarter create <option>

option can be left blank

The options you can add:
    <git> for git only projects
    <python> for python only projects
                  ''')
            continue

        # Check for files and directories
        requirements = not path.isfile('requirements.txt')
        venv = not path.isdir('venv')
        ignore = not path.isfile('.gitignore')
        README = not path.isfile('README.md')
        README2 = not path.isfile('README.rst')
        setup = not path.isfile('setup.py')
        license = not path.isfile('LICENSE') or path.isfile('LICENSE.txt')
        ispython = second_arg == 'python'
        isgit = second_arg == 'git'
        isall = second_arg == None
        ispythonall = ispython or isall
        isgitall = isgit or isall

        if requirements and ispythonall:


    elif first_arg == 'pwd' or first_arg == 'cwd':
        print(os.getcwd())

    else:
        print(pystarterCommands())
