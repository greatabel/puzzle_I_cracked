# 减法版本
def gcd(a, b):
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

#除法版本
def gcd_divide(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if __name__ == "__main__":
    for item in [(252, 105), (21, 14), (99, 2233)]:
        r = gcd(item[0], item[1])
        r_d = gcd_divide(item[0], item[1])
        print(r, ' r_d=', r_d)