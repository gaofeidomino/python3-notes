#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式
# 列表生成式（List Comprehensions），是Python内置的非常简单却强大的 可以用来创建list的生成式。

# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用
list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
[x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环后面还可以加上if判断，这样可以筛选出仅偶数的平方
[x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列（三层和三层以上的循环就很少用到）
[m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# 列出当前目录下的所有文件和目录名
import os
[d for d in os.listdir('.')]
# ['.config', 'Music', '.DS_Store', 'Downloads.pem', '.CFUserTextEncoding', '.stCommitMsg', '.hgignore_global', '.zshrc', '.continue', 'Pictures', '.zprofile', '.nvm', '.zsh_history', 'Desktop', 'Library', '.lesshst', '.gitignore_global', 'Public', 'Virtual Machines.localized', 'package-lock.json', 'work', '.ssh', 'Movies', 'Applications', '.Trash', '.gitflow_export', '.zcompdump', '.pnpm-state', '.npm', 'Documents', 'chrome-profile', '.vscode', '.bash_profile', 'Downloads', '.python_history', '.gitconfig', '.zsh_sessions']


# 可以同时使用两个甚至多个变量，比如 dict 的 items() 可以同时迭代 key 和 value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

# x = A
# y = B
# z = C

# 列表生成式也可以使用两个变量来生成 list
[k + '=' + v for k, v in d.items()]
# ['x=A', 'y=B', 'z=C']

# 把一个 list 中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
# ['hello', 'world', 'ibm', 'apple']



# if ... else

# 以下代码正常输出偶数
[x for x in range(1, 11) if x % 2 == 0]
# [2, 4, 6, 8, 10]

# 不能在最后的if加上else
# 因为跟在for后面的if是一个筛选条件，不能带else

'''
[x * x for x in range(1, 11) if x % 2 == 0 else 0]

File "<stdin>", line 1
    [x * x for x in range(1, 11) if x % 2 == 0 else 0]
                                               ^^^^
SyntaxError: invalid syntax
'''

# 把 if 写在 for 前面必须加 else，否则报错
# 因为 for 前面的部分是一个表达式，它必须根据 x 计算出一个结果。
# 因此，考察表达式：x if x % 2 == 0，无法根据 x 计算出结果，因为缺少 else，必须加上 else

'''
[x if x % 2 == 0 for x in range(1, 11)]

File "<stdin>", line 1
    [x if x % 2 == 0 for x in range(1, 11)]
     ^^^^^^^^^^^^^^^
SyntaxError: expected 'else' after 'if' expression
'''

[x if x % 2 == 0 else -x for x in range(1, 11)]
# [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]


# 如果 list 中既包含字符串，又包含整数，由于非字符串类型没有 lower() 方法，列表生成式会报错
# 使用内建的 isinstance 函数可以判断一个变量是不是字符串
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
# ['hello', 'world', 'apple']