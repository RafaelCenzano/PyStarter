class Error(Exception):
   # Base class for other exceptions
   pass

class MissingValue(Error):
   # Raised when value is missing
   pass

def versionFind(type='int'):
    import platform

    version = platform.python_version()
    version_split = version.split('.')
    main_version = version_split[0]
    try:
        sub_version = version_split[1]
    except:
        sub_version = None

    try:
        sub_sub_version = version_split[2]
    except:
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
    from os import path, listdir, getcwd

    path = getcwd()

    dirs = []

    for items in listdir(path):
        if path.isdiir(items):
            dirs.apphend(items)

    if 'venv' in dirs:
        return 'venv'
    elif 'env' in dirs:
        return 'env'
