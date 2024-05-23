#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 安装第三方模块

'''
Python 中，安装第三方模块，是通过包管理工具 pip 完成的。
    如果使用 Mac 或 Linux，安装 pip 这个步骤就可以跳过。
    如果使用 Windows，确保安装 Python 时勾选了 pip 和 Add python.exe to Path。
    在命令提示符窗口下尝试运行 pip，如果 Windows 提示未找到命令，可以重新运行安装程序添加 pip。
    注意：Mac 或 Linux 上有可能并存 Python 3.x 和 Python 2.x，因此对应的 pip 命令是 pip3。

一般来说，第三方库都会在 Python 官方的 (https://pypi.org/) 网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者 pypi 上搜索，
比如 Pillow 的名称叫 Pillow，因此，安装 Pillow 的命令就是：
    pip install Pillow
等待下载并安装后，就可以使用 Pillow 了。
'''

'''
安装常用模块
    使用 Python 时，我常需要用到很多第三方库，例如，上面提到的 Pillow，以及 MySQL 驱动程序，Web 框架 Flask，科学计算 Numpy 等。
    用 pip 一个一个安装费时费力，还需要考虑兼容性。推荐直接使用 Anaconda，这是一个基于 Python 的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，
    装上 Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

    可以从 Anaconda 官网下载 GUI 安装包，安装包有 500~600M，所以需要耐心等待下载。
    下载后直接安装，Anaconda 会把系统 Path 中的 python 指向自己自带的 Python，并且，Anaconda 安装的第三方模块会安装在 Anaconda 自己的路径下，不影响系统已安装的 Python 目录。

    安装好 Anaconda 后，重新打开命令行窗口，在命令行中输入 conda --version 命令，如果能够成功输出Anaconda 的版本号，则说明Anaconda 安装成功。
'''


'''
Anaconda 是一个开源的 Python 发行版本，用于科学计算、数据分析和机器学习等领域。它包含了许多常用的 Python 库和工具，
如 NumPy、SciPy、Pandas、Matplotlib、Scikit-learn 等，以及 IPython、Jupyter Notebook 等开发和交互环境。
Anaconda 也提供了一个方便的包管理工具 conda，可以帮助用户安装、管理和更新 Python 包及其依赖项。

Anaconda 旨在简化 Python 环境的配置和管理，使用户能够快速地搭建一个适用于科学计算和数据分析的工作环境。
它不仅支持 Windows、macOS 和 Linux 等多种操作系统，还提供了针对企业和个人用户的不同版本和服务，
如 Anaconda Individual Edition、Anaconda Team Edition 和 Anaconda Enterprise。
Anaconda 的目标是让用户能够更轻松地利用 Python 进行科学计算和数据分析，提高工作效率和生产力。


在 Python 中，常用的机器学习框架包括 TensorFlow、PyTorch、Scikit-learn、Keras 等：

    TensorFlow：
        TensorFlow 是由 Google 开发的一个开源机器学习框架，广泛应用于各种机器学习任务。
        它支持分布式计算、GPU 加速和自动微分等功能，适用于大规模数据集和复杂模型。
        TensorFlow 具有强大的生态系统，拥有众多高级库和工具，如 TensorFlow Estimator、TensorFlow Probability 等。
        然而，TensorFlow 的 API 相对复杂，对于初学者来说可能有一定的学习曲线。

    PyTorch：
        PyTorch 是一个由 Facebook 开发的动态图机器学习框架，以其简洁的 API 和灵活的调试体验而受到欢迎。
        PyTorch 支持 GPU 加速和自动微分，且代码易于理解和修改。它适用于研究原型设计和实验探索。
        PyTorch 的社区也非常活跃，提供了丰富的教程和示例。然而，与 TensorFlow 相比，PyTorch 的生态系统可能稍显逊色。

    Scikit-learn：
        Scikit-learn 是一个简单高效的机器学习库，提供了大量现成的机器学习算法和工具，适用于快速原型设计和数据处理。
        Scikit-learn 的 API 设计简洁易用，对于初学者来说非常友好。然而，它主要关注传统的机器学习算法，对于深度学习等复杂模型的支持相对较少。

    Keras：
        Keras 是一个高层神经网络 API，可以运行在 TensorFlow、Theano 或 CNTK 等后端之上。
        Keras 以其简洁易用的 API 和快速的原型设计能力而受到青睐。它适合初学者快速上手深度学习项目。
        然而，由于 Keras 是高层 API，对于底层细节的控制可能不如 TensorFlow 或 PyTorch 灵活。

'''


'''
模块搜索路径
    当试图加载一个模块时，Python 会在指定的路径下搜索对应的 .py 文件，如果找不到，就会报错：

        import mymodule
        # Traceback (most recent call last):
        #   File "<stdin>", line 1, in <module>
        # ModuleNotFoundError: No module named 'mymodule'

    默认情况下，Python 解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在 sys 模块的 path 变量中：
'''
import sys
sys.path
# ['', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages']

'''
    如果要添加自己的搜索目录，有两种方法：
        一是直接修改 sys.path，添加要搜索的目录
            sys.path.append('/Users/gaofei/my_py_scripts')
        这种方法是在运行时修改，运行结束后失效。

        第二种方法是设置环境变量 PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置 Path 环境变量类似。注意只需要添加自己的搜索路径，Python 自己本身的搜索路径不受影响。
'''