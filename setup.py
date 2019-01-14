from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Name of package
    name='PyStarter',

    # Version
    version='1.1.2',

    # description
    description='A program to help you start python and git project files and venvs',

    # Long description used as pypi homepage
    long_description=long_description,

    # Stating long description is .rst
    long_description_content_type='text/x-rst',

    # Github home page
    url='https://github.com/SavageCoder77/PyStarter',

    # Author
    author='Rafael Cenzano',

    # Contact info
    author_email='savagecoder77@gmail.com',

    # Classifiers help users find your project by categorizing it.
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # Keywords/Tags
    keywords='pystarter git python venv virtualenv',

    # says what package your importing
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Needed installs
    install_requires=['virtualenv==16.1.0','requests==2.20.1'],

    # Data files
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Adds CLI
    entry_points={
        'console_scripts': [
            'pystarter = pystarter.command_line:main',
        ],
    },

    # Additional links
    project_urls={
        'Bug Reports': 'https://github.com/SavageCoder77/PyStarter/issues',
        'Source': 'https://github.com/SavageCoder77/PyStarter',
    },
    )
