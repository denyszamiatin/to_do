import pickle

def list_serialize(data, file_name):
    if type(data) is list:
        pickle.dump(data,open(file_name,'w'))
        return True
    else:
        return False
