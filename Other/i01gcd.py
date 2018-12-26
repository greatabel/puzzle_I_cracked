def gcd(a, b):
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == "__main__":
    for item in [(252, 105), (21, 14), (99, 22)]:
        r = gcd(item[0], item[1])
        print(r)