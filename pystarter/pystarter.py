def versionFind(type='int'):
    import platform

    version = platform.python_version()
    version_split = version.split('.')
    main_version = version_split[0]
    try:
        sub_version = version_split[1]
    except BaseException:
        sub_version = None

    try:
        sub_sub_version = version_split[2]
    except BaseException:
        sub_sub_version = None

    if type == 'int' or type == 'one' or type == 'first' or type == 1:
        return main_version

    elif type == 'second' or type == 'two' or type == 2:
        return main_version, sub_version

    elif type == 'third' or type == 'three' or type == 3:
        return main_version, sub_version, sub_sub_version

    elif type == 'str' or type == 'string':
        return version

    else:
        raise MissingValue


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


def Pythonfilecheck():
    pass


def pystarterCommands():
    return ('''
The command is used like this:
pystarter create <option>

option can be left blank

Options you can use (do not use <> in command arguments):
    <git> for git only projects
    <python> for python only projects
    or leave it blank for both python and git projects
    ''')
