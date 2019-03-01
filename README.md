# puzzle_I_cracked
纪录所有我已经解决的比较有意思的谜题，问题，小项目。

1.https://glowing.com/jobs/mobiledeveloper 的红蓝块移动路径问题:

Q:There're 7 red tiles, 8 blue titles and one white title in a 4 x 4 plane. We could only move the white tile. When moving it, the white tile swaps the position with the adjacent tile. L, R, U, D are corresponding to four directions which the tile could be moved to (Left, Right, Up, Down) For example, starting from configuration (S), by the move sequence RDRDL we reach the configuration (E). Now, starting from configuration (S), find the shortest way to reach configuration (T).
<img src="/1Red Blue Puzzle/smallQuestion.png" alt="alt text" title="Title" />
Answer:解决方案的路径在”Red Blue Puzzle“文件夹下,python解决,记得2013年末那个星期好几个凌晨。

2.long time ago,Red-Black tree algorithm experiment:

Q：实现红黑树、二叉搜索树相关算法：插入（红黑树涉及树的调整：左旋、右旋等），删除，搜索（指定Key值节点）。 
        另外，红黑树实现计算树黑高的算法。 

        1).插入测试，输入 8，11，17，15，6，1，22，25，27，建立红黑树，按照 红黑树信息输出方式 输出整棵红黑树以及黑高。 
        2).删除测试，删除1）中红黑树中Key=15的节点，按照 红黑树信息输出方式 输出调整后的整棵红黑树以及黑高。 
        3).随机产生300,000个不同自然数Key值（1－300,000，每个数出现一次，出现顺序随机），建立红黑树，查找Key=15000的节点，输出查找花费时间。 
        随机产生300,000个不同自然数Key值（1－300,000），建立二叉搜索树，查找Key=15000的节点，输出查找花费时间。 
        4). 重复3－5次3）中操作，求各自平均时间。 
        5). 在1)－4)的红黑树算法基础上修改完成P307 14.1-4算法 OS_Key_Rank(T,k). 输入 1,2,3,4,5,6,7,8 建树， k=6, 输出OS_Key_Rank的返回值。
Answer：2008年我在网上找了半天，有用的资源太少了，作业只好自己做了，所以我就自己当时花了1天做这个作业，部分思路参考了google，代码在2Red-Black tree algorithm  experiment文件夹，java实现。

3.folder of 3ProjectEuler: 

All is about euler project, I am still working on it (not finished)
https://projecteuler.net/archives
