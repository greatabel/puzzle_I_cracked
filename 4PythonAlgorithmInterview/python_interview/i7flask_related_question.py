'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    1. 什么是flask?
    ans: Flask是Python编写的一款轻量级Web应用框架。其 WSGI 工具箱采用 Werkzeug ，
    模板引擎则使用 Jinja2。
    Flask使用 BSD 授权。其中两个环境依赖是Werkzeug和jinja2，这意味着它不需要依赖外部库。
    正因如此，我们将其称为轻量级框架
    --------------------
    2. flask是一个MVC模型？
    flask是个经典的MVC框架

    3. flask中连接数据库？
    在脚本中以用第三方库正常连接，用sql语句正常操作数据库，如mysql关系型数据库的pymsql库
    用ORM来进行数据库连接，flask中典型的flask_sqlalchemy，已面向对象的方式进行数据库的连接与操

    4.列举Http请求中的状态码?
    200 访问正常
    201 创建了资源
    300 多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择
    301 永久性重定向
    302 临时性重定向
--  4XX 服务器无法处理请求
    400 请求报文中存在错误，服务器无法理解
    404 服务器无法根据客户端的请求找到资源
--  5XX 服务器内部错误
    500 internal Server Error 服务器内部错误
    503 服务器暂时处于超负载或正在进行停机维护，现在无法处理请求

    5. HTTP协议里的请求头有什么用?

    Accept-Encoding:用于告诉服务器，客户机支持的数据压缩格式
    User-Agent：用于告诉服务器，客户机的软件环境
    Cookie：客户机通过这个头可以想服务器带数据
    ETag：缓存相关的头，和Last-Modified功能一样，不过实时性更强

    request 里的 Accept-* 可有钦定的意思？
    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding:gzip, deflate, sdch
    Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4

    response 里的 Content-* 才是已经决定了就是你了这个意思好吗
    Content-Encoding:gzip
    Content-Length:5506
    Content-Type:text/html;charset=utf-8

    6. 什么是wsgi?
    全称 Web Server Gateway Interface，或者 Python Web Server Gateway Interface ，
    是为 Python 语言定义的 Web 服务器和 Web 应用程序或框架之间的一种简单而通用的接口。
    自从 WSGI 被开发出来以后，许多其它语言中也出现了类似接口

    从名字就可以看出来，这东西是一个Gateway，也就是网关。网关的作用就是在协议之间进行转换
    WSGI 是作为 Web 服务器与 Web 应用程序或应用框架之间的一种低级别的接口，
    以提升可移植 Web 应用开发的共同点。WSGI 是基于现存的 CGI(公共网关接口)标准而设计的。

    WSGI就是一座桥梁，桥梁的一端称为服务端或网关端，另一端称为应用端或者框架端，WSGI的作用就是在协议之间进行转化。
    WSGI将Web组件分成了三类：Web 服务器（WSGI Server）、
    Web中间件（WSGI Middleware）与Web应用程序（WSGI Application）。
    Web Server接收HTTP请求，封装一系列环境变量，按照WSGI接口标准调用注册的WSGI Application，
    最后将响应返回给客户端。

    7.Flask框架依赖组件?
    Route(路由)
    templates(模板)
    Models(orm模型)
    blueprint(蓝图)
    Jinja2模板引擎

    8. blueprint的作用？
    蓝图Blueprint实现模块化的应用
    - book_bp = Blueprint('book', __name__）创建蓝图对象
    - 蓝图中使用路由@book_bp.route('url')
    - 在另一.py文件里导入和注册蓝图from book import book_bp app.register_blueprint(book_bp)

    作用
    将不同的功能模块化
    构建大型应用
    优化项目结构
    增强可读性,易于维护（跟Django的view功能相似）

    9. 简述Flask上下文管理流程?
    每次有请求过来的时候，flask 会先创建当前线程或者进程需要处理的两个重要上下文对象，
    把它们保存到隔离的栈里面，这样视图函数进行处理的时候就能直接从栈上获取这些信息。

    10.Flask中多app应用是怎么完成?
    请求进来时，可以根据URL的不同，交给不同的APP处理

    11Flask框架默认session处理机制?
    Flask的默认session利用了Werkzeug的SecureCookie，把信息做序列化(pickle)后编码(base64)，放到cookie里了。

    过期时间是通过cookie的过期时间实现的。

    为了防止cookie内容被篡改，session会自动打上一个叫session的hash串，这个串是经过session内容、SECRET_KEY计算出来的，
    看得出，这种设计虽然不能保证session里的内容不泄露，但至少防止了不被篡改
————————————————



    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





