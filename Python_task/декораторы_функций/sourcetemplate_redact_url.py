def sourcetemplate(url):
    def func(**kwargs):
        if not kwargs:
            return url
        return url+'?'+'&'.join((map(
            lambda x: f'{x[0]}={x[1]}', sorted(kwargs.items()))))
    return func