# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def find(n):
    result = 0

    for i in range(1,n+1,2):
        step = i - 1
        edge = i
        print('edge=',i,'step=',step)
        start = (edge - 2 )**2 + step
        if i == 1:
            print(i)
            result += i
        else:
            print(start, start + step, start + step *2 , start + step * 3)
            result += (start + (start + step) + (start + step *2) + (start + step *3) )

    print('f(',n,')=', result)
        

if __name__ == "__main__":
    find(1001)