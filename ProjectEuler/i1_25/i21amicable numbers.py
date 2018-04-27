# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def divisorGenerator(n):
    for i in range(1,int(n/2)+1):
        if n%i == 0: 
            yield i

    

def find_amicable(num):
    mydict = {}
    for i in range(1,num):
        thesum = sum(list(divisorGenerator(i)))
        mydict[i] = thesum
        # 理解错误版本
        # if thesum not in mydict:
        #     mydict[thesum] = str(i)
        # else:
        #     mydict[thesum] = mydict[thesum]+"," + str(i)
    # print(mydict)
    thelist = []
    for key, value in mydict.items():
        if key !=1:
            # print(key,"#",value)
            for k,v in mydict.items():
                if mydict[key] == k and key == mydict[k] and k!=v and k not in thelist:
                    thelist.append(k)
                    thelist.append(v)
                    print("#",k,v)
    print("sum:",sum(thelist))



if __name__ == "__main__":
    find_amicable(10000)