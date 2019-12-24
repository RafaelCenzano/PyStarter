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

        # Find the second argument
        try:
            args = sys.argv[2:].lower()
        except IndexError:
            args = ['all']

        # Check the second argument before proceeding
        if 'python' in args or 'git' in args or 'all' in args:
            pass
        else:
            print('No valid arguments passed for create command')
            print(pystarterCommands())
            exit()

        # Check for files and directories for python
        requirements = not path.isfile('requirements.txt')
        setup = not path.isfile('setup.py')
        runFile = not path.isfile('run.py')
        makeFile = not path.isfile('Makefile')

        # Check for files and directories for git
        license = not path.isfile('LICENSE') and not path.isfile('LICENSE.txt')
        ignore = not path.isfile('.gitignore')
        README = not path.isfile('README.md') and not path.isfile(
            'README.rst') and not path.isfile('README.txt')

        # Check for what the second arg is
        ispython = False
        isgit = False
        isall = False

        # Check arguments by looping through and checking
        for arguments in args:

            if arguments == 'python':
                ispython = True

            elif arguments == 'git':
                isgit = True

            elif arguments == 'all':
                isall = True

        if not isall and ispython and isgit:
            isall = True
        
        # Save license type
        licenseType = 0


        '''
        Python file creation
        '''


        # Create run.py
        if runFile and isall or ispython:

            try:

                print('Creating run.py')

                runPyWrite = open('run.py', 'w+')
                runPyWrite.write('')
                runPyWrite.close()

                print('run.py created\n')

            except BaseException:
                print('Error creating run.py\n')
                exit()

        if makeFile and isall or ispython:

            try:

                print('Creating Makefile')

                makeFileWrite = open('Makefile', 'w+')
                makeFileWrite.write('''
init:
    pip3 install -r requirements.txt

test:
    add test command here

run:
    python3 run.py''')
                makeFileWrite.close()

                print('Makefile created\n')

            except BaseException:
                print('Error creating run.py\n')
                exit()

        # Create blank requirements.txt
        if requirements and isall or ispython:

            try:

                print('Creating requirements.txt')

                requirementsTxtWrite = open('requirements.txt', 'w+')
                requirementsTxtWrite.write('')
                requirementsTxtWrite.close()

                print('requirements.txt created\n')

            except BaseException:
                print('Error creating requirements.txt\n')
                exit()

        # Create python setup file and readme.rst for setup file
        if setup and isall or ispython:

            try:

                print('Creating setup.py')

                setupPyWrite = open('setup.py', 'w+')
                setupPyWrite.write('''from setuptools import setup, find_packages


# Get Readme text
with open('README.rst') as f:
    readme = f.read()


# Get License text
with open('LICENSE') as f:
    license = f.read()


# Run setup
setup(
    name='Project-Name',
    version='1.0.0',
    description='Project description',
    long_description=readme,
    author='Your Name',
    author_email='email@domain.com',
    url='Project URL',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)''')

                setupPyWrite.close()

                print(
                    'setup.py created\n    Update fillers in setup.py for your project\n')

            except BaseException:
                print('Error creating setup.py')
                exit()

            try:

                if not path.isfile('README.rst'):

                    print('    Creating Readme.rst for setup.py')

                    readmeRstWrite = open('README.rst', 'w+')
                    readmeRstWrite.write('''Project
========================

Project description

Author''')

                    readmeRstWrite.close()

                    print('        Update fillers in Readme.rst for your project\n')

            except BaseException:
                print('Error creating Readme.rst for setup.py\n')
                exit()

        # Create license
        if license and isall or isgit:

            try:

                print('Creating LICENSE\n')

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

                    LicenseWrite = open('LICENSE', 'w+')
                    LicenseWrite.write(LICENSE)
                    LicenseWrite.close()

                    print('Update fillers in LICENSE for your project\n')

            except BaseException:
                print('Error creating license\n')
                exit()
                
        # Create .gitignore
        if ignore and isall or isgit:

            try:

                print('Creating .gitignore')

                gitignoreWrite = open('.gitignore', 'w+')
                gitignoreWrite.write('*.DS_Store')
                if isall or ispython:
                    gitignoreWrite.write('venv/')
                    gitignoreWrite.write('*.pyc')
                    gitignoreWrite.write('__pycache__/')
                gitignoreWrite.close()

                print('.gitignore created\n')

            except BaseException:
                print('Error creating .gitignore\n')
                exit()


        if README and isall or isgit:

            try:

                print('Creating README.md')

                ReadmeMdWrite = open('README.md', 'w+')
                ReadmeMdWrite.write('''# Project

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
                    ReadmeMdWrite.write('''## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 2:
                    ReadmeMdWrite.write('''## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 3:
                    ReadmeMdWrite.write('''## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 4:
                    pass

                else:
                    ReadmeMdWrite.write('''## License

This project's here: [LICENSE](LICENSE)''')
                
                ReadmeMdWrite.close()

            except BaseException:
                print('Error creating README\n')
                exit()

        elif README and is_python_and_all:

            try:

                print('Creating README.md')

                ReadmeMdWrite = open('README.md', 'w+')
                ReadmeMdWrite.write('''# Project

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
                    ReadmeMdWrite.write('''## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 2:
                    ReadmeMdWrite.write('''## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details''')

                elif licenseType == 3:
                    ReadmeMdWrite.write('''## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details''')

                else:
                    ReadmeMdWrite.write('''## License

This project's license here: [LICENSE](LICENSE)''')

                ReadmeMdWrite.close()

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
