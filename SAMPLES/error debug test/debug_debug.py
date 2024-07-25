#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 综合示例：配置文件日志和控制台日志
import logging

# 创建 logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 创建格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将格式化器添加到处理器
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 生成日志
logger.debug('This debug message will go to the file')
logger.info('This info message will go to the file')
logger.warning('This warning message will go to both the file and the console')
logger.error('This error message will go to both the file and the console')
logger.critical('This critical message will go to both the file and the console')
