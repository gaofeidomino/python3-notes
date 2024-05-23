#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归函数

# 计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示
# fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
# fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

fact(5)
fact(100)

# 120
# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

# ⚠️⚠️⚠️ 使用递归函数需要注意防止栈溢出：
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出

# 例如
fact(1000)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in facn
#   File "<stdin>", line 4, in facn
#   File "<stdin>", line 4, in facn
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# 解决递归调用栈溢出的方法是通过「尾递归」优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 「尾递归」是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 优化后
def fact_opt(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
    # 仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用


# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


# 用递归函数非常简单地实现「汉诺塔」
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')

# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C