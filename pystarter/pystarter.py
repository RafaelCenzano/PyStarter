def findVenv():
    # import os
    try:
        from os import path, listdir, getcwd
    except BaseException:
        print('Error with importing os')
        exit()

    command_path = getcwd()

    for item in listdir(command_path):
        if path.isdir(item):
            print('dirs ' + str(item))
            for dirs in listdir(path.join(command_path, item)):
                if path.isdir(path.join(command_path, item, dirs)):
                    print('dirs ' + str(item) + ' in ' + str(dirs))
                    if dirs == 'bin' or dirs == 'Scripts':
                        return item
    return None


def pystarterVersion():
    return '1.3.0'


def pystarterCommands():
    return ('''
The command is used like this:
pystarter create <option>

option can be left blank

Options you can use (do not use <> in command arguments):
    <git> for git only projects
    <python> for python only projects
    or leave it blank for for projects with git and python
           ''')


def cacheCleaner():
    import os
    import shutil

    pathsToRemoveFiles = []
    pathsToRemoveDirs = []
    pathToFolder = os.getcwd()

    for (root,dirs,files) in os.walk('.', topdown=True):
        dirsChecking = root[2:]
        if root[2:6] != 'venv':
            for directories in dirs:
                if '__pycache__' == directories:
                    pathsToRemoveDirs.append(os.path.join(pathToFolder,dirsChecking,directories))
            for f in files:
                name, ext = os.path.splitext(f)
                if '.pyc' == ext:
                    pathsToRemoveFiles.append(os.path.join(pathToFolder,dirsChecking,f))
    for paths in pathsToRemoveFiles:
        if os.path.exists(paths):
            os.remove(paths)
    for paths in pathsToRemoveDirs:
        if os.path.exists(paths):
            shutil.rmtree(paths)