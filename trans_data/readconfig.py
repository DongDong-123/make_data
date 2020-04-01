import configparser
import os



curPath = os.path.dirname(os.path.realpath(__file__))
# curPath = os.getcwd()
cfgPath = os.path.join(curPath, "setting.ini")


class BaseConfig:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(cfgPath, encoding='utf-8')


class ReadMySqlConfig(BaseConfig):

    def host(self):
        return self.conf.get('mysql', 'HOST')

    def user(self):
        return self.conf.get('mysql', 'USER')

    def passwd(self):
        return self.conf.get('mysql', 'PASSWD')

    def db(self):
        return self.conf.get('mysql', 'DB')

    def port(self):
        return self.conf.get('mysql', 'PORT')


class ReadOraclConfig(BaseConfig):
    def info(self):
        return self.conf.get('oracl', 'info')


class ReadLogPath(BaseConfig):
    def log_path(self):
        return self.conf.get('log_file', 'log_path')


if __name__ == "__main__":
    # res = ReadMySqlConfig()
    # print(res.port(),res.host(),res.user(),res.passwd(),res.db())

    res_log = ReadLogPath()
    print(res_log.log_path())