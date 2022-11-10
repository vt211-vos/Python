class NameLengthError(Exception):
    pass

def average(name):
    if len(name) <= 10:
        raise NameLengthError('Name should be more then 10')
    return name

def CheckName(name):
    try:
        value = average(name)
    except NameLengthError:
        print('Name should be more then 10')
    else:
        return value
CheckName("qwecvnb")

