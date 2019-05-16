'''

Investigating the Torricelli point of a triangle

Problem 143
Let ABC be a triangle with all interior angles being less than 120 degrees. 

Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, 

BNC and AMC are constructed on each side of triangle ABC, the circumscribed circles of

 AOB, BNC, and AMC will intersect at a single point, T, inside the triangle. Moreover he proved that T, 

 called the Torricelli/Fermat point, minimises p + q + r. Even more remarkable, 

 it can be shown that when the sum is minimised, AN = BM = CO = p + q + r and that AN, 

 BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall 

call triangle ABC a Torricelli triangle. For example, a = 399, b = 455, 

c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli triangles.

#----------------------------#

欧拉工程143: 三角形托里拆利点的研究

三角形ABC的每一个内角均小于120度，取三角形内的任意一点X满足XA = p，XC = q以及XB = r。

费马曾经向托里拆利提出挑战，找到点X的位置，使得p + q + r最小。

托里拆利证明了，如果对三角形ABC的三边分别构造等边三角形AOB，BNC和AMC，这三个三角形的外接圆将会交于三角形内一点T。
T点，也被称为托里拆利点或费马点，是使得p + q + r最小的点。更神奇的是，此时AN = BM = CO = p + q + r，且AN，BM和CO相交于点T。


如果当和最小时有a，b，c，p，q，r均为正整数，我们称这个三角形ABC为托里拆利三角形。例如，a = 399，b = 455，
c = 511就是托里拆利三角形的一个例子，此时p + q + r = 784。

对于所有满足p + q + r ≤ 120000的托里拆利三角形，求所有不同的p + q + r的值之和。


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
