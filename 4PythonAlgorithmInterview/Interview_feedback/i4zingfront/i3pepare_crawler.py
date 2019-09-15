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

    4 如何提高爬取效率？
        爬虫下载慢主要原因是阻塞等待发往网站的请求和网站返回

        采用异步与多线程，扩大电脑的cpu利用率；
        采用消息队列模式
        提高带宽

    5 request请求（封装http请求）方式中的post、get有什么区别？

    GET一般用于获取/查询资源信息，而POST一般用于更新资源信息
    get是在url中传递数据，数据放在请求头中，post是在请求体中传递数据
    get安全性非常低，post安全性较高，但是get执行效率却比Post方法好

    6 xpath、css选择器及返回类型区分？
    response.selector.xpath(css) 为了方便，其中的selector可以省略
    返回：由selector组成的list，每个元素都是一个selector对象

        1、SelectorList类型
        case = response.xpath('//*[@class="content"]/ul/li')

        2、List类型
        case = response.xpath('//*[@class="content"]/ul/li').extract()

        3、str类型
        case = ''.join(response.xpath('//*[@class="content"]/ul/li').extract())
        extract()[0]选取第一个元素， extract_first()能达到一样的效果

    7 模拟登陆原理？
    因为http请求是无状态的，网站为了识别用户身份，需要通过cookie记录用户信息（用户、密码），
    这些信息都会在手动登陆时记录在post请求的form-data里，
    那么在爬虫时候只需要将这些信息添加到请求头里即可

    8.用的什么框架，为什么选择这个框架？

    scrapy，只需要实现少量代码，就能够快速的抓取到数据内容。
    Scrapy 使用了 Twisted异步网络框架来处理网络通讯，可以加快下载速度，
    不用自己去实现异步框架，并且包含各种中间件接口，可以灵活的完成各种需求

    
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)