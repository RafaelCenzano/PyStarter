from pystarter import *
import sys
#from platform import system
#from shutil import rmtree, move


def main():
    #args = sys.argv[1:]

    try:
        first_arg = sys.argv[1].lower()
    except IndexError:
        first_arg = 'bob'


    # Version command
    if first_arg == '--version' or first_arg == '-v':
        print(pystarterVersion())

    # Help command
    elif first_arg == '--help' or first_arg == '-h':
        print(pystarterCommands())

    # Main command to create needed files and things
    elif first_arg == 'create':
        # Make sure imports work
        try:
            from os import path
            from subprocess import Popen, PIPE
        except:
            print('Error with pythom imports')
            pass

        # Find the second argument
        try:
            second_arg = sys.argv[2].lower()
        except IndexError:
            second_arg = 'None'

        if second_arg == 'python' or second_arg == 'git' or second_arg != 'None':
            print(str(second_arg) + ' is not an option for the create command\n')
            print('''
The command is used like this:
pystarter create <option>

option can be left blank

The options you can add:
    <git> for git only projects
    <python> for python only projects
                  ''')
            pass

        # Check for files and directories
        requirements = not path.isfile('requirements.txt')
        venv = not path.isdir('venv')
        ignore = not path.isfile('.gitignore')
        README = not path.isfile('README.md')
        README2 = not path.isfile('README.rst')
        setup = not path.isfile('setup.py')
        license = not path.isfile('LICENSE') or path.isfile('LICENSE.txt')

        # Check for what the second arg is
        ispython = second_arg == 'python'
        isgit = second_arg == 'git'
        isall = second_arg == 'None'

        # Checks for (python option, git option) or just both
        ispythonall = ispython or isall
        isgitall = isgit or isall

        # Create requirements.txt if it doesn't exsist and the user wants it created
        if requirements and ispythonall:
            requirementstxt = open('requirements.txt', 'w+')
            requirementstxt.write('')
            requirementstxt.close()

        if venv and ispythonall:
            pass

    elif first_arg == 'pwd' or first_arg == 'cwd':
        print(os.getcwd())

    else:
        print(pystarterCommands())

if __name__ == '__main__':
    main()
