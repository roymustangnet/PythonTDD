# -*- coding:utf-8 -*-
# @Time    : 2020/7/1 10:36
# @Author  : supakito

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in  browser.title