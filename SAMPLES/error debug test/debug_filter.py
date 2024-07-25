#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 日志过滤器 Filter
import logging

# 创建 logger
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建一个简单的过滤器，只允许 INFO 级别以上的日志通过
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.INFO

# 添加过滤器到处理器
console_handler.addFilter(InfoFilter())

# 创建格式化器并添加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 将处理器添加到 logger
logger.addHandler(console_handler)

# 生成日志
logger.debug('This debug message will not be shown')
logger.info('This is an info message')
logger.warning('This is a warning message')
