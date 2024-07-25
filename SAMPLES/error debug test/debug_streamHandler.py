#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输出日志到控制台 StreamHandler
import logging

# 创建 logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建格式化器并添加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(console_handler)

# 生成日志
logger.debug('This is a debug message')
logger.info('This is an info message')
