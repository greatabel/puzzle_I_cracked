'''


numpy
pandas
scipy

tensorflow
keras
等深度学习模型

常用数据挖掘算法

复杂时序序列预测优先


#----------------------------#



'''

import time
from termcolor import colored
import numpy as np



def main_process():
    res = '''
    https://www.infoq.cn/article/UB7YFmdUoNO*MeDHomho

    1. 如何理解过拟合？

    过拟合和欠拟合一样，都是数据挖掘的基本概念。过拟合指的就是数据训练得太好，在实际的测试环境中可能会产生错误，
    所以适当的剪枝对数据挖掘算法来说也是很重要的。
    欠拟合则是指机器学习得不充分，数据样本太少，不足以让机器形成自我认知

    2. 为什么说朴素贝叶斯是“朴素”的？

    朴素贝叶斯是一种简单但极为强大的预测建模算法。之所以称为朴素贝叶斯，
    是因为它假设每个输入变量是独立的。这是一个强硬的假设，实际情况并不一定，
    但是这项技术对于绝大部分的复杂问题仍然非常有效。

    3. SVM 最重要的思想是什么？
    SVM 计算的过程就是帮我们找到超平面的过程，它有个核心的概念叫：分类间隔。
    SVM 的目标就是找出所有分类间隔中最大的那个值对应的超平面。
    在数学上，这是一个凸优化问题。同样我们根据数据是否线性可分，
    把 SVM 分成硬间隔 SVM、软间隔 SVM 和非线性 SVM

    5.K-Means 和 KNN 算法的区别是什么？

    首先，这两个算法解决的是数据挖掘中的两类问题。
    K-Means 是聚类算法，KNN 是分类算法。
    其次，这两个算法分别是两种不同的学习方式。
    K-Means 是非监督学习，也就是不需要事先给出分类标签，而 KNN 是有监督学习，
    需要我们给出训练数据的分类标识。最后，K 值的含义不同。
    K-Means 中的 K 值代表 K 类。KNN 中的 K 值代表 K 个最接近的邻居
    
    -----------------------
    https://cloud.tencent.com/developer/article/1061741

    6. 例举几个常用的python分析数据包及其作用?

　　可视化：数据处理和分析：NumPy, SciPy, Pandas
　　机器学习：sklearn
　　可视化： Matplotlib, Seaborn
    
    7.  如何利用Numpy对数列的前n项进行排序
    使用argsort()函数：x[x [: n-1].argsort ()]

    8. 如何检验一个数据集或者时间序列是随机分布的
    画lag plot（Correlogram：相关图），如果图上的点呈散乱分布，则为随机

    9. 在python中如何创建包含不同类型数据的dataframe
    利用pandas包的DataFrame函数的serias创建列然后用dtype定义类型：
    df = pd.DataFrame({'x': pd.Series(['1.0', '2.0', '3.0'], dtype=float), 
        'y': pd.Series(['1', '2', '3'], dtype=int)})
    
    10 Pandas中使用的标准数据缺失标志是什么
    NaN 

    11 描述numpy array比python list的优势

    a. numpy array比python list更紧凑，存储数据占的空间小，读写速度快。
    (这是由于python  
        list储存的是指向对象（至少需要16个字节）的指针（至少4个字节）；
        而array中储存的是单一变量（比如单精度浮点数为4个字节，双精度为8）
    b. array可以直接使用vector和matrix类型的处理函数，非常方便

    -----------------------
    41道 Machine Learning 高频面试题
    https://www.dataapplab.com/machine-learning-interview-questions/


    '''
    print(res)

    x = np.random.rand(10)
    print(x)
    n = 5
    print(x[x [: n].argsort ()])


if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)