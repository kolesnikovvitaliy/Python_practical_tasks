def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    elif b >= a:
        return gcd(a, b % a)


    # while b:    
    #     a, b = b, a % b
    # print(a)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
