'''

For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)

#----------------------------#

欧拉工程160 阶乘的尾数

对于任意N，记f(N)为N!除去末尾零后的最后五位数字。
例如，

9! = 362880，所以f(9)=36288
10! = 3628800，所以f(10)=36288
20! = 2432902008176640000，所以f(20)=17664

求f(1,000,000,000,000)

#----------------------------#
skip this problem ,use solution from nayuki
'''




import time
from termcolor import colored


def count_factors(end, n):
    if end == 0:
        return 0
    else:
        return end // n + count_factors(end // n, n)

# The product of {all numbers from 1 to n that are coprime with 10}, modulo 10^5.
# The input argument can be taken modulo 10^5 because factorialoid(10^5) = 1, 
# and each block of 10^5 numbers behaves the same.
def factorial_coprime(n):
    n %= 100000
    product = 1
    for i in range(1, n + 1):
        if i % 2 != 0 and i % 5 != 0:
            product = i * product % 100000
    return product

# Equal to n! but with all factors of 2 and 5 removed and then modulo 10^5.
# The identity factorialIsh(n) = odd_factorialish(n) * even_factorialish(n) (mod 10^5) is true by definition.
def factorialish(n):
    return even_factorialish(n) * odd_factorialish(n) % 100000


# The product of {all even numbers from 1 to n}, but with all factors of 2 and 5 removed and then modulo 10^5.
# For example, even_factorialish(9) only considers the numbers {2, 4, 6, 8}. Divide each number by 2 to get {1, 2, 3, 4}. Thus even_factorialish(9) = factorialish(4).
def even_factorialish(n):
    if n == 0:
        return 1
    else:
        return factorialish(n // 2)


# The product of {all odd numbers from 1 to n}, but with all factors of 2 and 5 removed and then modulo 10^5.
# By definition, odd_factorialish() never considers any number that has a factor of 2. The product of the numbers that not a multiple of 5 are accumulated by factorial_coprime().
# Those that are a multiple of 5 are handled recursively by odd_factorialish(), noting that they are still odd after dividing by 5.
def odd_factorialish(n):
    if n == 0:
        return 1
    else:
        return odd_factorialish(n // 5) * factorial_coprime(n) % 100000


def main_process():
    limit = 10 ** 12
    n = limit
    twos = count_factors(n, 2) - count_factors(n, 5)  # Always non-negative for every n
    # We can reduce 'twos' because there is a cycle: 2^5 = 2^2505 = 32 mod 100000
    if twos >= 2505:
        twos = (twos - 5) % 2500 + 5
    r = factorialish(n) * pow(2, twos, 100000) % 100000
    print(colored('mycount=', 'red'), r)
    # mycount= 16576


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





