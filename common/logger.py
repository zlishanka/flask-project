import os
import sys
import logging, logging.handlers
import time
from datetime import datetime

class LoggingLevel:
    INFO = logging.INFO
    WARNING = logging.WARNING
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR


def logging_setup(log_file, log_level):
    log_handler = logging.handlers.TimedRotatingFileHandler(log_file, when='midnight')
    stdout_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d [%(levelname)s]\
                                    [%(process)d]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    formatter.converter = time.gmtime       # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.addHandler(stdout_handler)
    logger.setLevel(log_level) 

def logging_info(fmt, *arg):
    logging.info("%s [Info][pid=%s] "+fmt, str(datetime.now()), os.getpid(), *arg)

def logging_warning(fmt, *arg):
    logging.error("%s [Warning][pid=%s] "+fmt, str(datetime.now()), os.getpid(), *arg) 

def logging_debug(fmt, *arg): 
    logging.debug("%s [Debug][pid=%s] "+fmt, str(datetime.now()), os.getpid(), *arg)