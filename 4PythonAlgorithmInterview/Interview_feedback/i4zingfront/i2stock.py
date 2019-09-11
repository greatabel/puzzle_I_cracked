'''

设计一个股票模拟交易系统。假设我们有一个很牛叉的AI系统，已经预测到未来一段时间内给定股票的价格，

以数组来表示，它的第i个元素是一支给定的股票在第i天的价格。 
假设: 
1. 如果你最多只允许完成两次交易(一次交易是指:买入和卖出); 
2. 你有本金K单位(K >= 1)，一单位本金可以购买1股票;这意味着你寻找的是K单位本金条件下最大利润。
 提示:K = 1的时候最简单，可以先考虑。 
设计一个算法来找出最大利润。 

#----------------------------#

分析：其实可以理解成一段离散点组成的价格升降曲线（近似），
    先考虑单次交易的情况，就是在这段曲线上找到从最小点到最高点直接到最大距离（当然中间可能有下降，只要全局最大即可）
    然后2次交易的情况，只是在整个价格升降曲线上找到一个分割点，在价格曲线开始到分割点的利润总和+
    分割点到价格曲线末尾的利润总和

时间复杂度：价格列表的长度假设为n，单论遍历为n，但是总的最大值需要每一个位置开始进行单轮，
            所以总的平均时间复杂度为o(n^2)
空间复杂度：只增加了存储临时最大值的imax和是否需要局部布长的和gap，临时分段利润和profits 2个值，
        其他 istart， iend，flag 可以不需要，只是为了清晰显示具体操作。
        空间复杂度是 常数级别的

'''
import random
import time


limit = 100
k = 1 # 股数 可以设置为任意值，只考虑单股是简化
flag = False


def single_turn(pricelist):
    global flag
    imax = 0
    gap = 0

    istart = 0
    iend = 0
    for i in range(len(pricelist)-1):

        gap_step = pricelist[i+1] - pricelist[i]
        gap += gap_step
        if gap < 0:
            gap = 0
            if iend > istart:
                istart = i+1
        if gap > imax:
            imax = gap
            iend = i+1
    # 只是显示一下实际是怎么操作的，其实可以注释掉：
    if flag:
        print('开始买入在', pricelist[istart], '，卖出在', pricelist[iend], '',
            '每股赚取了:', imax)
    return imax


def main_process():
    global flag
    prices_per_day = random.sample(range(1, limit), 9)
    print('每日价格数据为：', prices_per_day)
    # s = single_turn(prices_per_day)
    # print(s)
    turn_num = 2
    profits = [0] * turn_num
    imax = 0
    split_indx = 0
    for i in range(2, len(prices_per_day)-1):
        profits[0] = single_turn(prices_per_day[:i])
        profits[1] = single_turn(prices_per_day[i:])
        if sum(profits) > imax:
            imax = sum(profits)
            split_indx = i
    print('2轮真正分割为第', split_indx+1, '天，价格位置', prices_per_day[split_indx])
    print('总最大利润：', imax)

    #以下主要为显示每一轮实际怎么操作的
    flag = True
    print('第一轮操作：')
    single_turn(prices_per_day[:split_indx])
    print('第二轮操作：')
    single_turn(prices_per_day[split_indx:])

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





