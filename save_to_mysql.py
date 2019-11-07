import pymysql
from readConfig import ReadConfig

read_config = ReadConfig()
HOST = read_config.get_host()
USER = read_config.get_user()
PASSWORD = read_config.get_password()
DB = read_config.get_db()


class Save_MySQL:
    """
    数据存到MySQL，传入表名，表字段，和值
    """

    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset="utf8")
        self.curs = self.conn.cursor()

    def save(self, table_name, words, valu):
        va = []
        tt = words.split(",")
        # print(tt)
        for word in tt:
            # print(word)
            word = word.strip()
            # print("{}".format(word.strip()), valu.get(word))
            va.append(valu.get(word))
        va = tuple(va)
        sql = "insert into {}({}) VALUES {}".format(table_name, words, va)
        # print(sql)
        self.curs.execute(sql)

        # return curs

    def commit(self):
        self.conn.commit()

    def quit(self):
        self.curs.close()
        self.conn.close()


if __name__ == "__main__":
    tt = Save_MySQL()
    words = 'ctif_id,ctif_tp,tel_tp,tel,is_rp'
    # valu = '"t1", "1", "11", "16619922387", "1"'
    valu = {
        "ctif_id": "t2",
        "ctif_tp": "1",
        "tel_tp": "11",
        "tel": "16619923387",
        "is_rp": "1"
    }
    curs = tt.save("t_stan_tel", words, valu)
    tt.quit()
    # va = ''
    # tt = words.split(",")
    # print(tt)
    # for word in tt:
    #     print(word)
    #     print("{}".format(word), valu.get(word))
    #     va += valu.get(word)
