import time
from termcolor import colored


def main_process():
    t = '''

    https://zhuanlan.zhihu.com/p/35794035
    --------------------
    1. 什么是爬虫？
    请求网站并且提取数据的自动化程序

    2 爬虫基本流程？
    发起请求（scrapy 发送get, post 请求）可能保护请求头等信息，等待服务器响应
    获取服务器响应内容，可能是网页文本（html，json）,图片二进制，视频二进制等
    解析内容（正则 xpath json解析等）
    保存数据（本地文件，数据库等）

    3 反爬措施，如果解决？
        1. 基于用户行为，同一个ip段时间内多次访问同一个页面
        可以使用代理ip，构建ip池
        2. 请求头user-agent
        构建user-agent池（操作系统、浏览器不同，模拟不同用户）
        3. 动态加载（抓到的数据和浏览器显示的不一样），js渲染
        模拟ajax请求，返回json形式的数据
        selenium / webdriver 模拟浏览器加载 （chromedriver安装）

    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)