# coding:utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>                #
# author gavin li 94369299@qq.com                                       #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2003-2020, gavin li                                    #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:  2019-10-12                                                 #
#########################################################################
import enum
# 定义Season枚举类
Season = enum.Enum('Season',('Spring','Summer','Fall','Winner'))
# 直接访问指定枚举
print(Season.Spring)
# 访问枚举成员的变量名
print(Season.Spring.name)
# 访问枚举成员的值
print(Season.Spring.value)

# 根据枚举变量名访问枚举对象
print(Season['Summer'].name)
# 根据枚举值访问枚举对象
print(Season(3))
print(Season(3).name)

# 遍历Season枚举的所有成员
for name,member in Season.__members__.items():
    print(name,'=>',member,member.value)



