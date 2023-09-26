def unique(iterable):
    yield from (dict((k, None) for k in iter(iterable)))
