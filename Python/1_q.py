import io, hashlib, hmac


def my_func(a, b):
    ha = hashlib.sha1(a.encode("utf-8")).hexdigest()
    print(ha)
    hb = hashlib.sha1(b.encode("utf-8")).hexdigest()
    print(hb)
    return ha == hb


print(my_func("a", "a"))
