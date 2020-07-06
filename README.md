# PyStarter

PyStarter starter provides an easy way to start a git or python projects with helpful file creation.

![Version](https://img.shields.io/pypi/v/PyStarter.svg)
![Supported python versions](https://img.shields.io/pypi/pyversions/PyStarter.svg)
![License badge](https://img.shields.io/github/license/RafaelCenzano/PyStarter.svg)
![GitHub stars](https://img.shields.io/github/stars/RafaelCenzano/PyStarter.svg)
![GitHub forks](https://img.shields.io/github/forks/RafaelCenzano/PyStarter.svg)

## Usage

Main Commands:

``pystarter create``

This command creates project files for python and git projects

This command has 3 extra options. One to create git ready, one to create python ready projects, and one to create both python and git ready projects.
The options are: *git*, *python*, *all*, *setup*
- *git* creates files needed for git projects
- *python* creates files need for python projects
- *all* creates files for git and python but doesn't include setup.py
- *setup* creates a template setup.py

``pystarter clean``

This command removes compiled python (*pyc*) files and *pycache* folders in your project

To get full command list run:

``pystarter -h``

or

``pystarter --help``


## Authors

1. [Rafael Cenzano](https://github.com/RafaelCenzano)


## License

This project is licensed under the MIT [License](LICENSE.txt)
