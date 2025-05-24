"""
@Author: Murong Li
@Time: 2025-05-23 17:04
@File: module_example.py
@Description: Description
"""


class My_Calculator_test:
    @staticmethod
    def add(x, y):  # 定义一个静态方法，计算两个数的和
        return x + y

    @staticmethod
    def subtract(x, y):  # 定义一个静态方法，计算两个数的差
        return x - y

    @staticmethod
    def multiply(x, y):  # 定义一个静态方法，计算两个数的积
        return x * y

    @staticmethod
    def divide(x, y):  # 定义一个静态方法，计算两个数的商
        if y == 0:  # 如果除数为0，则抛出异常
            raise ValueError("除数不能为0")
        return x / y

    @staticmethod
    def power(x, y):  # 定义一个静态方法，计算x的y次方
        return x**y
