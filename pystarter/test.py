from pystarter import *
import sys

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

        if path.isfile('README.md') == False and path.isfile('README.rst') == False:
            DidREADME = False
        else:
            DidREADME = True

        # Check for files and directories
        requirements = not path.isfile('requirements.txt')
        venv = not path.isdir('venv')
        ignore = not path.isfile('.gitignore')
        README = not path.isfile('README.md')
        README2 = not path.isfile('README.rst')
        setup = not path.isfile('setup.py')
        license = not path.isfile('LICENSE') or not path.isfile('LICENSE.txt')

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
            requirementstxt.write(' ')
            requirementstxt.close()

        # Create venv for python
        if venv and ispythonall:
            venv = Popen(['virtualenv venv'], stdout = PIPE, stderr = PIPE, shell = True)
            (out, err) = venv.communicate()

        if ignore and isgitall:
            gitignore = open('.gitignore', 'w+')
            gitignore.write('venv/\n')
            gitignore.write('*.pyc\n')
            gitignore.write('config.py\n')
            gitignore.write('__pycache__\n')
            gitignore.close()

        if README and isgitall and DidREADME == False:
            dirname = path.dirname(__file__)
            READMEMD = open('README.md', 'w+')
            READMEMD.write('#' + str(dirname) + '\n\n\n')
            READMEMD.close()
            DidREADME = True

        if README2 and isgitall and DidREADME == False:
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

        if setup and ispythonall:
            setuppy = open('setup.py', 'w+')
            setuppy.write('import sys')
            setuppy.write('import os')
            setuppy.close()

        if license and isgitall:
            from builtins import input
            import requests

            while True:
                print('\nLICENSE options:\n1. Apache License 2.0\n2. MIT License\n3. GNU General Public License\nMore information here:\nhttps://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project\n')
                whichlicense = input('What LICENSE would you like for you project (Choose the number or write out the whole name. Write none is you don\'t want a license) : ').lower()

                if whichlicense == '1' or whichlicense == 'apache license 2.0' or whichlicense == 'apache' or whichlicense == 'apache license':
                    url = 'https://gist.githubusercontent.com/SavageCoder77/af203e37c70f074e164105313f572e59/raw/d18216a75ee3c25f81945889c832397c5e344e67/Apache2.0.txt'
                    r = requests.get(url)
                    page = r.text
                    soup = bs(page, 'html.parser')
                    text = soup.findAll('pre', attrs={'style':'word-wrap'})
                    LICENSE = text[0].getText()

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(LICENSE)
                    LICENSEWRITE.close()

                    print('You will need to add you name to the LICENSE')

                elif whichlicense == '2' or whichlicense == 'mit' or whichlicense == 'mit license':
                    url = 'https://gist.githubusercontent.com/SavageCoder77/8b0528ef01117657117b489bee831728/raw/46b65a070289a090df8a144c72ec38c19349ffa2/MIT.txt'
                    r = requests.get(url)
                    page = r.text
                    soup = bs(page, 'html.parser')
                    text = soup.findAll('pre', attrs={'style':'word-wrap'})
                    LICENSE = text[0].getText()

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(LICENSE)
                    LICENSEWRITE.close()

                    print('You will need to add you name to the LICENSE')

                elif whichlicense == '3' or whichlicense == 'gnu' or whichlicense == 'gnu general public license' or whichlicense == 'general public license':
                    url = 'https://gist.githubusercontent.com/SavageCoder77/de69952598e851bc8d46bf5f42960fc3/raw/55ef789e1949d20300aeb0e8ee591a79bdf945c3/GNU.txt'
                    r = requests.get(url)
                    page = r.text
                    soup = bs(page, 'html.parser')
                    text = soup.findAll('pre', attrs={'style':'word-wrap'})
                    LICENSE = text[0].getText()

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(LICENSE)
                    LICENSEWRITE.close()

                    print('You will need to add you name to the LICENSE')

                elif whichlicense == 'none':
                    break

                else:
                    print('\n\n\nThat is not and option\n\n')


    elif first_arg == 'pwd' or first_arg == 'cwd':
        import os
        print(os.getcwd())

    else:
        print(pystarterCommands())

if __name__ == '__main__':
    main()
