import logging
import os


class LogInfo:
    def __init__(self, file_name='run'):
        self.filename = "{}.log".format(file_name)

    def logger(self, level='INFO'):
        path = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(path):
            os.makedirs(path, mode=0o770)
        file = self.filename
        file_name = os.path.join(path, file)
        with open(file_name, 'w') as f:
            pass
        logging.basicConfig(level=level, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', filename=file_name)

        return logging


