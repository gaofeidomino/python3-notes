#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误处理
'''
Python 内置了一套 try...except...finally... 的错误处理机制。示例：
'''
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
     print('except:', e)
finally:
      print('finally...')
print('END')
# try...
# except: division by zero
# finally...
# END

'''
当某些代码可能会出错时，就可以用 try 来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即 except 语句块，
执行完 except 后，如果有 finally 语句块，则执行 finally 语句块，至此，执行完毕。

没有错误发生，except 语句块不会被执行，但是 finally 如果有，则一定会被执行（可以没有 finally 语句）。
错误有很多种类，如果发生了不同类型的错误，应该由不同的 except 语句块处理。
'''
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

'''
此外，如果没有错误发生，可以在 except 语句块后面加一个 else，当没有错误发生时，会自动执行 else 语句：
'''
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

'''
Python 的错误其实也是 class，所有的错误类型都继承自 BaseException，所以在使用 except 时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
第二个 except 永远也捕获不到 UnicodeError，因为 UnicodeError 是 ValueError 的子类，如果有，也被第一个 except 给捕获了。

常见的错误类型和继承关系看这里：（https://docs.python.org/3/library/exceptions.html#exception-hierarchy）、（EXPAND/Exception Hierarchy.md）
'''
try:
    r = 10 / int('2')
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

'''
使用 try...except 捕获错误还有一个巨大的好处，就是可以跨越多层调用，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
比如函数 main() 调用 bar()，bar() 调用 foo()，结果 foo() 出错了，这时，只要 main() 捕获到了，就可以处理：
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


'''调用栈'''
'''
    如果错误没有被捕获，它就会一直往上抛，最后被 Python 解释器捕获，打印一个错误信息，然后程序退出。
    出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
'''
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
# Traceback (most recent call last):
#   File "/python3-notes/SAMPLES/error debug test/err.py", line 10, in <module>
#     main()
#   File "/python3-notes/SAMPLES/error debug test/err.py", line 8, in main
#     bar('0')
#   File "/python3-notes/SAMPLES/error debug test/err.py", line 5, in bar
#     return foo(s) * 2
#            ^^^^^^
#   File "/python3-notes/SAMPLES/error debug test/err.py", line 2, in foo
#     return 10 / int(s)
#            ~~~^~~~~~~~
# ZeroDivisionError: division by zero


'''记录错误'''
'''
    如果不捕获错误，自然可以让 Python 解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

    Python 内置的 logging 模块可以非常容易地记录错误信息：
        通过配置，logging 还可以把错误记录到日志文件里，方便事后排查。
'''
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "/python3-notes/SAMPLES/error debug test/err_logging.py", line 11, in main
#     bar('0')
#   File "/python3-notes/SAMPLES/error debug test/err_logging.py", line 7, in bar
#     return foo(s) * 2
#            ^^^^^^
#   File "/python3-notes/SAMPLES/error debug test/err_logging.py", line 4, in foo
#     return 10 / int(s)
#            ~~~^~~~~~~~
# ZeroDivisionError: division by zero
# END


'''抛出错误'''
'''
    因为错误是 class，捕获一个错误就是捕获到该 class 的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
    Python 的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

    如果要抛出错误，首先根据需要，可以定义一个错误的 class，选择好继承关系，然后，用 raise 语句抛出一个错误的实例：
        只有在必要的时候才定义自己的错误类型。如果可以选择 Python 已有的内置的错误类型（比如 ValueError，TypeError），尽量使用 Python 内置的错误类型。
'''
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
# Traceback (most recent call last):
#   File "/python3-notes/SAMPLES/error debug test/err_raise.py", line 10, in <module>
#     foo('0')
#   File "/python3-notes/SAMPLES/error debug test/err_raise.py", line 7, in foo
#     raise FooError('invalid value: %s' % s)
# FooError: invalid value: 0

'''
    另一种错误处理方式：
'''
# err_reraise.py
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
# ValueError!
# Traceback (most recent call last):
#   File "/python3-notes/SAMPLES/error debug test/err_reraise.py", line 14, in <module>
#     bar()
#   File "/python3-notes/SAMPLES/error debug test/err_reraise.py", line 9, in bar
#     foo('0')
#   File "/python3-notes/SAMPLES/error debug test/err_reraise.py", line 4, in foo
#     raise ValueError('invalid value: %s' % s)
# ValueError: invalid value: 0

'''
    在 bar() 函数中，明明已经捕获了错误，但是，打印一个 ValueError! 后，又把错误通过 raise 语句抛出去了，为什么？

    其实这种错误处理方式相当常见。捕获错误目的只是记录一下，便于后续追踪。
    但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。

    raise 语句如果不带参数，就会把当前错误原样抛出。此外，在 except 中 raise 一个 Error，还可以把一种类型的错误转化成另一种类型：
        只要是合理的转换逻辑就可以，但是，决不应该把一个 IOError 转换成毫不相干的 ValueError。
'''
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')