# -*- coding: utf-8 -*-
import logbook, os
from logbook import FileHandler, Logger

logger = None

logbook.set_datetime_format("local")


def log_type(record, handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date = record.time,                              # 日志时间
        level = record.level_name,                       # 日志等级
        filename = record.filename.split('rqpro_api_server/')[-1],   # 文件名
        func_name = record.func_name,                    # 函数名
        lineno = record.lineno,                          # 行号
        msg = record.message                             # 日志内容
    )
    return log


def init(log_path):
    global logger
    log_hander = FileHandler(log_path)
    log_hander.formatter = log_type
    log_hander.push_application()
    logger = Logger('simulate_tcm')
