# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# 图在：p15question.gif

# How many such routes are there through a 20×20 grid?

# 太慢了，得换个非递归方法
# def p(x,y):
#     print(x,y)
#     result = 0
#     if x == 0 and y == 0:
#         result = 0
#     elif (x == 0 or y == 0):
#         result = 1
#     else:
#         result = p(x - 1 , y) + p(x, y - 1)
#     return result


def p(x,y):
    resultArray = []
    for i in range(0,x):
        new = []
        for j in range(0,y):
            new.append(0)
        resultArray.append(new)
    print(resultArray,resultArray[1][1])
    for i in range(0,x):
        for j in range(0,y):
            print("i=",i," j=",j)            
            if i == 0 and j == 0:
                resultArray[i][j] = 0
            elif (i == 0 or j == 0):
                resultArray[i][j] = 1
            else:
                resultArray[i][j] = resultArray[i-1][j] + resultArray[i][j-1]
    print(resultArray)
    print('*'*10, resultArray[x-1][y-1])

    # return result

if __name__ == "__main__":
    p(21, 21)