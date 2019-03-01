# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 错误的思路，这样12位数以下还可以，20位太慢了
# def smallest_multiple(n):
#     num = 1
#     flag = 0
#     while flag!=n:
#         num+=1
#         for i in range(1,n+1):
#             # print("i=",i )
#             if num % i != 0:
#                 flag = 0
                
#             else:
#                 flag+=1
#                 # print("@:",num)

#     print("#:",num)

def biggest_common(a,b):
    result = 1
    small = 1
    if a < b:
        small = a
    else:
        small = b

    for i in range(1,small+1):
        if a % i == 0 and b % i ==0:
            result = i
    print('bigggestcommon=',result)
    return result

def smallest_multiple(a,b):
    c = biggest_common(a, b)
    a1 = a//c
    b1 = b//c
    print("a=",a,"b=",b,"c=",c,a1,b1)
    return c*a1*b1

def find_smallest_multiple(n):
    result = 1
    for i in range(1, n+1):
        result = smallest_multiple(i,result)
        print(result)

if __name__ == "__main__":
    find_smallest_multiple(20)
