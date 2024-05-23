#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Fei Gao'

import sys

def test():
    args = sys.argv

    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()



'''
Python 本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。

以内建的sys模块为例，编写一个 hello_module 的模块，如上：
    第 1、第 2 行是标准注释，第 1 行注释可以让这个 hello_module.py 文件直接在 Unix/Linux/Mac 上运行，第 2 行注释表示 .py 文件本身使用标准 UTF-8 编码；
    第 4 行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
    第 6 行使用 __author__ 变量把作者写进去，这样公开源代码后别人就可以看到作者的大名；
    后面开始就是真正的代码部分；

以上就是 Python 模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。


使用sys模块的第一步，就是导入该模块：
    （见第 8 行）

    导入 sys 模块后，就有了变量 sys 指向该模块，利用 sys 这个变量，就可以访问 sys 模块的所有功能。
    sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数。argv 至少有一个元素，因为第一个参数永远是该 .py 文件的名称，例如：
        运行 python3 hello_module.py 获得的 sys.argv 就是 ['hello_module.py']；
        运行 python3 hello_module.py GaoFei 获得的 sys.argv 就是 ['hello_module.py', 'GaoFei']。

最后，注意到这两行代码：

    if __name__=='__main__':
        test()

在命令行运行 hello_module 模块文件时，Python 解释器把一个特殊变量 __name__ 置为 __main__，
而如果在其他地方导入该 hello_module 模块时，if 判断将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    可以用命令行运行 hello_module.py 看看效果：

        python3 hello_module.py
        # Hello, world!
        python hello_module.py GaoFei
        # Hello, GaoFei!
    
    如果启动 Python 交互环境，再导入 hello_module 模块：

        python3
        import hello_module

    导入时，没有打印 Hello, word!，因为没有执行 test() 函数。
    调用 hello_module.test() 时，才能打印出 Hello, word!：

        hello_module.test()
        Hello, world!

'''

'''
作用域
    在一个模块中，可能会定义很多函数和变量，但有的函数和变量希望给别人使用，有的函数和变量希望仅仅在模块内部使用。在 Python 中，是通过 _ 前缀来实现的。
    正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
    类似 __xxx__ 这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的 __author__ ，__name__ 就是特殊变量，hello 模块定义的文档注释也可以用特殊变量 __doc__ 访问，自己的变量一般不要用这种变量名；
    类似 _xxx 和 __xxx 这样的函数或变量就是非公开的（private），不应该被直接引用，比如 _abc ， __abc 等；

    之所以说，private 函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为 Python 并没有一种方法可以完全限制访问 private 函数或变量，但是，从编程习惯上不应该引用 private 函数或变量。

    private 函数或变量不应该被别人引用，那它们有什么用？例子：
'''
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
    
'''
在模块里公开 greeting() 函数，而把内部逻辑用 private 函数隐藏起来了，这样，调用 greeting() 函数不用关心内部的 private 函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
    外部不需要引用的函数全部定义成 private，只有外部需要引用的函数才定义为 public。
'''