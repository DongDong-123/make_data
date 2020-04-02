import pymysql
from trans_data import loggers
from trans_data import readconfig
import cx_Oracle as oracle


class ConnectMysql:
    def __init__(self):
        self.conf = readconfig.ReadMySqlConfig()
        self.loginfo = loggers.LogInfo()
        self.log = self.loginfo.logger('DEBUG')

    def connect(self):
        try:
            conn = pymysql.connect(host=self.conf.host(), user=self.conf.user(), passwd=self.conf.passwd(), db=self.conf.db(), port=int(self.conf.port()),charset='utf8')
            cur = conn.cursor()
            self.log.info('database connect success!')
        except Exception as e:
            self.log.error('database connect false!')
            self.log.error(e)
            conn, cur = None, None

        return conn, cur

    def excue(self, conn, cur, sql):
        try:
            cur.execute(sql)
            conn.commit()
            data = cur.fetchall()
            self.log.info('execute {} success!'.format(sql))
            if data:
                return data
        except Exception as e:
            self.log.info('execute {} false!'.format(sql))
            self.log.error(e)
            return ''

    def close(self, conn, cur):
        try:
            cur.close()
            conn.close()
        except Exception as e:
            self.log.error('close database error！')
            self.log.error(e)


class ConnectOracl:
    def __init__(self):
        self.conf = readconfig.ReadOraclConfig()
        self.loginfo = loggers.LogInfo()
        self.log = self.loginfo.logger('DEBUG')

    def connect(self):
        try:
            conn = oracle.connect(self.conf.info())
            cur = conn.cursor()
            self.log.info('database connect success!')
        except Exception as e:
            self.log.error('database connect false!')
            self.log.error(e)
            conn, cur = None, None
        return conn, cur

    def excue(self, conn, cur, sql):
        try:
            cur.execute(sql)
            conn.commit()
            self.log.info('execute {} success!'.format(sql))
        except Exception as e:
            self.log.info('execute {} false!'.format(sql))
            self.log.error(e)

    def close(self, conn, cur):
        try:
            cur.close()
            conn.close()
        except Exception as e:
            self.log.error('close database error！')
            self.log.error(e)


if __name__ == "__main__":
    co = ConnectMysql()
    print(co.conf.host(), type(co.conf.host()))
    cn, cu = co.connect()
    if cn:
        print('ok')
        co.close(cn, cu)
    else:
        print("fail")


