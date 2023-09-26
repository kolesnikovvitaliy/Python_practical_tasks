with open('./data_file/data.csv', 'r', encoding='utf-8') as file:
    lines = (i.rstrip() for i in file.readlines())
    next(lines)
    result = sum(int(x[1]) for i in lines if (x := i.split(','))[2] == 'a')
    print(result)