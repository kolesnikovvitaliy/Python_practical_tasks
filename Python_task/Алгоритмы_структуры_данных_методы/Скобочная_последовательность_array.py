import sys
from array import array


def check_breackets(string: str):
    _lst = array('i')
    count = array('i')
    for index, item in enumerate(string, 1):
        if item in '({[':
            _lst.append(ord(item))
            count.append(index)
        elif _lst and ord(item) - _lst[-1] in (1, 2):
            _lst.pop()
            count.pop()
        elif item not in '({[]})':
            continue
        else:
            return index

    if not _lst:
        return 'Success'
    return count[-1]


if __name__ == '__main__':
    string = sys.stdin.read().strip()
    print(check_breackets(string))

    assert check_breackets("([](){([])})") == 'Success'
    assert check_breackets("()[]}") == 5
    assert check_breackets("{{[()]]") == 7
    assert check_breackets("{{{[][][]") == 3
    assert check_breackets("{*{{}") == 3
    assert check_breackets("[[*") == 2
    assert check_breackets("{*}") == 'Success'
    assert check_breackets("{{") == 2
    assert check_breackets("{}") == 'Success'
    assert check_breackets("") == 'Success'
    assert check_breackets("}") == 1
    assert check_breackets("*{}") == 'Success'
    assert check_breackets("{{{**[][][]") == 3
    assert check_breackets("((({[]})") == 2
    assert check_breackets("{}([]") == 3
    assert check_breackets("(slkj, {lk[lve]} ,l)") == 'Success'
    assert check_breackets("(slkj{lk[lsj]}") == 1
    assert check_breackets("dasdsadsadas]]]") == 13