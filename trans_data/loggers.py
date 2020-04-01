import logging


def logger(level='INFO'):
    logging.basicConfig(level=level, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s', filename='log/test.log')

    return logging


