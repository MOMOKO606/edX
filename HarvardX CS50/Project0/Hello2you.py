# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:15:09 2019

@author: bianl
"""
#  导入 Flask 类
from flask import Flask
#  创建实例
app = Flask(__name__)

#  route() 装饰器告诉Flask什么样的URL能触发我们的函数
#  route 装饰器创建了从网址/到这个函数的映射
@app.route("/")
def index():
    return "Hello,world!"
#  route 装饰器创建了从网址/<string:name>到这个函数的映射
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello,{name}!"

if __name__ == '__main__':
      app.run( debug = True )

    