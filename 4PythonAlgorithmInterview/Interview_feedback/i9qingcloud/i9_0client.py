#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5
import socket
import json
# 侦听的IP和端口
ip_port = ('127.0.0.1', 6666)
# 创建socket对象
s = socket.socket()
s.connect(ip_port)
while True:
    # 发送消息
    send_data = input(">>>").strip()
    # 用户如果没有输入,进入到下一步发送给server端,server接收到空就会堵塞不运行
    if len(send_data) == 0:
        continue
    # 用户输入exit退出
    if send_data == 'exit':
        break
    # 发送用户输入的指令到server端
    s.send(bytes(send_data, encoding='utf-8'))
    # 接收消息
    # 接收到对方返回结果的准备消息和要返回内容的长度
    msg_szie = 0
    recv_msg = s.recv(1024)
    if recv_msg:
        msg_size = int(str(recv_msg, encoding='utf-8'))
    # 发送一个'start'给server端,让server端开始发送内容
    start_tag = 'Start'
    s.send(bytes(start_tag, encoding='utf-8'))
    # 通过第一次交互,得知要接受多少数据后,recv_size设置初始值
    recv_size = 0
    recv_msg = b''
    # 当前接收内容小于总接收内容,则一直持续到接收完
    while recv_size < msg_size:
        recv_data = s.recv(1024)
        # 每次接收内容做拼接
        recv_msg += recv_data
        recv_size += len(recv_data)
    print(str(recv_msg, encoding='utf-8'))
s.close()