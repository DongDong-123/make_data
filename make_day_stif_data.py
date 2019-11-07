from create_data import make_stan_stif
from Common import *
from readConfig import ReadConfig
import pymysql
from save_to_csv import write_to_csv
from mysql_to_file import Wirte_to_file

config = ReadConfig()
HOST = config.get_host()
USER = config.get_user()
PASSWD = config.get_password()
DB = config.get_db()

def connnect_mysql(table_name, begin, end):
    conn = pymysql.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, charset="utf8")
    cur = conn.cursor()
    sql = "select tp.busi_reg_no, tp.client_tp, tp.smid, tp.ctnm, tp.citp, tp.citp_ori, tp.citp_nt, tp.ctid, " \
          "tp.ctid_edt, tb.act_tp, tb.act_cd, tb.cabm from {} as tp join t_stan_bact as tb on " \
          "tp.busi_reg_no = tb.ctif_id limit {},{};".format(table_name, begin, end)
    cur.execute(sql)
    conn.commit()
    query_result = cur.fetchall()
    cur.close()
    conn.close()
    return query_result


def process_data(data_query, ctif_tp_num, stif_time, file_date_time):
    write_data = Wirte_to_file()
    datas = []
    for data in data_query:
        info_data_dict = {
            "busi_reg_no": data[0],
            "client_tp": data[1],
            "smid": data[2],
            "ctnm": data[3],
            "citp": data[4],
            "citp_ori": data[5],
            "citp_nt": data[6],
            "ctid": data[7],
            "ctid_edt": data[8]
        }
        bact_data_dict = {
            "act_tp": data[9],
            "act_cd": data[10],
            "cabm": data[11]
        }
        for num in range(10):
            t_stan_stif, stan_stif_connect = make_stan_stif(info_data_dict, bact_data_dict, ctif_tp_num, stif_time)
            datas.append(stan_stif_connect)

    file_name = "t_stan_stif".split("_")[-1] + "_" + file_date_time
    print(len(datas))
    write_data.write_to_csv(file_name + ".csv", datas)


def run(table_name, file_date_time, begin, end):
    if table_name == "t_stan_person":
        # 主体类别，1个人，2，机构
        ctif_tp_num = 1
    else:
        ctif_tp_num = 2

    stif_time = "".join(file_date_time.split("-"))
    # print(stif_time)
    query_result = connnect_mysql(table_name, begin, end)
    # print(len(query_result), query_result)
    process_data(query_result, ctif_tp_num, stif_time, file_date_time)


if __name__ == "__main__":
    # table_name = "t_stan_org"
    table_name = "t_stan_person"
    file_date_time = "2019-11-07"
    begin = 0
    end = 2
    run(table_name, file_date_time, begin, end)
