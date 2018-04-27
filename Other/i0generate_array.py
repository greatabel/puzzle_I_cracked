# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法

def AA(a, index):
    m = 1
    for i in range(0, index):
        m *= a[i]
    for i in range(index+1, len(a)):
        m *= a[i]
    return m

def solution(a):
    b = []
    for i in range(0,len(a)):
        b.append(AA(a, i))
    print('b=',b)




solution([2,3,4])
