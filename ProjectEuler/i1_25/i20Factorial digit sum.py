# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def digits_sum(num):
    total = 1
    for i in range(1,num+1):
        # print(i)
        total *= i
    print(total)
    count = 0
    while total > 0:
        remain = total % 10
        print("remain=",remain)
        count += remain
        total = int(total//10)
    print(count)
    


if __name__ == "__main__":
    digits_sum(100)