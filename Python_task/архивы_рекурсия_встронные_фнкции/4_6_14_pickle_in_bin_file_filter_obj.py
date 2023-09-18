import pickle


def filter_dump(filename: str, objects: object, typename: type):
    obj = [item for item in objects if isinstance(item, typename)]
    with open(filename, mode='wb') as file:
        pickle.dump(obj, file)