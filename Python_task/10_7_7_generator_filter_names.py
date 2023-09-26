def filter_names(names: list[str], ignore_char: str, max_names: int):
    filter_name_list = (i for i in names if i.isalpha() and
                        not i.lower().startswith(ignore_char.lower()))
    count = 0
    for i in filter_name_list:
        if count == max_names:
            return
        yield i
        count += 1
     # return (v for k, v in enumerate(filter_name_list) if k < max_names)
