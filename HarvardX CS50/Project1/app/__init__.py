# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:29:33 2019

@author: bianl
"""
#  初始化脚本
from flask import Flask
from app import views

#  导入 Flask 类, 并创建实例
app = Flask(__name__)
