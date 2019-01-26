import os, sys
import shutil
from datetime import datetime


class LoggerMeta(type):
    LOG_DIR = 'logs'
    MAX_LOG_FILE_COUNT = 10

    def __init__(cls, *args, **kw):
        super().__init__(*args, **kw)

        cls.terminal = sys.stdout

        os.makedirs(cls.LOG_DIR, exist_ok=True)
        fnames = os.listdir(cls.LOG_DIR)
        for i in range(cls.MAX_LOG_FILE_COUNT):
            cls.fname = f'{i}.txt'
            if cls.fname not in fnames:
                break
        else:
            shutil.rmtree(cls.LOG_DIR)
            cls.fname = '0.txt'

        cls.log = open(os.path.join(cls.LOG_DIR, cls.fname), 'w')

    def __del__(cls):
        cls.flush()
        cls.log.close()
        sys.stdout = cls.terminal

    @staticmethod
    def _log(level, string):
        if not ':' in string:
            string = ':' + string

        category, message = [i.strip() for i in string.split(':', 1)]
        print(f'[{level.ljust(8)}] [{category.ljust(8)}] {message}')

    def debug(cls, msg):
        cls._log('DEBUG', msg)

    def info(cls, msg):
        cls._log('INFO', msg)

    def warning(cls, msg):
        cls._log('WARNING', msg)

    def error(cls, msg):
        cls._log('ERROR', msg)

    def write(cls, msg):
        cls.terminal.write(msg)
        cls.log.write(msg)
        cls.log.flush()

    def flush(cls):
        cls.terminal.flush()
        cls.log.flush()

    def get_log(cls):
        with open(os.path.join(cls.LOG_DIR, cls.fname)) as f:
            return f.read()


class Logger(metaclass=LoggerMeta):
    pass
