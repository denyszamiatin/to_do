import pickle
import setting

def serialize_tasks(tasks, file_name = setting.file_name):
    with open(file_name, 'w') as f:
        pickle.dump(tasks, f)


def deserialize_tasks(file_name = setting.file_name):
    with open(file_name, 'r') as f:
        try:
            return pickle.load(f)
        except IOError:
            return Exception('File not found')
