from array import array


def fib_mod(n, m):
    left, right, _lst = 0, 1, array('i', [0, 1])
    for i in range(1, n):
        left, right = right, (left + right) % m
        if left == 1 and right == 0:
            break
        _lst.append(right)

    index = n % len(_lst)
    return _lst[index]

# 2
# def fib_mod(x, y):
#     if x == 0:
#         return x, 1
#     a, b = fib_mod(x // 2, y)
#     if x % 2:
#         return (a * a + b * b) % y, ((2 * a + b) * b) % y
#     return ((2 * b - a) * a) % y, (a * a + b * b) % y


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))  # 1
#     print(fib_mod(n, m)[0]) # 2


if __name__ == "__main__":
    main()
