# Imports
import sys


def versionFind(type='int'):
    version_tuple = sys.version_info
    print(version_tuple)
    print(type)

def pystarterVersion():
    return '0.1.6'

def pystarterCommands():
    return ('''

Usage:
  pystarter <command> [options]

Commands:
  create             Create all needed files for a git and python project
                         default option creates git and python files

Command Options:
  python             Create project ready for python only
  git                Create project ready for git only'

'General Options:

  --help, -h         Show help
  --version, -v      Show PyStarter version
            ''')
