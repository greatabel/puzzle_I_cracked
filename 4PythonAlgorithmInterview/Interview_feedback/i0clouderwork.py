'''



#----------------------------#

https://juejin.im/entry/57bd4e6fa633bd005d482ed1


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

    2. 

    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





