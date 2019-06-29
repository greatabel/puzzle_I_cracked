'''

Exploring strings for which only one character comes lexicographically after its neighbour to the left

Problem 158
Taking three different letters from the 26 letters of the alphabet, character strings of length three can be formed.
Examples are 'abc', 'hat' and 'zyx'.
When we study these three examples we see that for 'abc' two characters come lexicographically after its neighbour to the left.
For 'hat' there is exactly one character that comes lexicographically after its neighbour to the left. For 'zyx' there are zero characters that come lexicographically after its neighbour to the left.
In all there are 10400 strings of length 3 for which exactly one character comes lexicographically after its neighbour to the left.

We now consider strings of n ≤ 26 different characters from the alphabet.
For every n, p(n) is the number of strings of length n for which exactly one character comes lexicographically after its neighbour to the left.

What is the maximum value of p(n)?


#----------------------------#

按字典序升序排列的字符串研究

从字母表的26个字母中取出三个不同的字母，可以组成一个长度为3的字符串。
这样的例子包括’abc’，’hat’和’zyx’。
可以发现，对于字符串’abc’，有两个字符与其左侧字符是按照字典序升序排列的。
对于字符串’hat’，只有一个字符与其左侧字符是按照字典序升序排列的，而对于字符串’zyx’则不存在这样的字符。
总共有10400个长度为3的字符串，其中恰好有一个字符与其左侧字符是按照字典序升序排列的。

现在考虑由字母表中的n ≤ 26个不同字符组成的字符串。
对于任意n，我们用p(n)表示长度为n且恰好有一个字符与其左侧字符是按照字典序升序排列的字符串数目。

p(n)的最大值是多少？


'''




import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





