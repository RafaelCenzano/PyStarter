from pystarter import *
import sys


def main():
    #args = sys.argv[1:]

    try:
        first_arg = sys.argv[1].lower()
    except IndexError:
        first_arg = None

    # Version command
    if first_arg == '--version' or first_arg == '-v':
        print(pystarterVersion())

    # Help command
    elif first_arg == '--help' or first_arg == '-h':
        print(pystarterCommands())

    # Main command to create needed files and things
    elif first_arg == 'create':

        # import os
        try:
            from os import path
        except BaseException:
            print('Error with importing os')
            exit()

        # import subprocess
        try:
            from subprocess import Popen, PIPE
        except BaseException:
            print('Error with importing subprocess')
            exit()

        # universal input
        try:
            input = raw_input
        except NameError:
            pass

        # Find the second argument
        try:
            second_arg = sys.argv[2].lower()
        except IndexError:
            second_arg = None

        if second_arg is not None:
            if second_arg != 'python':
                if second_arg != 'git':
                    print(
                        str(second_arg)
                        + ' is not an option for the create command\n')
                    print('''
The command is used like this:
pystarter create <option>

option can be left blank

The options you can add:
    <git> for git only projects
    <python> for python only projects
    or leave it blank for both python and git projects
                        ''')
                    exit()
                else:
                    if path.isdir('.git'):
                        print(
                            'Detected git folder.\nWould you like to include git file creation for the command\ny/n\n')
                        check_if_git = input('>')
                        if 'y' in check_if_git:
                            second_arg = 'git'
            # else:
                #python_check = pystarter_check_for_python_files()

        # Check if any README file exsists
        README = True
        if path.isfile('README.md') == False and path.isfile(
                'README.rst') == False and path.isfile('README.txt') == False:
            README = False

        # Check for files and directories for git
        requirements = path.isfile('requirements.txt')
        setup = path.isfile('setup.py')

        # Check for files and directories for python
        license = path.isfile('LICENSE') or path.isfile('LICENSE.txt')
        ignore = path.isfile('.gitignore')

        # Check for what the second arg is
        ispython = second_arg == 'python'
        isgit = second_arg == 'git'
        isall = second_arg is None

        # Checks for (python option, git option) or just both
        is_python_and_all = ispython or isall
        is_git_and_all = isgit or isall

        # Create .gitignore for git
        if ignore == False and is_git_and_all == True:
            gitignore = open('.gitignore', 'w+')
            gitignore.write('venv/\n')
            gitignore.write('*.pyc\n')
            gitignore.write('config.py\n')
            gitignore.write('__pycache__\n')
            gitignore.close()

        if README == False and is_git_and_all == True and DidREADME == False:
            dirname = path.dirname(__file__)
            READMEMD = open('README.md', 'w+')
            READMEMD.write('#' + str(dirname) + '\n\n\n')
            READMEMD.close()
            DidREADME = True

        if README2 == False and is_git_and_all == True and DidREADME == False:
            dirname = path.dirname(__file__)
            READMERST = open('README.rst', 'w+')
            lengthdirname = len(dirname)
            count = 0
            while count < lengthdirname:
                READMERST.write('=')
                count += 1
            READMERST.write('\n' + str(dirname) + '\n')
            count = 0
            while count < lengthdirname:
                READMERST.write('=')
                count += 1
            READMERST.write('\n\n\n')
            READMERST.close()
            DidREADME = True

        # Create requirements.txt if it doesn't exsist and the user wants it
        # created
        if requirements == False and is_python_and_all == True:
            requirementstxt = open('requirements.txt', 'w+')
            requirementstxt.write(' ')
            requirementstxt.close()

        # Create venv for python
        if findVenv() is not None and is_python_and_all:
            venv = Popen(
                ['virtualenv venv'],
                stdout=PIPE,
                stderr=PIPE,
                shell=True)
            (out, err) = venv.communicate()

        if setup == False and is_python_and_all == True:
            setuppy = open('setup.py', 'w+')
            setuppy.write('import sys')
            setuppy.write('import os')
            setuppy.close()

        if license == False and is_git_and_all == True:
            from builtins import input
            import requests

            while True:
                print('\nLICENSE options:\n1. Apache License 2.0\n2. MIT License\n3. GNU General Public License\n\nMore information here:\nhttps://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project\n')
                whichlicense = input(
                    'What LICENSE would you like for you project (Choose the number or write out the whole name. Write none is you don\'t want a license) : ').lower()

                if whichlicense == '1' or whichlicense == 'apache license 2.0' or whichlicense == 'apache' or whichlicense == 'apache license':
                    url = 'https://gist.githubusercontent.com/RafaelCenzano/af203e37c70f074e164105313f572e59/raw/d18216a75ee3c25f81945889c832397c5e344e67/Apache2.0.txt'
                    r = requests.get(url)
                    LICENSE = r.content

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(str(LICENSE))
                    LICENSEWRITE.close()

                    print('You will need to add your name to the LICENSE')

                    break

                elif whichlicense == '2' or whichlicense == 'mit' or whichlicense == 'mit license':
                    url = 'https://gist.githubusercontent.com/RafaelCenzano/8b0528ef01117657117b489bee831728/raw/46b65a070289a090df8a144c72ec38c19349ffa2/MIT.txt'
                    r = requests.get(url)
                    LICENSE = r.content

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(str(LICENSE))
                    LICENSEWRITE.close()

                    print('You will need to add your name to the LICENSE')

                    break

                elif whichlicense == '3' or whichlicense == 'gnu' or whichlicense == 'gnu general public license' or whichlicense == 'general public license':
                    url = 'https://gist.githubusercontent.com/RafaelCenzano/de69952598e851bc8d46bf5f42960fc3/raw/0fbbd2e2f1c869acf01b67027e50af7c1153cf55/GNU.txt'
                    r = requests.get(url)
                    LICENSE = r.content

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(str(LICENSE))
                    LICENSEWRITE.close()

                    print('You will need to add your name to the LICENSE')

                    break

                elif whichlicense == 'none':
                    break

                else:
                    print('\n\n\nThat is not and option\n\n')

    elif first_arg == 'pwd' or first_arg == 'cwd':

        # import os
        try:
            import os
        except BaseException:
            print('Error with importing os')
            exit()

        print(os.getcwd())

    else:
        print(pystarterCommands())
