def txt_to_dict():
    with open('./data_file/planets.txt') as file:
        res = {}
        f = ((x[0], x[2]) for i in file if len((x := i.strip().split())) > 0)
        for k, v in f:
            if len(res) == 4:
                yield res
                res = {}
            res[k] = v
        yield res



planets = txt_to_dict()
print(*planets)