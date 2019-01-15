# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:36:14 2019

@author: bianl
"""
#  从我们的 app 包中导入 app 变量
from app import app

#  route() 装饰器告诉Flask什么样的URL能触发我们的函数
#  两个 route 装饰器创建了从网址 / 以及 /index 到这个函数的映射
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"