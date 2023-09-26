def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = (x for i in f if (x := i.strip()) != '')
        yield from (i if len(i) <= 25 else '...' for i in lines)

# def nonempty_lines(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         lines = (j for i in f.readlines() for j in i.strip() != '')
#         line = (i for i in lines if i != '')
#         return (i if len(i) <= 25 else '...' for i in line)
