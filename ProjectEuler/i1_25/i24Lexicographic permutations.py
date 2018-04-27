
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# answer is :2783915460
import time

# def permutaion(elements,divider):
#     if len(elements) == 0:
#         print(divider)
#     else:
#         for i in range(len(elements)):
#             permutaion(elements[0:i] + elements[i+1:], divider + str(elements[i]))

rs = []
def permutaion(elements,divider):
    if len(elements) == 0:
        # print(divider)
        rs.append(divider)        
    else:
        for i in range(len(elements)):
            permutaion(elements[0:i] + elements[i+1:], divider + str(elements[i]))


def find_permutations(start, end):
    elements = list(range(start, end+1))
    permutaion(elements, "")
    



if __name__ == "__main__":
    tic = time.clock()
    find_permutations(0,9)
    print("rs=",rs[1000000-1])

    toc = time.clock()
    print("time=",toc - tic)