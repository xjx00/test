#!/usr/bin/python3
#-*-coding:utf-8-*-
#author: 17光电02 徐建祥
import sys

year = input("请输入年份:")
try:
    year = int(year)
except:
    print("Input is not a number")
    sys.exit()

if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("是闰年")
else:
    print("不是闰年")

