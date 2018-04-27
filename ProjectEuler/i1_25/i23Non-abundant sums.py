
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import time

def divisorGenerator(n):
    # print("divisorGenerator ",n)
    for i in range(1,int(n/2)+1):
        if n%i == 0: 
            # print(i)
            yield i

def is_abundant(number):
    thesum = sum(list(divisorGenerator(number)))
    if thesum > number:
        return True
    else:
        return False

def  find_abundant_below_num(num):
    myset = set()
    for number in range(1,num):
        if is_abundant(number):
            myset.add(number)
    print("find_abundant_below_num:",len(myset))
    return myset

def generate_number_whoIs2abundantSum(abundants,limit):
    the2sumSet = set()
    for x in abundants:
        for y in abundants:
            if x + y < limit:
                the2sumSet.add(x+y)
    print(len(the2sumSet))
    thesum = 0
    for i in range(1,limit):
        thesum += i
    print('thesum=',thesum,thesum - sum(the2sumSet))




if __name__ == "__main__":
    tic = time.clock()
    myset = find_abundant_below_num(28124)
    toc = time.clock()
    print(toc - tic)
    generate_number_whoIs2abundantSum(myset,28124)