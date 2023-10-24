from collections import defaultdict


def flip_dict(dict_of_lists):
    result_dict = defaultdict(list)
    [result_dict[i].append(k) for k, v in dict_of_lists.items() for i in v]
    return result_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))