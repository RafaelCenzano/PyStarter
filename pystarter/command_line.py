from pystarter import *
import sys


# Main function for command line
def main():

    # Get first argument
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

    # Main command to create files and venvs
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

        # universal input for both python 3 and 2
        try:
            input = raw_input
        except NameError:
            pass

        # Find the second argument
        try:
            second_arg = sys.argv[2].lower()
        except IndexError:
            second_arg = None

        # Check the second argument before proceeding
        if second_arg is not None:
            if second_arg != 'python' or second_arg != 'git':
                print(
                    str(second_arg)
                    + ' is not an option for the create command\n')
                print(pystarterCommands())
                exit()

        # Check for files and directories for python
        requirements = !path.isfile('requirements.txt')
        setup = !path.isfile('setup.py')
        runFile = !path.isfile('run.py')

        # Check for files and directories for git
        license = !path.isfile('LICENSE') and !path.isfile('LICENSE.txt')
        ignore = !path.isfile('.gitignore')
        README = !path.isfile('README.md') and !path.isfile('README.rst') and !path.isfile('README.txt')

        # Check for what the second arg is
        ispython = second_arg == 'python'
        isgit = second_arg == 'git'
        isall = second_arg is None

        # Boolean variables for (python option, git option) or just both
        is_python_and_all = ispython or isall
        is_git_and_all = isgit or isall

        # Save license type
        licenseType = 0

        # Create .gitignore
        if ignore == False and is_git_and_all == True:
            try:
                gitignore = open('.gitignore', 'w+')
                gitignore.write('*.DS_Store')
                if !isgit:
                    gitignore.write('venv/')
                    gitignore.write('*.pyc')
                gitignore.close()
            except BaseException:
                print('Error creating .gitignore')
                exit()

        # Create blank requirements.txt
        if requirements and is_python_and_all:
            requirementstxt = open('requirements.txt', 'w+')
            requirementstxt.write('')
            requirementstxt.close()

        '''
        # Create venv for python
        if findVenv() is not None and is_python_and_all:
            try:
                venv = Popen(
                    ['virtualenv venv'],
                    stdout=PIPE,
                    stderr=PIPE,
                    shell=True)
                (out, err) = venv.communicate()
                print(out)
                print('Virtualenv created')
            except BaseException:
                print('Error creating Virtualenv')
                exit()
        '''

        # Create python setup file and readme.rst for setup file
        if setup and is_python_and_all:
            try:
                setuppy = open('setup.py', 'w+')
                setuppy.write('''
from setuptools import setup, find_packages


# Get Readme text
with open('README.rst') as f:
    readme = f.read()


# Get License text
with open('LICENSE') as f:
    license = f.read()


# Run setup
setup(
    name='Project-Name',
    version='0.0.0',
    description='Project description',
    long_description=readme,
    author='Your Name',
    author_email='email@domain.com',
    url='Project URL',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
                              ''')
                setuppy.close()
                print('Update fillers in setup.py for your project')
            except BaseException:
                print('Error creating setup.py')
                exit()

            try:
                if path.isfile('')
                readmerst = open('README.rst', 'w+')
                readmerst.write('''
Project
========================

Project description

Author

                                ''')
                readmerst.close()
                print('Update fillers in Readme.rst for your project')
            except BaseException:
                print('Error creating Readme.rst for setup.py')
                exit()

        # Create license
        if license and is_git_and_all:

            try:
                LICENSE = ''

                while True:
                    print('\nLICENSE options:\n1. Apache License 2.0\n2. MIT License\n3. GNU General Public License\n\nMore information here:\nhttps://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project\n')
                    whichlicense = input(
                        'What LICENSE would you like for you project (Choose the number or write out the whole name. Write \'none\' if you don\'t want a license) : ').lower()

                    if '1' in whichlicense or 'apache' in whichlicense:
                        licenseType = 1
                        LICENSE = APACHELicense()
                        break

                    elif '2' in whichlicense or 'mit' in whichlicense:
                        licenseType = 2
                        LICENSE = MITLicense()
                        break

                    elif '3' in whichlicense or 'gnu' in whichlicense or 'general public license' in whichlicense:
                        licenseType = 3
                        LICENSE = GNULicense()
                        break

                    elif 'none' in whichlicense:
                        break

                    else:
                        print('\n\n\nThat is not and option\n\n')

                LICENSEWRITE = open('LICENSE', 'w+')
                LICENSEWRITE.write(str(LICENSE))
                LICENSEWRITE.close()

                print('You will need to add your name to the LICENSE')

            except BaseException:
                print('Error creating license')
                exit()

        if README and isgit:
            READMEMD = open('README.md', 'w+')
            READMEMD.write('''
# Project

Project Description

## Setup

Clone the repository and enter it

```
git clone <git clone url>
cd <project name>
```

#### Requirements

Run the make command to install requirements

```
requirement install command
```

## Running the program

Run description

```
run command
```

## Running the tests

```
run test command
```

#### What are the tests checking

test check for ...

#### What happens when a test fails

Report the failed test [here](issue link)!

## Authors

* [**Author Name**](author link)
                           ''')
            if licenseType == 1:
                READMEMD.write('''
## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
                               ''')
            elif licenseType == 2:
                READMEMD.write('''
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
                              ''')
            elif licenseType == 3:
                READMEMD.write('''
## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details
                               ''')
            else:
                READMEMD.write('''
## License

This project's here: [LICENSE](LICENSE)
                               ''')
                READMEMD.close()

        if README and is_python_and_all:
            READMEMD = open('README.md', 'w+')
            READMEMD.write('''
# Project

Project Description

## Setup

Clone the repository and enter it

```
git clone <git clone url>
cd <project name>
```

#### Requirements

[Use a virtualenv to create an isolated enviorment](https://virtualenv.pypa.io/en/latest/)

Run the make command to install requirements

```
make
```

or with pip manually

```
pip install -r requirements.txt
```

## Running the program

Run description

```
make run
```

or with python manually

```
python run.py
```

## Running the tests

```
make test
```

or manually with ...

```
run test command
```

#### What are the tests checking

test check for ...

#### What happens when a test fails

Report the failed test [here](issue link)!

## Authors

* [**Author Name**](author link)
                           ''')
            if licenseType == 1:
                READMEMD.write('''
## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
                               ''')
            elif licenseType == 2:
                READMEMD.write('''
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
                              ''')
            elif licenseType == 3:
                READMEMD.write('''
## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details
                               ''')
            else:
                READMEMD.write('''
## License

This project's here: [LICENSE](LICENSE)
                               ''')
                READMEMD.close()

    else:
        print('Command ' + sys.argv[1:] + ' not found.\n')
        print(pystarterCommands())


if __name__ == '__main__':
    main()
