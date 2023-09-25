def flatten(nested_list: list[list[int] | int]):
    if isinstance(nested_list, int):
        yield nested_list
    else:
        for i in nested_list:
            yield from flatten(i)
