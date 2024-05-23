#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断和模式匹配


# 条件判断
age = 20

if age >= 18:
    print('your age is', age)
    print('adult')


if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if 语句执行是从上往下判断，如果在某个判断上是 True，把该判断对应的语句执行后，就忽略掉剩下的 elif 和 else

# 只要 x 是非零数值、非空字符串、非空 list 等，就判断为 True，否则为 False
x = 1
if x:
    print('True')


birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')

# 输入1982，结果报错
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() > int()
'''
# 因为 input() 返回的数据类型是 str，str 不能直接和整数比较，必须先把 str 转换成整数。Python 提供了 int() 函数
s = input('birth: ')
birth = int(s)

if birth < 2000:
    print('00前')
else:
    print('00后')



# 模式匹配
# 针对某个变量匹配若干种情况，可以使用 match 语句

# 如，某个学生的成绩只能是 A、B、C，用 if 语句编写如下
score = 'B'

if score == 'A':
    print('score is A.')
elif score == 'B':
    print('score is B.')
elif score == 'C':
    print('score is C.')
else:
    print('invalid score.')

# 用match语句改写，如下
score = 'B'

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

# match 语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
# 11~18 years old.

# 第一个 case x if x < 10 表示当 age < 10 成立时匹配，且赋值给变量 x，
# 第二个 case 10 仅匹配单个值，
# 第三个 case 11|12|...|18 能匹配多个值，用|分隔


# match 语句还可以匹配列表
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

# 第一个 case ['gcc'] 表示列表仅有 'gcc' 一个字符串，没有指定文件名，报错；
# 第二个 case ['gcc', file1, *files] 表示列表第一个字符串是 'gcc'，第二个字符串绑定到变量 file1，后面的任意个字符串绑定到 *files（可变参数），它实际上表示至少指定一个文件；
# 第三个 case ['clean'] 表示列表仅有 'clean' 一个字符串；
# 最后一个 case _表示其他所有情况。