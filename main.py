#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:main.py
@time:2022/09/17
"""
from Qndxx import Qndxx
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--aa', type=str, default = None)
    args = parser.parse_args()
    laravel_session = args.aa
    qndxx = Qndxx(laravel_session)
    qndxx.login()
    qndxx.confirm()
