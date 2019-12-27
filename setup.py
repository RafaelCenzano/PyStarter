from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
from io import open

# Get long description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as fR:
    long_description = fR.read()

# Get License text
with open(path.join(this_directory, 'LICENSE.txt'), encoding='utf-8') as fL:
    licenseText = fL.read()

setup(
    # Name of package
    name='PyStarter',

    # Version
    version='1.3.2',

    # description
    description='A program to help you start python and git projects with file creations',

    # Long description used as pypi homepage
    long_description=long_description,

    # Stating long description is .md
    long_description_content_type='text/markdown',

    # License
    license=licenseText,

    # Github home page
    url='https://github.com/RafaelCenzano/PyStarter',

    # Author
    author='Rafael Cenzano',

    # Contact info
    author_email='savagecoder77@gmail.com',

    # Maintainer
    maintainer='Rafael Cenzano',

    # Maintainer email
    maintainer_email='savagecoder77@gmail.com',

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
        # Python 2 no support 2020 same with PyStarter!
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # Keywords/Tags
    keywords='pystarter git python',

    # says what package your importing
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Needed installs
    #install_requires=[],

    # Data files
    # package_data={
    #    'sample': ['package_data.dat'],
    # },

    python_requires='>=3.4',

    # Adds CLI
    entry_points={
        'console_scripts': [
            'pystarter = pystarter.command_line:main',
        ],
    },

    # Additional links
    project_urls={
        'Bug Reports': 'https://github.com/RafaelCenzano/PyStarter/issues',
        'Source': 'https://github.com/RafaelCenzano/PyStarter',
    }
)
