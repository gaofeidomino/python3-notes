#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代

# 给定一个 list 或 tuple，可以通过 for 循环来遍历这个 list 或 tuple，这种遍历称为迭代（Iteration）
# 在Python中，迭代通过for ... in来完成

# Python 的 for 循环抽象程度高，因为 Python 的 for 循环不仅可以用在 list 或 tuple 上，还可以作用在其他可迭代对象上
# 只要是可迭代对象，无论有无下标，都可以迭代，比如 dict

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# a
# c
# b

# 因为 dict 的存储不是按照 list 的方式顺序排列，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict 迭代的是 key。
# 如果要迭代 value，可以用for value in d.values()
# 如果要同时迭代key和value，可以用for k, v in d.items()

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)


# 字符串也是可迭代对象
for s in 'ABC':
    print(s)

# A
# B
# C


# 如何判断一个对象是可迭代对象呢？
# 方法是通过collections.abc模块的Iterable类型判断

from collections.abc import Iterable
isinstance('abc', Iterable)     # True
isinstance([1,2,3], Iterable)   # True
isinstance(123, Iterable)       # False


# 对 list 实现类似 Java 那样的下标循环
# Python 内置的 enumerate 函数可以把一个 list 变成「索引-元素对」，这样就可以在 for 循环中同时迭代索引和元素本身

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 0 A
# 1 B
# 2 C

# for循环里，同时引用两个变量

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 1 1
# 2 4
# 3 9

# 使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(L):
    if not L:
        return(None, None)
    
    min_val = max_val = L[0]

    for n in L:
        if min_val > n:
            min_val = n
        elif max_val < n:
            max_val = n
    
    return(min_val, max_val)