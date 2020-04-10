import pymysql
from create_data import *
import json
from readConfig import ReadConfig


read_config = ReadConfig()
HOST = read_config.get_host()
USER = read_config.get_user()
PASSWORD = read_config.get_password()
DB = read_config.get_db()


def test1():
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="work_for_2019_10", charset="utf8")
    curs = conn.cursor()


    sql = "select * from dm_area"

    num = curs.execute(sql)
    conn.commit()
    print("数量", num)
    res = curs.fetchall()
    # file_code = compare_area_data()
    # print("数量2", len(file_code))
    # n = 0
    # province_code = ""
    code_dict = {}
    for data in res:
        number = str(data[0])
        print("num", number)
        if number in ["710000", "810000", "820000", "999999"]:
            code_dict[number] = data[1]
        else:
            code_2 = number[:2]
            province_code = code_2 + "0000"
            if number == province_code:
                code_dict[province_code] = {}
            else:
                code_4 = number[:4]
                # code_t_4 = number[2:]
                city_code = code_4 + "00"
                if number == city_code:
                    code_dict[province_code][city_code] = {}
                else:
                    code_tail = number[4:]
                    if code_dict.get(province_code):
                        if code_dict.get(province_code).get(city_code):
                            code_dict[province_code][city_code][number] = data[1]
                        else:
                            code_dict[province_code][number] = data[1]
                    else:
                        code_dict[number] = data[1]


    print(code_dict)

    code_dict = json.dumps(code_dict, ensure_ascii=False)

    with open("code_dict.txt", "w", encoding="utf-8") as f:
        f.write(code_dict)


    # print("不同数量", n)
    # print(res)

    curs.close()
    conn.close()


def test2():
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, charset="utf8", port=3306)
    curs = conn.cursor()
    sql0 = "CREATE DATABASE (if not exists) work_data charset='utf8'; enging=innodb;"
    # sql = "select BUSI_CODE from dm_industry_compare"
    sql = "show databases;"

    num = curs.execute(sql)
    # conn.commit()
    res = curs.fetchall()
    sql2 = "use work_data;"
    curs.execute(sql2)
    sql3 = "show tables;"
    curs.execute(sql3)
    ress = curs.fetchall()
    print(ress)
    conn.commit()
    print(res)
    curs.close()
    conn.close()
    # for code in res:
    #     with open("incustry_code.txt", "a+", encoding="utf-8") as f:
    #         f.write(code[0] +",")


# test2()

def create_tables(sql):

    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db="main_body", charset="utf8", port=3306)
    curs = conn.cursor()

    curs.execute(sql)
    conn.commit()
    curs.close()
    conn.close()

def read_sql():
    root_path = os.getcwd()
    sql_path = os.path.join(root_path, "sql")
    print(sql_path)
    sql_file_list = os.listdir(sql_path)
    for sql_file in sql_file_list:
        with open(os.path.join(sql_path, sql_file), "r", encoding="utf-8") as f:
            sql = f.read()

        print(sql)
        yield sql


def run():
    sql0 = "CREATE DATABASE (if not exists) main_body charset='utf8'; enging=innodb;"
    create_tables(sql0)
    # sql_list = read_sql()
    # for sql in sql_list:
    #     create_tables(sql)


run()