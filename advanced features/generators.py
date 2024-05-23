#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器
'''
通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含 100万个元素的列表，不仅占用很大的存储空间，如果仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的 list，从而节省大量的空间。

在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个 generator，有很多种方法。
'''

# 第一种
# 只要把一个列表生成式的 [] 改成 ()，就创建了一个 generator
L = [x * x for x in range(10)]
L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
g
# <generator object <genexpr> at 0x104893ac0>

# 创建 L 和 g 的区别仅在于最外层的 [] 和 ()，L 是一个 list，而 g 是一个 generator

# 打印出 generator 的每一个元素，可以通过 next() 函数获得 generator 的下一个返回值
next(g)
# 0

next(g)
# 1

next(g)
# 4

next(g)
# 9

next(g)
# 16

next(g)
# 25

next(g)
# 36

next(g)
# 49

next(g)
# 64

next(g)
# 81

next(g)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

# generator 保存的是算法，每次调用 next(g)，就计算出 g 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的错误

# 因为 generator 也是可迭代对象，使用 for 循环就可以不断打印 generator 的每一个元素
g = (x * x for x in range(10))
for n in g:
    print(n)
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

# 如果推算的算法比较复杂，用类似列表生成式的 for 循环无法实现的时候，还可以用函数来实现
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 代码如下
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'Done'

# 赋值语句：a, b = b, a + b 相当于 
# t = (b, a + b)    # t是一个tuple
# a = t[0]
# b = t[1]

# fib()函数可以输出斐波那契数列的前 N 个数
fib(6)
# 1
# 1
# 2
# 3
# 5
# 8
# 'done'

# 仔细观察，可以看出，fib 函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑非常类似 generator。
# 也就是说，上面的函数和 generator 仅一步之遥。

# 要把 fib 函数变成 generator 函数，只需要把 print(b) 改为 yield b 就可以了：
def my_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 这是定义 generator 的另一种方法
# 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator 函数，调用一个 generator 函数将返回一个 generator：
def my_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
my_generator
# <function my_generator at 0x104b4f9c0>

f = my_generator(6)
f
# <generator object my_generator at 0x104996a40>

# generator 函数和普通函数的执行流程不一样
# 普通函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回
# generator 的函数，在每次调用 next() 的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行

# 例如： 定义一个generator函数，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 调用该 generator 函数时，首先要生成一个 generator 对象，然后用 next() 函数不断获得下一个返回值
o = odd()
next(o)
# step 1
# 1

next(o)
# step 2
# 3

next(o)
# step 3
# 5

next(o)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''
# 在执行过程中，遇到 yield 就中断，下次又继续执行。执行 3 次 yield 后，已经没有 yield 可以执行了，所以，第 4 次调用 next(o) 就报错


# ⚠️⚠️⚠️  务必注意：调用 generator 函数会创建一个 generator 对象，多次调用 generator 函数会创建多个相互独立的 generator
# 例如这样调用 next() 每次都返回1
next(odd())
# step 1
# 1
next(odd())
# step 1
# 1
next(odd())
# step 1
# 1
# 原因在于 odd() 会创建一个新的 generator 对象，上述代码实际上创建了 3 个完全独立的 generator，对 3 个 generator 分别调用 next() 当然每个都会返回第一个值
# 正确的写法是创建一个 generator 对象，然后不断对这一个 generator 对象调用 next()，如本页 150行-168行代码

# 在循环过程中不断调用 yield，就会不断中断。要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来


# 用 for 循环调用 generator 时，拿不到 generator 的 return 语句的返回值。
# 想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value: done


'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个 list，写一个 generator，不断输出下一行的 list
'''
def triangles():
    row = [1]
    while True:
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

n = 0
results = []

for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]




# 小结
# 在 Python 中，可以简单地把列表生成式改成 generator，也可以通过函数实现复杂逻辑的 generator

# generator 的工作原理，它是在 for 循环的过程中不断计算出下一个元素，并在适当的条件结束 for 循环。
# 对于函数改成的 generator 来说，遇到 return 语句或者执行到函数体最后一行语句，就是结束 generator 的指令，for 循环随之结束。


# 请注意区分普通函数和 generator 函数

# 普通函数调用直接返回结果：
r = abs(6)
r
# 6

# generator函数的调用实际返回一个 generator 对象：
g = my_generator(6)
g
# <generator object my_generator at 0x104996a40>