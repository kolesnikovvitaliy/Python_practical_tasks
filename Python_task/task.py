from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if from_left:
        if key in chainmap:
            return chainmap[key]
    else: 
        if key in chainmap:
            return [i[key] for i in reversed(chainmap.maps) if key in i][0]
    return


    # for dicts in chainmap.maps:
    #     for k, v in dicts.items():
    #         if key == k:
    #             dicts[k] = value
    # return



chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))
