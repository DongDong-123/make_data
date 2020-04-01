import logging
from trans_data import readconfig


class LogInfo:
    def __init__(self):
        self.conf = readconfig.ReadLogPath()
        self.path = self.conf.log_path()

    def logger(self, level='INFO'):
        logging.basicConfig(level=level, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', filename=self.path)

        return logging


