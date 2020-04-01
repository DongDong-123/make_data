from trans_data import connect
from trans_data import read_excel
from trans_data import loggers

log = loggers.logger("DEBUG")

file_path = r'E:\桌面文件夹\工作\make_data\trans_data\test\test.xls'
sheet_name = 'test'
table = 'tests'

sheet_to_table = {
    'org': 'org',
    'person': 'person',
    'stif': 'stif',
    'pack': 'pack',
    'back': 'back',
    'contact': 'contact',
}


class Scheduling:
    def __init__(self):
        self.cm = connect.ConnectMysql()

    def read_file(self):
        # 读取excel数据
        rd = read_excel.ReadExcel(file_path)
        file = rd.read_sheet_by_row(sheet_name)
        datas = []
        column_name = ''
        for index, elem in enumerate(file):
            if index == 0:
                column_name = ','.join(elem)
                log.info(column_name)
            else:
                datas.append(tuple(elem))

        return datas, column_name

    def make_sql(self, table, column, datas):
        for data in datas:
            sql = "insert into {}({}) VALUES {}".format(table, column, data)
            log.debug(sql)
            yield sql

    def save_to_database(self):
        datas, column_name = self.read_file()

        # 拼装sql
        sqls = self.make_sql(table, column_name, datas)

        # 写入数据库
        con, cur = self.cm.connect()
        for sql in sqls:
            self.cm.excue(con, cur, sql)

        self.cm.close(con, cur)

def run():
    read = Scheduling()




if __name__ == "__main__":
    # table = 'test'
    # column = ['co1', 'co2','co3']
    # column = ','.join(column)
    # datas = [[1,2,3],[3,4,5],[2,3,5]]
    # make_sql(table, column, datas)

    pass