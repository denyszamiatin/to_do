import pickle


def list_serialize(data, file_name):
    """Return boolean result of writing data to file

    Keyword arguments:
    data - list of info to write
    file_name - string path to file
    
    >>> list_serialize([], 'test.txt')
    True
    >>> list_serialize((1,2,3), 'test.txt')
    False
    """
    if type(data) is list:
        pickle.dump(data, open(file_name, 'w'))
        return True
    else:
        return False


def list_deserialize(file_name):
    """Return unserialized data from file
    
    Keyword arguments:
    file_name - string path to file
    """
    try:
        return pickle.load(open(file_name, 'r'))
    except IOError:
        return None
