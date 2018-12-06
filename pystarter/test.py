# This file must be called directly

from pystarter import *
import sys

commands = ('''

Usage:
pystarter <command> [options]

Commands:
create             Create all needed files for a git and python project
                     default option creates git and python files

Command Options:
python             Create project ready for python only
git                Create project ready for git only

General Options:

--help, -h         Show help
--version, -v      Show PyStarter version
        ''')

def main():
    #args = sys.argv[1:]

    try:
        first_arg = sys.argv[1].lower()
    except IndexError:
        first_arg = 'bob'


    # Version command
    if first_arg == '--version' or first_arg == '-v':
        print('1.1.1')

    # Help command
    elif first_arg == '--help' or first_arg == '-h':
        print(commands)

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

        if second_arg != 'None':
            if second_arg != 'python':
                if second_arg != 'git':
                    print(str(second_arg) + ' is not an option for the create command\n')
                    print('''
The command is used like this:
pystarter create <option>

option can be left blank

The options you can add:
    <git> for git only projects
    <python> for python only projects
                        ''')
                    GO = False
                else:
                    GO = True
            else:
                GO = True
        else:
            GO = True

        # Check if any README file exsists
        if path.isfile('README.md') == False and path.isfile('README.rst') == False:
            DidREADME = False
        else:
            DidREADME = True

        # Check for files and directories for git
        requirements = path.isfile('requirements.txt')
        setup = path.isfile('setup.py')
        venv = path.isdir('venv')

        # Check for files and directories for python
        license = path.isfile('LICENSE') or path.isfile('LICENSE.txt')
        ignore = path.isfile('.gitignore')
        README = path.isfile('README.md')
        README2 = path.isfile('README.rst')

        # Check for what the second arg is
        ispython = second_arg == 'python' and GO == True
        isgit = second_arg == 'git' and GO == True
        isall = second_arg == 'None' and GO == True

        # Checks for (python option, git option) or just both
        ispythonall = ispython == True or isall == True
        isgitall = isgit == True or isall == True

        # Create .gitignore for git
        if ignore == False and isgitall == True:
            gitignore = open('.gitignore', 'w+')
            gitignore.write('venv/\n')
            gitignore.write('*.pyc\n')
            gitignore.write('config.py\n')
            gitignore.write('__pycache__\n')
            gitignore.close()

        if README == False and isgitall == True and DidREADME == False:
            dirname = path.dirname(__file__)
            READMEMD = open('README.md', 'w+')
            READMEMD.write('#' + str(dirname) + '\n\n\n')
            READMEMD.close()
            DidREADME = True

        if README2 == False and isgitall == True and DidREADME == False:
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

        # Create requirements.txt if it doesn't exsist and the user wants it created
        if requirements == False and ispythonall == True:
            requirementstxt = open('requirements.txt', 'w+')
            requirementstxt.write(' ')
            requirementstxt.close()

        # Create venv for python
        if venv == False and ispythonall == True:
            venv = Popen(['virtualenv venv'], stdout = PIPE, stderr = PIPE, shell = True)
            (out, err) = venv.communicate()

        if setup == False and ispythonall == True:
            setuppy = open('setup.py', 'w+')
            setuppy.write('import sys')
            setuppy.write('import os')
            setuppy.close()

        if license == False and isgitall == True:
            from builtins import input
            import requests

            while True:
                print('\nLICENSE options:\n1. Apache License 2.0\n2. MIT License\n3. GNU General Public License\n\nMore information here:\nhttps://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project\n')
                whichlicense = input('What LICENSE would you like for you project (Choose the number or write out the whole name. Write none is you don\'t want a license) : ').lower()

                if whichlicense == '1' or whichlicense == 'apache license 2.0' or whichlicense == 'apache' or whichlicense == 'apache license':
                    url = 'https://gist.githubusercontent.com/SavageCoder77/af203e37c70f074e164105313f572e59/raw/d18216a75ee3c25f81945889c832397c5e344e67/Apache2.0.txt'
                    r = requests.get(url)
                    LICENSE = r.content

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(str(LICENSE))
                    LICENSEWRITE.close()

                    print('You will need to add your name to the LICENSE')

                    break

                elif whichlicense == '2' or whichlicense == 'mit' or whichlicense == 'mit license':
                    url = 'https://gist.githubusercontent.com/SavageCoder77/8b0528ef01117657117b489bee831728/raw/46b65a070289a090df8a144c72ec38c19349ffa2/MIT.txt'
                    r = requests.get(url)
                    LICENSE = r.content

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(str(LICENSE))
                    LICENSEWRITE.close()

                    print('You will need to add your name to the LICENSE')

                    break

                elif whichlicense == '3' or whichlicense == 'gnu' or whichlicense == 'gnu general public license' or whichlicense == 'general public license':
                    url = 'https://gist.githubusercontent.com/SavageCoder77/de69952598e851bc8d46bf5f42960fc3/raw/55ef789e1949d20300aeb0e8ee591a79bdf945c3/GNU.txt'
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
        import os
        print(os.getcwd())

    elif first_arg == 'activate':
        import platform
        os_type = platform.system()
        python_version_find = platform.python_version()
        split_versison = python_version_find.split(".")
        version_info_python = split_versison[0]

        if os_type == 'Windows':
            activate_this_file = 'venv\\scripts\\activate_this.py'
        else:
            activate_this_file = 'venv/bin/activate_this.py'

        if version_info_python == '2'
            execfile(activate_this_file, dict(__file__=activate_this_file))
        else:
            exec(open(activate_this_file, dict(__file__=activate_this_file)).read())

    else:
        print(commands)

if __name__ == '__main__':
    main()
