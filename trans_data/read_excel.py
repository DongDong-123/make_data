import xlrd
import os

from trans_data import loggers


class ReadExcel:
    def __init__(self, file_name):
        self.book = xlrd.open_workbook(file_name)
        self.sheets = self.book.sheet_names()
        self.log = loggers.logger('DEBUG')

    def read_sheet_by_row(self, sheet_name):
        self.log.info("sheet list: {}".format(self.sheets))
        if sheet_name in list(self.sheets):
            sheet = self.book.sheet_by_name(sheet_name)
            rows = sheet.nrows
            self.log.debug('sheet name:{}'.format(sheet_name))
            self.log.debug('rows:{}'.format(rows))
            for num in range(rows):
                yield sheet.row_values(num)
        else:
            self.log.info('sheet {} not exises!'.format(sheet_name))


if __name__ == "__main__":
    file = r'E:\桌面文件夹\工作\make_data\trans_data\test\test.xls'
    rd = ReadExcel(file)
    sheets = rd.sheets
    if 'test' in sheets:
        print('okk')
