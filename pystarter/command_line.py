from pystarter import *
from license import *
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

    # Python Cache cleaner
    elif first_arg == 'clean':
        print('Cleaning out .pyc files and __pycache__ folders')
        cacheCleaner()
        print('Project cleaned')

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
            args = sys.argv[2:]
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

            checkArg = arguments.lower()

            if checkArg == 'python':
                ispython = True

            elif checkArg == 'git':
                isgit = True

            elif checkArg == 'all':
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
                print('Error creating Makefile\n')
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
                setupPyWrite.write(
                    '''from setuptools import setup, find_packages
import os
from os import path

currentDir = os.getcwd()

# Get Readme text
with open(path.join(currentDir, 'README.md'), encoding='utf-8') as fR:
    readme = fR.read()


# Get License text
with open(path.join(currentDir, 'LICENSE'), encoding='utf-8') as fL:
    licenseText = fL.read()


# Run setup
setup(

    # Project name
    name='Project-Name',

    # Project version number
    # Major.Moderate.Minor values
    version='1.0.0',

    # Project description
    description='Project description',

    # Project long description
    long_description=readme,

    # Define markdown long description type
    long_description_content_type='text/markdown'

    # Author name
    author='Your Name',

    # Author contact
    author_email='email@domain.com',

    # License text
    license=licenseText,

    # Project home page
    url='Project URL',

    # Classifiers help users find your project by categorizing it.
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # Python 2 no support as of 2020
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # Keywords/Tags
    keywords='project keywords',

    # says what package your importing
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Needed installs
    #install_requires=[],

    # Data files
    # package_data={
    #    'sample': ['package_data.dat'],
    # },

    #python_requires='>=3.4',

    # Adds CLI
    #entry_points={
    #    'console_scripts': [
    #        'sample cli command = projectName.FileName:FunctionName',
    #    ],
    #},

    # Additional links
    # project_urls={
    #    'Bug Reports': '',
    #    'Source': '',
    #},
)''')

                setupPyWrite.close()

                print(
                    'setup.py created\n    Update fillers in setup.py for your project\n')

            except BaseException:
                print('Error creating setup.py\n')
                exit()

        # Create license
        if license and isall or isgit:

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

        if README and isgit and not isall:

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

        elif README and isall:

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
pip3 install -r requirements.txt
```

## Running the program

Run description

```
make run
```

or with python manually

```
python3 run.py
```

## Running the tests

```
make test
```

or with ... manually

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
