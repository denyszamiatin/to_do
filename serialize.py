import pickle

def list_serialize(data, file_name):
    if type(data) is list:
        pickle.dump(data,open(file_name,'w'))
        return True
    else:
        return False

def list_deserialize(file_name):
    try:
        return pickle.load(open(file_name,'r'))
    except IOError:
        return None
