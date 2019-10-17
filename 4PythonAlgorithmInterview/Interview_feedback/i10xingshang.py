'''
原题：（现又i张10元纸币，k张五元纸币，j张两元纸币， 购物后要支付n元）
i,j,k不是升序或者降序，偶调整下了顺序：
原题：（现又i张10元纸币，j张五元纸币，k张两元纸币， 购物后要支付n元） -- abel 2019-10-17
'''

import time
from termcolor import colored
import random


def findsolution(i, j, k, n):
    '''
    思路：
    n % 2 == 1 
        考虑十位以下的情况：
        当n为奇数，个数上必须有且只能有1个5元在个位，m的个位数上2元数目是固定的： t2single = (n % 10 - 5) // 2
        除此之外的2元全部都可以换10元：t2 = (k - t2single) * 2 // 10      

        考虑十位以上的情况：
            所有5元可以组成10的个数 total5 =  5 * j // 10
        需要 i + total5 + t2 >= n//10：
            1） 手上10元足够自己就足够 i >=  n//10 : 支付 (n//10, 1, t2single)
            2)  需要10元和5元凑十位以上 i <  n//10 ，(n - 10 * i)//5 <= j时：支付(i, (n-10*i)//5, t2single)
            3)  需要10元，5元，2元凑十位以上: i < n//10 and j<(n-10*i)//5 :支付（i,j, (n-10*i-5*j)/2 + t2single)

    n % 2 == 0
        考虑十位以下的情况：
            n位偶数，个位不能含有5元，否则怎么都凑不齐，所以个位只能有： t2single = (n%10) // 2
            其余的2元全部可以变成10远：t2 = (k-t2single) * 2 // 10

        考虑十位以上的情况：
            所有5元可以组成10的个数 total5 =  5 * j // 10
        需要 i + total5 + t2 >= n//10:
            1） 手上10元足够自己就足够 i >=  n//10 : 支付 (n//10, 0, t2single)
            2)  需要10元和5元凑十位以上 i <  n//10 ，(n - 10 * i)//5 <= j时：支付(i, (n-10*i)//5, t2single)
            3)  需要10元，5元，2元凑十位以上: i < n//10 and j < (n-10*i)//5 :支付（i,j, (n-10*i-5*j)/2 + t2single)
    '''

    total5= 5 * j // 10
    if n % 2 == 1:
        if n % 10 <5:
            print("不能刚好够 n元")
        else:
            t2single = (n % 10 - 5) // 2
            t2 = (k - t2single) * 2 // 10
            if n // 10 > i + total5+ t2:
                print("不能刚好够 n元")
            else:
                if n // 10 <=i:
                    print(f"使用{n // 10}张10元，{1}张5元，{t2single}张2元，刚好够{n}元")
                else:
                    if (n - 10 * i) // 5 <= j:
                        print(f"使用{i}张10元，{(n - 10 * i) // 5}张5元，{t2single}张2元，刚好够{n}元")
                    else:
                        print(f"使用{i}张10元，{j}张5元，{t2single + (n - 10 * i - 5 * j) / 2}张2元，刚好够{n}元")
    else:
        t2single = (n % 10) // 2
        t1 = (k - t2single) * 2 // 10
        if n // 10 > i + total5+ t1:
            print("不能刚好凑齐 n元")
        else:
            if n // 10 <= i:
                print(f"使用{n // 10}张10元，{0}张5元，{t2single}张2元，刚好够{n}元")
            else:
                if (n - 10 * i) // 5 <= j:
                    print(f"使用{i}张10元，{(n - 10 * i) // 5}张5元，{t2single}张2元，刚好够{n}元")
                else:
                    print(f"使用{i}张10元，{j}张5元，{t2single + (n - 10 * i - 5 * j) / 2}张2元，刚好够{n}元")


if __name__ == "__main__":
    for i in range(10):
        n = random.randint(1, 100)
        i = random.randint(1, 100)
        j = random.randint(1, 100)
        k = random.randint(1, 100)
        print(i,"个10元 ", j, "个5元", k, "个2元时 ", colored("希望凑总数：", "red"), n, "元 ？")
        tic = time.process_time()
        # testcase: 2张10元， 1张5元，1张2元凑 27元零钱
        # findsolution(2, 1, 1, 127)
        # testcase: 10张10元， 5张5元，3张2元凑 127元零钱

        findsolution(i, j, k, n)
        toc = time.process_time()
    print("time=",toc - tic)





