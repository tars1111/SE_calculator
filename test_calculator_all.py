#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   test_calculator_all.py    
@Contact :   zhu1956318525@163.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/6 17:21   浛颖      1.0         使用了Python的unittest模块，分别对加法、减法、乘法、除法以及三角函数计算功能进行了测试
'''

import unittest
from SE_calculator import add, subtract, multiply, divide, sin_func, cos_func, tan_func

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

        result = add(-2, 2)
        self.assertEqual(result, 0)

        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

        result = subtract(2, -2)
        self.assertEqual(result, 4)

        result = subtract(0, 0)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = multiply(3, 5)
        self.assertEqual(result, 15)

        result = multiply(-2, 2)
        self.assertEqual(result, -4)

        result = multiply(0, 5)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

        result = divide(5, 0)
        self.assertEqual(result, "Error: 除数不能为0")

    def test_sin_func(self):
        result = sin_func(30)
        self.assertAlmostEqual(result, 0.5, places=2)

        result = sin_func(45)
        self.assertAlmostEqual(result, 0.7071, places=4)

        result = sin_func(90)
        self.assertAlmostEqual(result, 1.0, places=2)

    def test_cos_func(self):
        result = cos_func(60)
        self.assertAlmostEqual(result, 0.5, places=2)

        result = cos_func(90)
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_tan_func(self):
        result = tan_func(45)
        self.assertAlmostEqual(result, 1.0, places=2)

        result = tan_func(60)
        self.assertAlmostEqual(result, 1.7321, places=4)

if __name__ == '__main__':
    unittest.main()

