import xlrd
import csv
import os
import re


class Excel:
    def __init__(self, path, sheet_index=0):
        self.work_book = xlrd.open_workbook(path)
        self.sheet = self.work_book.sheet_by_index(sheet_index)
        self.row = self.sheet.nrows  # 总行数
        self.col = self.sheet.ncols  # 总列数

    def get_sheel(self, work_book, name):
        # 根据索引获取sheet，从0开始
        sheet_content_by_index = work_book.sheet_by_index(0)

        # 根据sheet名字获取sheet
        sheet_content_by_name = work_book.sheet_by_name(name)
        return sheet_content_by_index

    def get_info_by_row(self):
        """
        逐行读取所有数据
        :return: 生成器，一行数据组成的列表
        """
        for num in range(self.row):
            yield list(map(self.process_float, self.sheet.row_values(num)))

    def get_info_by_col(self):
        """
        逐列读取所有数据
        :return: 生成器，一列数据组成的列表
        """
        for num in range(self.col):
            yield list(map(self.process_float, self.sheet.col_values(num)))

    def get_info_by_cell(self):
        """
        按单元格逐行读取数据，(可选择按列)
        :return: 生成器  包含单元格内容、类型元组的列表
        """
        for row in range(1, self.row):
            for col in range(self.col):
                sheet_cell_value = self.sheet.cell(row, col).value
                sheet_cell_value = list(map(self.process_float, [sheet_cell_value]))[0]
                sheet_value_type = self.get_cell_type(row, col)
                # sheet_cell_value = sheet_1.cell_value(row, col).encode('utf-8')
                # sheet_cell_value = sheet_1.row(row)[col].value.encode('utf-8')
                yield (sheet_cell_value, sheet_value_type)

    def get_cell_type(self, row_index, col_index):
        """
        获取指定单元格内容的数据类型（ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error）
        :param row_index: int 行索引
        :param col_index: int 列索引
        :return: str 单元格的类型
        """
        sheet_value_type = self.sheet.cell(row_index, col_index).ctype
        type_dict = {0: 'empty', 1: 'string', 2: 'number', 3: 'date', 4: 'boolean', 5: 'error'}
        return type_dict[sheet_value_type]

    def process_float(self, parm):
        """
        判断是否为float类型，且为整数，整数则转换为int，
        :param parm: all type
        :return: 原数据或转换为int类型的整数
        """
        if isinstance(parm, float) and parm == int(parm):
            return int(parm)
        else:
            return parm


def WriteExcel(datas):
    head = ''
    file_name = 'test.csv'
    file_path = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(file_path):
        csvFile = open(file_path, "a", encoding="utf-8-sig", newline='')
        writer = csv.writer(csvFile)
        writer.writerows([head, datas])
        csvFile.close()
    else:
        csvFile = open(file_path, "a", encoding="utf-8-sig", newline='')
        writer = csv.writer(csvFile)
        writer.writerow(datas)
        csvFile.close()



def process_data(data, t):
    patt = '\d\.'

    data = '{}.'.format(t) + str(data)
    return data



def main():
    n = 0
    t = 2
    path = 'E:\\3.42\\15\\40-ZKQS-TF-OT.xlsx'
    res = Excel(path)
    # row_infos = res.get_info_by_cell()
    row_infos = res.get_info_by_row()
    temp = []
    for info in row_infos:
        n = n+1
        print(info)
        if info[0] != '':
            if not temp:
                temp = info
            else:
                WriteExcel(temp)
                temp.clear()
                t = 2
                info[6] = process_data(info[6], 1)
                info[7] = process_data(info[7], 1)
                temp = info
        else:
            temp_info6 = process_data(info[6], t)
            temp_info7 = process_data(info[7], t)
            temp[6] = str(temp[6]) + '\n' + temp_info6
            temp[7] = str(temp[7]) + '\n' + temp_info7
            t += 1



        if n > 100:
            break



if __name__ == "__main__":
    main()
    datas = [2,3]
    # WriteExcel(datas)