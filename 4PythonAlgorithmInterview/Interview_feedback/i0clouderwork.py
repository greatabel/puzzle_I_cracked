'''



#----------------------------#

https://juejin.im/entry/57bd4e6fa633bd005d482ed1

 如何对100亿条记录（每条是数字）进行排序？
https://blog.csdn.net/ghoota/article/details/52766299

'''

import time
from termcolor import colored


def main_process():
    t = '''
    1. HTTP Methods 一共有九个，分别是 GET，HEAD，POST，PUT，DELETE，TRACE，OPTIONS，CONNECT，PATCH。
    其中 HEAD，TRACE，OPTIONS，CONNECT 在 RESTful API 设计中不常用
    在RESTful API 设计中，常用的有POST，GET，PUT，PATCH 和 DELETE
    

    POST    创建数据 Create 
    201 (Created) HTTP Header 'Location' 值设置为/books/id，其中id为新创建的book id 
    404 (Not Found), 如果资源已经存在，返回409 (Conflict)

    GET 读取数据 Read   200 (OK) 在Body中返回所有的books，可以使用参数来获取部分books数据如/books?page=3  
    200 (OK)在Body中返回对应id的book
    404 (Not Found) 如果没有对应数据，或者id格式不对

    PUT 修改数据 Update
    整条修改修改除ID外的所有属性
    404 (Not Found) 除非该API要实现批量或者全部更新可返回200，否则一般直接返回404即可   200 (OK) 204 (No Content) 
    404 (Not Found), 如果id格式不正确或者没有找到

    PATCH   修改数据 Update
    部分修改 修改一条记录的部分属性
    404 (Not Found) 除非该API要实现批量或者全部更新可返回200，否则一般直接返回404即可   200 (OK) 204 (No Content) 
    404 (Not Found), 如果id格式不正确或者没有找到

    DELETE  删除数据 Delete 404 (Not Found)一般直接返回404 除非你真的想删除全部集合可返回200 200 (OK)
    404 (Not Found) 如果id格式不正确或者没有找到



    2. python3.5新的关键字
    Python 3.5，我们现在可以通过新的 await 和 async (语法)功能很轻松的执行协程
    Python3.7中 async和await 成为了关键字，这也意味着async和await不能成为变量名字了


    3. 如何对100亿条记录（每条是数字）进行排序？
    1.把这个37GB的大文件，用哈希分成1000个小文件，每个小文件平均38MB左右（理想情况），把100亿个数字对1000取模，模出来的结果在0到999之间，每个结果对应一个文件，所以我这里取的哈希函数是 h = x % 1000，哈希函数取得”好”，能使冲突减小，结果分布均匀。

    2.拆分完了之后，得到一些几十MB的小文件，那么就可以放进内存里排序了，可以用快速排序，归并排序，堆排序等等。

    3.1000个小文件内部排好序之后，就要把这些内部有序的小文件，合并成一个大的文件，可以用二叉堆来做1000路合并的操作，每个小文件是一路，合并后的大文件仍然有序。

    首先遍历1000个文件，每个文件里面取第一个数字，组成 (数字, 文件号) 这样的组合加入到堆里（假设是从小到大排序，用小顶堆），遍历完后堆里有1000个 (数字，文件号) 这样的元素
    然后不断从堆顶拿元素出来，每拿出一个元素，把它的文件号读取出来，然后去对应的文件里，加一个元素进入堆，直到那个文件被读取完。拿出来的元素当然追加到最终结果的文件里。
    按照上面的操作，直到堆被取空了，此时最终结果文件里的全部数字就是有序的了

    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





