'''



#----------------------------#



'''
import json
import ujson
import time
from termcolor import colored

def monkey_patch_json():  
    json.__name__ = 'ujson'  
    json.dumps = ujson.dumps  
    json.loads = ujson.loads  



def main_process():
    t = '这里有一个比较实用的例子，很多代码用到 import json，后来发现ujson性能更高，\
    如果觉得把每个文件的import json 改成 import ujson as json成本较高，\
    或者说想测试一下用ujson替换json是否符合预期，只需要在入口加上：'
    print(colored('mycount=', 'red'), t)
    monkey_patch_json()

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





