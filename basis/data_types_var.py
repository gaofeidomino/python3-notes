#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据类型和变量

## 数据类型

# 1、整数（int）：用于表示整数值，可以进行常见的算术操作，如加减乘除等。


# 2、浮点数（float）：用于表示带有小数点的数字，也可以进行算术操作，如整数一样。


# 3、字符串（str）：用于表示文本数据，可以进行字符串拼接、切片、查找等操作。
# 字符串内部既包含 ' 又包含 "，可以用转义字符 \ 来标识，比如：
'I\'m \"OK\"!'
# 表示的字符串内容是：I'm "OK"!

# \n 表示换行，\t 表示制表符，字符 \ 本身也要转义，所以 \\ 表示的字符就是 \
print('I\'m ok.')
# I'm ok.
print('I\'m learning\nPython.')
# I'm learning
# Python.
print('\\\n\\')
# \
# \

# 如果字符串里面有很多字符都需要转义，就需要加很多 \，为了简化，Python允许用 r'' 表示 '' 内部的字符串默认不转义
print('\\\t\\')
# \       \
print(r'\\\t\\')
# \\\t\\


# 4、布尔值（bool）：只有两个值，True 和 False，用于表示逻辑真值和逻辑假值。
True
# True
False
# False
3 > 2
# True
3 > 5
# False

# 布尔值可以用 and、or 和 not 运算
# and运算是与运算，只有所有都为True，and运算结果才是True
True and True
# True
True and False
# False
False and False
# False
5 > 3 and 3 > 1
# True

# or运算是或运算，只要其中有一个为True，or运算结果就是True
True or True
# True
True or False
# True
False or False
# False
5 > 3 or 1 > 3
# True

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True
not True
# False
not False
# True
not 1 > 2
# True


# 5、空值。用 None 表示。None 不能理解为 0，因为 0 是有意义的，而 None 是一个特殊的空值。


# 变量。
# 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
# 变量在程序中就是用一个变量名表示，变量名必须是大小写英文、数字和_的组合，且不能用数字开头。

# 等号 = 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 'ABC'

# 不要把赋值语句的等号等同于数学的等号。

# Python解释器干了两件事情：
# 在内存中创建了一个'ABC'的字符串；
# 在内存中创建了一个名为a的变量，并把它指向'ABC'。

a = 'ABC'
b = a
a = 'XYZ'
print(b)
# 最后一行打印出变量 b 的内容到底是 'ABC' 还是 'XYZ' ？
# 如果从数学意义上理解，就会错误地得出 b 和 a 相同，也应该是 'XYZ'，但实际上 b 的值是 'ABC'：
# 1.执行 a = 'ABC'，解释器创建了字符串 'ABC' 和变量 a，并把 a 指向 ABC'：
# 2.执行 b = a，解释器创建了变量 b，并把 b 指向 a 指向的字符串 'ABC'：
# 3.执行 a = 'XYZ'，解释器创建了字符串 'XYZ'，并把 a 的指向改为 'XYZ'，但 b 并没有更改：
# 4.最后打印变量 b 的结果是'ABC' 