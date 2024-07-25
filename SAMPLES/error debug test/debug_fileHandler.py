#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输出日志到文件 FileHandler
import logging

# 创建 logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)

# 创建格式化器并添加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(file_handler)

# 生成日志
logger.error('This is an error message')
logger.critical('This is a critical message')
