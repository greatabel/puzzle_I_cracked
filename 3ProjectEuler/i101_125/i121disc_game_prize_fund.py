'''
A bag contains one red disc and one blue disc. 
In a game of chance a player takes a disc at random and its colour is noted. 
After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is exactly 11/120, 
and so the maximum prize fund the banker should allocate for winning in this game 
would be £10 before they would expect to incur a loss. 

Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game,
so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

翻译：
欧拉工程 欧拉项目 121：
一个包包含一个红色圆盘和一个蓝色圆盘。 在游戏中，一次中玩家随机拿出一个圆盘并记录其颜色。 
每轮之后，圆盘送回到包中，添加一个额外的红色圆盘，随机再拿出另一张圆盘。

玩家需要支付1英镑才能开始玩这个游戏，只有：玩家在游戏结束时拍记录的蓝色圆盘多于红色圆盘，则才能算赢得比赛。

如果游戏进行了4轮比赛，那么玩家获胜的概率恰好是11/120，因此银行家在这场比赛中应该分配的最高奖金将是10英镑，
否则再增加奖金就会产生损失。 请注意，任何支付都将是一个整数磅，并且还包括为玩游戏而支付的原始£1，
因此在给出的示例中，玩家实际上赢得了9英镑。
如果玩15个回合，找出能分配给单个游戏的最大奖金。

'''

'''
思路分析：
if   第1轮，拿出来是蓝色的概率就是1/2
if   第2轮，拿出来是蓝色的概率就是1/3
if   第3轮，拿出来是蓝色的概率就是1/4
if   第4轮，拿出来是蓝色的概率就是1/5
if   第n轮，拿出来是蓝色的概率就是1/n+1


分析下只进行4轮比赛的情况：蓝色的计数需要 > 4/2，于是需要蓝色计数是 3 或者 4
3，4个蓝色的情况如下： 0代表那一轮选择了红色，1代表那一轮选择了蓝色
第1轮  第2轮 第3轮 第4轮  概率可能性
0       1    1     1    1/2 * 1/3 * 1/4  * 1/5
1       0    1     1    1/2 * 2/3 * 1/4  * 1/5
1       1    0     1    1/2 * 1/3 * 3/4  * 1/5
1       1    1     0    1/2 * 1/3 * 1/4  * 4/5
1       1    1     1    1/2 * 1/3 * 1/4  * 1/5

概率之和 11 /120

我们如果追求的是终极无限的平衡（也就是平局），玩家付出了1英镑，我们设置一个奖金数刚好概率上用户玩4轮
能把1英镑赚回去，那么是：
1 / (11/ 120) 约= 10.909
由于只能是整数，如果设置成11，庄家长期看是亏本，为了不亏本，设置成10英镑

接下来我们分析一般情况：
对于k轮之后， 我们假设j 个蓝色的个数 为 f(k, j)
初始状态下 f(1轮， 0个蓝色) = 1  f(1轮， 1个蓝色) = 1
f(k+1, j+1) 我们第 k+1个盘子 要么是红色  要么是蓝色，于是：
k+1 是蓝色的话，还是只有从包中唯一的1个蓝色，1个蓝色, 只有1个选法，这种情况有：1 * f(k,j)
k+1 是红色的话，这个红色可以在包里面的(k+1)个红盘中选择，有 (k + 1)个选法 ，这种情况有 (k+1) * f(k, j+1)
f(k+1, j+1) = f(k, j) + f(k, j+1) * (k + 1)
'''

from math import factorial
import time
from termcolor import colored


def main_process():
    n = 15

    f = {}
    for j in range(1, n + 1):
        for k in range(j + 1):
            # 不管那一轮，蓝色一个都没有，意味着全部都是红色
            # 这种情况的总个数，相当于第1轮从1个红色选，第2轮从2个，第3个从3个红色选……
            # 完全就是阶乘的情况
            if k == 0:
                f[(k, j)] = factorial(j)
            # 如果k轮有k个蓝色，意味着每一次选择都是蓝色，不管是哪一轮，这种情况只可能随着每一个
            # 轮数发生一次这种情形：1次蓝色，2次蓝色，3次蓝色，4次蓝色……n次蓝色，每种情况只会出现一种
            elif k == j:
                f[(k, j)] = 1
            # 其他情况就是 思路分析的迭代关系情况
            else:
                f[(k, j)] = (f[(k - 1, j - 1)] +
                                      j * f[(k, j - 1)])

    # 计算满足获胜的要求的情况
    blue_len = int((n / 2)) + 1
    count = 0
    for blue in range(blue_len, n + 1):
        count += f[(blue, n)]

    # 计算获胜概率
    r = count / factorial(n+1)
    print(colored('奖金设置为=', 'red'), int(1/r))
    # wrong : 172915618909
    # right:  2269

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)
