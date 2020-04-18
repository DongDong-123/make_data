import configparser
import os

curPath = os.path.dirname(os.path.realpath(__file__))
cfgPath = os.path.join(curPath, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfgPath, encoding='utf-8')

    def get_user(self):
        return self.cfg.get("mysql", "USER")

    def get_password(self):
        return self.cfg.get("mysql", "PASSWORD")

    def get_db(self):
        return self.cfg.get("mysql", "DB")

    def get_host(self):
        return self.cfg.get("mysql", "HOST")


class SendEmailConfig:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(cfgPath, encoding='utf-8')

    def get_smtpserver(self):
        return self.cfg.get("EMAIL", "SMTPSERVER")

    def get_user(self):
        return self.cfg.get("EMAIL", "USER")

    def get_password(self):
        return self.cfg.get("EMAIL", "PASSWORD")

    def get_sender(self):
        return self.cfg.get("EMAIL", "SENDER")

    def get_receiver(self):
        return eval(self.cfg.get("EMAIL", "RECEIVER"))


if __name__ == "__main__":
    res = ReadConfig()
    # print(res.redis_host())
    # print(res.redis_password())