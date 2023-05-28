with open('files.txt', encoding='UTF-8') as f:
    space = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
    def converter(x):
        for i in space.keys():
            if 1 < x < 1024:
                return f'{int(round(x))} {i}'
            else:
                x = x / 1024
    files = [i.split() for i in f.readlines()]
    filesdict = {}
    for i in files:
        filesdict.setdefault(i[0].split('.')[1], []).append(i)
    for k, v in sorted(filesdict.items()):
        sumkb = 0
        for i in sorted(v, key=lambda x: x[0]):
            print(i[0])
            sumkb += int(i[1]) * space[i[2]]
        print(f"{'-' * 10}\nSummary: {converter(sumkb)}\n")