def fib(n):
    left, right = 0, 1
    for _ in range(1, n):
        left, right = right, left+right
    return right


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
