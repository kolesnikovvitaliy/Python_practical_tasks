def parse_ranges(ranges):
    split_by_commas = (i for i in ranges.split(','))
    split_by_a_line = (i.split('-') for i in split_by_commas)
    make_integers = ((int(k), int(v)+1) for k, v in split_by_a_line)
    parse_ranges = (j for k, v in make_integers for j in range(k, v))
    return parse_ranges

# def parse_ranges(ranges: str):
#     for r in ranges.split(","):
#         start, end = map(int, r.split("-"))
#         yield from range(start, end+1)