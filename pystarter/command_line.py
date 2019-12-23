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
            print('Error with importing os\n')
            exit()

        # import subprocess
        try:
            from subprocess import Popen, PIPE
        except BaseException:
            print('Error with importing subprocess\n')
            exit()

        # Find the second argument
        try:
            second_arg = sys.argv[2].lower()
        except IndexError:
            second_arg = None

        # Check the second argument before proceeding
        if second_arg == 'python' or second_arg == 'git' or second_arg is None:
            pass
        else:
            print(
                str(second_arg)
                + ' is not an option for the create command\n')
            print(pystarterCommands())
            exit()

        # Check for files and directories for python
        requirements = not path.isfile('requirements.txt')
        setup = not path.isfile('setup.py')
        runFile = not path.isfile('run.py')

        # Check for files and directories for git
        license = not path.isfile('LICENSE') and not path.isfile('LICENSE.txt')
        ignore = not path.isfile('.gitignore')
        README = not path.isfile('README.md') and not path.isfile(
            'README.rst') and not path.isfile('README.txt')

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

                print('Creating .gitignore')

                gitignore = open('.gitignore', 'w+')
                gitignore.write('*.DS_Store')
                if not isgit:
                    gitignore.write('venv/')
                    gitignore.write('*.pyc')
                gitignore.close()

                print('.gitignore created\n')

            except BaseException:
                print('Error creating .gitignore\n')
                exit()

        # Create blank requirements.txt
        if requirements and is_python_and_all:

            try:

                print('Creating requirements.txt')

                requirementstxt = open('requirements.txt', 'w+')
                requirementstxt.write('')
                requirementstxt.close()

                print('requirements.txt created\n')

            except BaseException:
                print('Error creating requirements.txt\n')
                exit()

        # Create python setup file and readme.rst for setup file
        if setup and is_python_and_all:

            try:

                print('Creating setup.py')

                setuppy = open('setup.py', 'w+')
                setuppy.write('''from setuptools import setup, find_packages


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
)''')

                setuppy.close()

                print(
                    'setup.py created\n    Update fillers in setup.py for your project\n')

            except BaseException:
                print('Error creating setup.py')
                exit()

            try:

                if not path.isfile('README.rst'):

                    print('    Creating Readme.rst for setup.py')

                    readmerst = open('README.rst', 'w+')
                    readmerst.write('''Project
========================

Project description

Author''')

                    readmerst.close()

                    print('        Update fillers in Readme.rst for your project\n')

            except BaseException:
                print('Error creating Readme.rst for setup.py\n')
                exit()

        # Create license
        if license and is_git_and_all:

            try:

                print('Creating LICENSE')

                LICENSE = ''

                while True:

                    print('''
LICENSE options:
  1. Apache License 2.0
  2. MIT License
  3. GNU General Public License

More information here:
  https://opensource.guide/legal/#which-open-source-license-is-appropriate-for-my-project
                          ''')

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
                        licenseType = 4
                        break

                    else:
                        print('\n\n' + whichlicense + ' is not an option\n\n')

                if licenseType is not 4:

                    LICENSEWRITE = open('LICENSE', 'w+')
                    LICENSEWRITE.write(LICENSE)
                    LICENSEWRITE.close()

                    print('Update fillers in LICENSE for your project\n')

            except BaseException:
                print('Error creating license\n')
                exit()

        if README and is_git_and_all:

            try:

                print('Creating README.md')

                READMEMD = open('README.md', 'w+')
                READMEMD.write('''# Project

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

* [**Author Name**](author link)''')

                if licenseType == 1:
                    READMEMD.write('''## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 2:
                    READMEMD.write('''## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 3:
                    READMEMD.write('''## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 4:
                    pass

                else:
                    READMEMD.write('''## License

This project's here: [LICENSE](LICENSE)''')
                    READMEMD.close()

            except BaseException:
                print('Error creating README\n')
                exit()

        elif README and is_python_and_all:

            try:

                print('Creating README.md')

                READMEMD = open('README.md', 'w+')
                READMEMD.write('''# Project

Project Description

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

* [**Author Name**](author link)''')

                if licenseType == 1:
                    READMEMD.write('''## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 2:
                    READMEMD.write('''## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 3:
                    READMEMD.write('''## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details''')

                else:
                    READMEMD.write('''## License

This project's license here: [LICENSE](LICENSE)''')

                    READMEMD.close()

            except BaseException:
                print('Error creating README\n')
                exit()

    else:
        passedArgs = ''
        for items in sys.argv[1:]:
            passedArgs += items
        print('Command ' + passedArgs + ' not found.\n')
        print(pystarterCommands())


if __name__ == '__main__':
    main()
