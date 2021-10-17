import logging, logging.handlers
import os

BaseDir = os.path.dirname(__file__)


#  os.path.dirname此方法的作用是用来获取用文件的路径
#  __file__表示的是当前文件(config.py)


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志的级别
    logger.setLevel(logging.DEBUG)
    # 创建处理器
    fh = logging.handlers.TimedRotatingFileHandler(BaseDir + "/log/log.log", when="midnight",
                                                   interval=1, backupCount=7)
    sh = logging.StreamHandler()
    fh.setLevel(logging.INFO)
    sh.setLevel(logging.INFO)
    # 创建格式器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt=fmt)
    # 在处理器添加格式器
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # 在日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(fh)
