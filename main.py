#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:main.py
@time:2022/09/17
"""
from Qndxx import Qndxx

if __name__ == '__main__':
    laravel_session = "qGX9yOVupa1OaTpiNmq1US6JgtYMZIvc9H2SzO0a"
    qndxx = Qndxx(laravel_session)
    qndxx.login()
    qndxx.confirm()
