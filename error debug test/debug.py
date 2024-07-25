#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 调试
'''
第一种方法，用 print() 把可能有问题的变量打印出来看看：
    坏处是将来得删掉，到处都是 print()，运行结果也会包含很多垃圾信息
'''
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()
#  n = 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in main
#   File "<stdin>", line 4, in foo
# ZeroDivisionError: division by zero


'''
第二种方法，断言（assert）
    如果断言失败，assert 语句本身就会抛出 AssertionError
    assert 和 print() 相比好不到哪儿去。不过，启动 Python 解释器时可以用 -O 参数来关闭 assert：python -O err.py
        断言的开关“-O”是英文大写字母O，不是数字0；关闭后，可以把所有的 assert 语句当成 pass 来看
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()

# assert 的意思是，表达式 n != 0 应该是 True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in main
#   File "<stdin>", line 3, in foo
# AssertionError: n is zero!


'''
第三种方法，使用日志模块 logging
    logging 不会抛出错误，而且可以输出到文件
'''
import logging
'''
    使用 basicConfig 方法配置日志的基本设置，如日志级别、格式和输出位置。
        level: 设置日志级别。常用的级别有 DEBUG, INFO, WARNING, ERROR, CRITICAL。
        format: 设置日志格式。常用的格式包含时间、日志级别和消息内容。
'''
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
'''
    使用不同的日志级别方法生成日志消息
'''
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''
    配置和使用日志
'''
# 配置日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app.log',  # 日志输出到文件
                    filemode='w')  # 'w' 模式会覆盖之前的日志文件

'''
创建 logger
getLogger 获取（或创建）名为 example_logger 的日志记录器（logger）
logging.getLogger(name) 方法会根据指定的名称获取一个 Logger 对象。
如果名称为空字符串 ''，则返回根记录器（root logger）。如果指定的名称的记录器不存在，它会创建一个新的记录器对象。

记录器使用类似层次结构的名称空间。例如，
    logging.getLogger('example') 和 logging.getLogger('example.child') 会创建两个层次结构中的记录器，
    example.child 是 example 的子记录器。

子记录器会继承父记录器的配置和级别设置，这样可以实现灵活的日志记录和管理。
'''
logger = logging.getLogger('example_logger')

# 生成不同级别的日志消息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

'''
    日志处理器（Handler）
        使用不同的处理器将日志输出到不同的位置，如控制台、文件、远程服务器等

        StreamHandler: 输出日志到控制台，代码见(SAMPLES/error debug test/debug_streamHandler.py)

        FileHandler: 输出日志到文件，代码见(SAMPLES/error debug test/debug_fileHandler.py)

    日志过滤器（Filter）
        可以使用过滤器根据条件过滤日志消息，代码见(SAMPLES/error debug test/debug_filter.py)

    综合示例：配置文件日志和控制台日志，代码见(SAMPLES/error debug test/debug_debug.py)
'''


'''
第四种方法，启动 Python 的调试器 pdb，让程序以单步方式运行，可以随时查看运行状态
    (SAMPLES/error debug test/debug_pdb.py)
'''
'''
    # 启动
    python -m pdb debug_pdb.py
        > /python3-notes/SAMPLES/error debug test/debug_pdb.py(1)<module>()
        -> s = '0'

    # 命令 l 查看代码
    (Pdb) l
        1  -> s = '0'
        2     n = int(s)
        3     print(10 / n)
        [EOF]

    # 命令 n 单步执行代码
    (Pdb) n
        > /python3-notes/SAMPLES/error debug test/debug_pdb.py(2)<module>()
        -> n = int(s)

    (Pdb) n
        > /python3-notes/SAMPLES/error debug test/debug_pdb.py(3)<module>()
        -> print(10 / n)

    (Pdb) n
        ZeroDivisionError: division by zero
        > /python3-notes/SAMPLES/error debug test/debug_pdb.py(3)<module>()
        -> print(10 / n)

    (Pdb) n
        --Return--
        > /python3-notes/SAMPLES/error debug test/debug_pdb.py(3)<module>()->None
        -> print(10 / n)

    (Pdb) n
        ZeroDivisionError: division by zero
        > <string>(1)<module>()->None

    (Pdb) n
        --Return--
        > <string>(1)<module>()->None

    # 命令 「p 变量名」 来查看变量
    (Pdb) p s
        '0'

    (Pdb) p n
        0

    # 命令 q 结束调试，退出程序
    (Pdb) q
'''

'''
    pdb.set_trace()
        需要 import pdb，然后，在可能出错的地方放一个 pdb.set_trace()，就可以设置一个断点    
        程序会自动在 pdb.set_trace() 暂停并进入 pdb 调试环境，可以用命令 p 查看变量，或者用命令 c 继续运行

        
    python debug_pdb.py 
        > /python3-notes/SAMPLES/error debug test/debug_pdb.py(13)<module>()
        -> print(10 / n)

    (Pdb) p s
        '0'

    (Pdb) p n
        0

    (Pdb) c
        Traceback (most recent call last):
        File "/python3-notes/SAMPLES/error debug test/debug_pdb.py", line 13, in <module>
            print(10 / n)
                ~~~^~~
        ZeroDivisionError: division by zero
'''


'''推荐使用支持调试功能的 IDE 和 logging'''