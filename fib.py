"""
509. 斐波那契数
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。
"""

class Solution(object):
    def fib_1(self, n):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib(self, n):
        if n < 2:
            return n 
        a, b, c = 0, 1, 0
        for i in range(1, n):
            c = a + b 
            a, b = b, c
        return c
