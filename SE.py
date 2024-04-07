#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   SE.py    
@Contact :   zhu1956318525@163.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/6 17:23   浛颖      1.0         这段代码实现了自定义的正弦、余弦和正切函数的计算，采用泰勒级数展开的方式进行近似计算。你可以根据需要调整精度和展开项数。

'''

import math

def my_sin(angle):
    angle = math.radians(angle)
    result = 0
    for n in range(10):
        result += ((-1) ** n) * (angle ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return result

def my_cos(angle):
    angle = math.radians(angle)
    result = 0
    for n in range(10):
        result += ((-1) ** n) * (angle ** (2 * n)) / math.factorial(2 * n)
    return result

def my_tan(angle):
    return my_sin(angle) / my_cos(angle)

# 测试自定义三角函数计算
angle = 30
print(f"sin({angle}) = {my_sin(angle)}")
print(f"cos({angle}) = {my_cos(angle)}")
print(f"tan({angle}) = {my_tan(angle)}")
