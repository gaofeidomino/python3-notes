#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数
'''
在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
在 Python中，对匿名函数提供了有限支持
还是以 map() 函数为例，计算 f(x)=x2 时，除了定义一个 f(x) 的函数外，还可以直接传入匿名函数：
'''
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 通过对比可以看出，匿名函数 lambda x: x * x 实际上就是：
def fn(x):
    return x * x
'''
关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数
    匿名函数有个限制，就是只能有一个表达式，不用写 return，返回值就是该表达式的结果
    用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
    
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
f = lambda x: x * x
f
# <function <lambda> at 0x102e0fc40>
f(5)
# 25
'''也可以把匿名函数作为返回值返回，比如：'''
def build(x, y):
    return lambda: x * x + y * y



def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))

# 上述代码可以简化为

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]