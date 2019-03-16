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
'''

import time
from termcolor import colored


def main_process():
    print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)














