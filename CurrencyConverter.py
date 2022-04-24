#!/usr/bin/env python3.7
# !-*- coding: utf-8 -*-
#
# Copyright (c) 2018 jd.com, Inc. All Rights Reserved
#
"""
File:   Moneychange.py
Author: wangshuai191
Date:   2019/2/11 20:15
Brief:  
"""
TempStr = input()
if TempStr[0:3] in ['RMB']:
    USD = eval(TempStr[3:])/6.78
    print("USD{:.2f}".format(USD))
elif TempStr[0:3] in ['USD']:
    RMB = eval(TempStr[3:])*6.78
    print("RMB{:.2f}".format(RMB))
