import logging
import time
import os

class MyLogger:
    def __init__(self):
        # 定义一个记录器
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        # 定义一个控制台输出的handler
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO) # 设置处理器的日志级别

        log_path = os.path.dirname(__file__)
        log_path = log_path + os.path.sep + ".." + os.path.sep + 'log' # os.path.sep代表了操作系统特定的路径分隔符
        # 判断日志目录是否存在，不存在则创建
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        log_file = "{}.log".format(time.strftime("%Y-%m-%d"))
        # 设置日志文件名
        filename = os.path.join(log_path, log_file)

        # 定义一个文件输出的handler
        fh = logging.FileHandler(filename, encoding="utf-8")
        fh.setLevel(logging.INFO) # 设置处理器的日志级别

        # 设置日志输出格式
        formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s|%(lineno)s|%(message)s")
        # 设置处理器的日志输出格式
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        # 将处理器添加到记录器中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

logger = MyLogger().logger