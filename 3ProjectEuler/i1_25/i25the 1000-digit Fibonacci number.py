# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import time
# http://ujihisa.blogspot.jp/2010/11/memoized-recursive-fibonacci-in-python.html

# def permutaion(elements,divider):
#     if len(elements) == 0:
#         print(divider)
#     else:
#         for i in range(len(elements)):
#             permutaion(elements[0:i] + elements[i+1:], divider + str(elements[i]))

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


__fib_cache = {}
def fib_v2(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib_v2(n-2) + fib_v2(n-1)
        return __fib_cache[n]

def find(n):
    i = 0
    result  = fib(i)
    mylen = len(str(result))
    while mylen < n:
        i += 1
        result = fib(i)
        mylen = len(str(result))
        
        print('#',i,fib(i),len(str(fib(i))))
    print(i,fib(i),len(str(fib(i))))

def find_v2(n):
    i = 0
    result  = fib_v2(i)
    mylen = len(str(result))
    while mylen < n:
        i += 1
        result = fib_v2(i)
        mylen = len(str(result))
        if mylen % 10 == 0:
            print('#',i,fib_v2(i),len(str(fib_v2(i))))
    print(i,fib_v2(i),len(str(fib_v2(i))))


if __name__ == "__main__":
    tic = time.clock()
    # for i in range(0,20):
    #     print(i,fib(i),len(str(fib(i))))
    find_v2(1000)

    toc = time.clock()
    print("time=",toc - tic)