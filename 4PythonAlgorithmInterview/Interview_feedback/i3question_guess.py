'''
题目描述：

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

#----------------------------#



'''

import time
from termcolor import colored


def dfs(s, segment, res, ip):
    if segment == 4:
        if s == '':
            res.append(ip[1:])
        return 
    for i in range(1, 4):
        if i <= len(s):
            if int(s[:i]) <= 255:
                dfs(s[i:], segment+1,res,ip+'.'+s[:i])
                if s[0] == '0':
                    break

def main_process():
    s= "25525511135"
    res = []
    dfs(s, 0, res, '')
    print(res)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





