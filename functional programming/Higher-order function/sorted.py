#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted 排序算法

'''
无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，可以直接比较，但如果是字符串或者两个 dict，直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

sorted() 也是一个高阶函数。用 sorted() 排序的关键在于实现一个映射函数。
'''

# Python 内置的 sorted() 函数可以对 list 进行排序：
sorted([36, 5, -12, 9, -21])
# [-21, -12, 5, 9, 36]


# sorted() 函数也是一个高阶函数，它还可以接收一个 key 函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36, 5, -12, 9, -21], key=abs)
# [5, 9, -12, -21, 36]


# 字符串排序：
sorted(['bob', 'about', 'Zoo', 'Credit'])
# ['Credit', 'Zoo', 'about', 'bob']

# 默认情况下，对字符串排序，是按照 ASCII 的大小比较的，由于 'Z' < 'a'，结果，大写字母 Z 会排在小写字母 a 的前面
# 给 sorted 传入 key 函数，可实现忽略大小写的排序：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# ['about', 'bob', 'Credit', 'Zoo']


# 进行反向排序，可以传入第三个参数 reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']



# 用一组 tuple 表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 用 sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)
# [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

# 按成绩从高到低排序：
def by_score(t):
    return -t[1]

L3 = sorted(L, key=by_score)
print(L3)
# [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]