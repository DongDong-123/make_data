# coding=utf-8

import pymysql
import csv
import os
from readConfig import ReadConfig
import loggers
import time

config = ReadConfig()
HOST = config.get_host()
USER = config.get_user()
DB = config.get_db()
PASSWD = config.get_password()
loginfo = loggers.LogInfo()
log = loginfo.logger('DEBUG')
busi_no = set()


class Read_for_mysql:
    """使用前先确认配置文件信息是否正确"""

    def __init__(self):
        self.conn = pymysql.connect(host=HOST, user=USER, password=PASSWD, db=DB, charset="utf8")
        self.curs = self.conn.cursor()
        loginfo = loggers.LogInfo(log_name)
        self.log = loginfo.logger('DEBUG')

    def read(self, table_name, begin, end):
        """
        组装sql，查询数据
        :param table_name:
        :param begin:
        :param end:
        :return:
        """
        # sql_date = "select tstm from t_stan_stif limit "
        # sql = "select * from {} LIMIT {}, {};".format(table_name, begin, end)

        sql = "select ctif_id,ctif_tp,client_tp,smid,ctnm,citp,citp_nt,ctid,cbat,cbac,cabm,ctat,ctac,cpin,cpba,cpbn,ctip,tstm,cttp,tsdr,crpp,crtp,crat,tcif_id,tcnm,tsmi,tcit,tcit_nt,tcid,tcat,tcba,tcbn,tctt,tcta,tcpn,tcpa,tpbn,tcip,tmnm,bptc,pmtc,ticd,busi_type,trans_type,pos_dev_id,trans_stat,bank_stat,mer_prov,mer_area,pos_prov,pos_area,mer_unit,extend1,iofg,trans_channel,ctmac,(case when balance is null then '' else balance end),acc_flag,ctid_edt,tran_flag,trans_order,trans_cst_type from {} LIMIT {}, {};".format(
            table_name, begin, end)
        self.log.info(sql)
        self.curs.execute(sql)
        data_tuble = self.curs.fetchall()
        return data_tuble


class Wirte_to_file:
    """
    写入CSV文件，先判断文件是否存在，若存在，则直接写入数据，若不存在，创建文件，写入表头后再添加数据
    """

    def __init__(self):
        self.loginfo = loggers.LogInfo(log_name)
        self.log = self.loginfo.logger('DEBUG')

    def write_to_csv(self, file_name, datas):
        path = os.getcwd()
        new_path = os.path.join(path, "vip")
        if not os.path.exists(new_path):
            os.makedirs(new_path, exist_ok=False)
        t_stan_stif_header = ["CTIF_ID主体客户号", "CTIF_TP 1个人2 机构主体类别", "CLIENT_TP 1客户 2商户客户类别(1代表客户 2代表商户)",
                              "SMID主体特约商户编码(30)", "CTNM", "CITP主体身份证件/证明文件类型(2)", "citp_ori主体身份证件/证明文件类型原值",
                              "CITP_NT主体身份证件/证明文件类型说明(32)", "CTID可疑主体身份证件/证明文件号码(32)", "CBAT交易主体的银行账号种类(2)",
                              "CBAC交易主体的银行账号(64)", "CABM交易主体银行账号的开户行名称(128)", "CTAT主体的交易账号种类（2）", "CTAC主体的交易账号（64）",
                              "CPIN主体所在支付机构的名称（128）", "CPBA主体所在支付机构的银行账号（64）", "CPBN主体所在支付机构的银行账号的开户行名称（128）",
                              "CTIP主体的交易IP地址", "TSTM交易时间", "CTTP货币资金转移方式（4）", "TSDR资金收付标志", "CRPP资金用途（500）",
                              "CRTP交易币种（3）", "CRAT交易金额（接口20）", "TCIF_ID交易对手ID（100002）", "TCNM交易对手姓名/名称（128）",
                              "TSMI交易对手特约商户编码（30）", "TCIT交易对手证件/证明文件类型（2）", "tcit_ori交易对手证件/证明文件类型原值",
                              "TCIT_NT交易对手证件/证明文件类型说明（32）", "TCID交易对手证件/证明文件号码（32）", "TCAT交易对手的银行账号种类（）",
                              "TCBA交易对手的银行账号（64）", "TCBN交易对手银行账号的开户行名称（128）", "TCTT交易对手的交易账号种类（2）", "TCTA交易对手的交易账号（64）",
                              "TCPN交易对手所在支付机构的名称（128）", "TCPA交易对手所在支付机构的银行账号（64）", "TPBN交易对手所在支付机构银行账号的开户行名称（128）",
                              "TCIP交易对手的交易IP地址（15）", "TMNM交易商品名称（64）", "BPTC银行与支付机构之间的业务交易编码（64）",
                              "PMTC支付机构与商户之间的业务交易编码（64）", "TICD业务标识号（128）", "BUSI_TYPE", "trans_type", "pos_dev_id",
                              "trans_stat", "bank_stat", "mer_prov", "mer_area", "pos_prov", "pos_area", "mer_unit",
                              "extend1转换标识", "iofg 境内外标识", "trans_channel交易渠道", "ctmac交易主体发生的mac地址(32)", "balance账户余额",
                              "acc_flag交易对方账户类型", "ctid_edt主体身份证件/证明文件有效期截止日", "tran_flag对手账号标识", "trans_order交易订单号",
                              "trans_cst_type交易类型(客户定义) ", "crat_u交易金额折合美元", "crat_c交易金额折合人民币", "trans_way交易方式",
                              "agency_ctnm代办人姓名", "agency_citp代办人身份证件（证明文件）类型 ", "agency_ctid代办人身份证件（证明文件）号码 ",
                              "agency_country代办人国籍"]
        # t_stan_stif1_header = ["CTIF_ID主体客户号", "CTIF_TP 1个人2 机构主体类别", "CLIENT_TP 1客户 2商户客户类别(1代表客户 2代表商户)",
        #                        "SMID主体特约商户编码(30)", "CTNM", "CITP主体身份证件/证明文件类型(2)", "CITP_NT主体身份证件/证明文件类型说明(32)",
        #                        "CTID可疑主体身份证件/证明文件号码(32)", "CBAT交易主体的银行账号种类(2)", "CBAC交易主体的银行账号(64)",
        #                        "CABM交易主体银行账号的开户行名称(128)", "CTAT主体的交易账号种类（2）", "CTAC主体的交易账号（64）", "CPIN主体所在支付机构的名称（128）",
        #                        "CPBA主体所在支付机构的银行账号（64）", "CPBN主体所在支付机构的银行账号的开户行名称（128）", "CTIP主体的交易IP地址", "TSTM交易时间",
        #                        "CTTP货币资金转移方式（4）", "TSDR资金收付标志", "CRPP资金用途（500）", "CRTP交易币种（3）", "CRAT交易金额（接口20）",
        #                        "TCIF_ID交易对手ID（100002）", "TCNM交易对手姓名/名称（128）", "TSMI交易对手特约商户编码（30）",
        #                        "TCIT交易对手证件/证明文件类型（2）", "TCIT_NT交易对手证件/证明文件类型说明（32）", "TCID交易对手证件/证明文件号码（32）",
        #                        "TCAT交易对手的银行账号种类（）", "TCBA交易对手的银行账号（64）", "TCBN交易对手银行账号的开户行名称（128）",
        #                        "TCTT交易对手的交易账号种类（2）", "TCTA交易对手的交易账号（64）", "TCPN交易对手所在支付机构的名称（128）",
        #                        "TCPA交易对手所在支付机构的银行账号（64）", "TPBN交易对手所在支付机构银行账号的开户行名称（128）", "TCIP交易对手的交易IP地址（15）",
        #                        "TMNM交易商品名称（64）", "BPTC银行与支付机构之间的业务交易编码（64）", "PMTC支付机构与商户之间的业务交易编码（64）",
        #                        "TICD业务标识号（128）", "BUSI_TYPE", "trans_type", "pos_dev_id", "trans_stat", "bank_stat",
        #                        "mer_prov", "mer_area", "pos_prov", "pos_area", "mer_unit", "extend1转换标识", "iofg 境内外标识",
        #                        "trans_channel交易渠道", "ctmac交易主体发生的mac地址(32)", "balance账户余额", "acc_flag交易对方账户类型",
        #                        "ctid_edt主体身份证件/证明文件有效期截止日", "tran_flag对手账号标识", "trans_order交易订单号",
        #                        "trans_cst_type交易类型(客户定义) ", "citp_ori主体身份证件/证明文件类型原值", "tcit_ori交易对手证件/证明文件类型原值",
        #                        "crat_u交易金额折合美元", "crat_c交易金额折合人民币", "trans_way交易方式", "agency_ctnm代办人姓名",
        #                        "agency_citp代办人身份证件（证明文件）类型 ", "agency_ctid代办人身份证件（证明文件）号码 ",
        #                        "agency_country代办人国籍"]  # 3.42数据导入唯品会表头
        #
        # data = "&#@".join([str(elem) for elem in datas])
        file_path = os.path.join(new_path, file_name)
        if not os.path.exists(file_path):
            head = os.path.split(file_name)[-1]
            head = head.split(".")[0]
            head = "t_stan_" + head.split("_")[0] + "_header"
            head = "&#@".join([str(elem) for elem in eval(head)])
            # print(head)

            csvFile = open(file_path, "a", encoding="utf-8-sig", newline='')
            writer = csv.writer(csvFile)
            # datas.insert(0, head)
            # writer.writerows([[elem] for elem in datas])
            writer.writerows([[head], [datas]])
            csvFile.close()
        else:
            csvFile = open(file_path, "a", encoding="utf-8-sig", newline='')
            writer = csv.writer(csvFile)
            writer.writerow([datas])
            csvFile.close()


def get_busi_no(data, date):

    ticd = data[41]
    tstm = data[17]  # 交易时间

    data = list(data)
    date = date.replace('-', '')
    # data[0] = 'a' + data[0]  # 修改客户号
    data[0] = 'MC0100000000000004'  # 修改客户号
    data[3] = data[0]
    # data[0] = data[0] + '1'
    data[17] = date + data[17][8:]
    data.insert(6, '')
    data.insert(28, '')
    data[43] = data[43] + '6'  # 业务标识号 1,2,3,4,5,6
    data[-1] = data[-1].strip()

    ctif_id = data[0]  # 主体客户号
    ctif_tp = data[1]  # 主体类别
    client_tp = data[2]  # 客户类别
    info = ','.join([ctif_id, ctif_tp, client_tp])

    data.extend(['' for i in range(7)])
    print(data)
    return data, info


def writes(datas, file_time):
    """ 存储客户号、主体类别、客户类别，
    数据格式 '存储客户号,主体类别,客户类别'
    """
    infos = list(datas)
    with open('{}.txt'.format(file_time), '+a', encoding='utf-8') as f:
        for info in infos:
            f.write(info + '\n')


def to_csv(all_datas, busi_no, file_name, write_data, file_time, sgin=None):
    """拼接数据，写入csv"""
    # data_list = []
    for data in all_datas:
        data, info = get_busi_no(data, file_time)
        busi_no.add(info)
        process_data = "&#@".join(data)
        # data_list.append(process_data)
        if len(busi_no) > 100:
            writes(busi_no, file_time)
            busi_no.clear()
        elif sgin:
            writes(busi_no, file_time)
            busi_no.clear()

        write_data.write_to_csv(file_name + ".csv", process_data)


parm_file = 'vip.txt'


def run(table_name, file_time):

    read_data = Read_for_mysql()
    write_data = Wirte_to_file()
    # file_name = table_name.replace('1', '')
    file_name = table_name.split("_")[1] + "_" + file_time

    with open(parm_file, 'r', encoding='utf-8') as f:
        res = f.read()

    parm = res.split(',')
    begin = int(parm[0])
    end = int(parm[1])
    num = 0
    all_datas = []  # 读取的数据，每10000条，写入文件一次
    # 去重存储客户号

    while num < 300:  # 循环次数，乘每次取的数量，等于总条数

        all_data = read_data.read(table_name, begin, end)
        all_datas.extend(list(all_data))
        begin = begin + end
        if len(all_datas) > 100:
            log.info('begin write file{}'.format(begin))
            to_csv(all_datas, busi_no, file_name, write_data, file_time)
            all_datas.clear()
        num += 1

    if all_datas:
        log.info('finished to write')
        to_csv(all_datas, busi_no, file_name, write_data, file_time, sgin=1)


    return begin, end

import random


def make_random_trade_time(trade_date):
    """
    生成当天的随机交易时间
    :param trade_date:
    :return:
    """
    one_date_time = 86400
    random_num = random.randint(1, one_date_time)
    # trade_date = '2020-04-12'
    trade_date = '{}-{}-{}'.format(trade_date[:4], trade_date[4:6],trade_date[6:])
    trade_date = '{} 00:00:00'.format(trade_date)
    tt = time.strptime(trade_date, '%Y-%m-%d %H:%M:%S')
    tt = time.mktime(tt)
    random_time = int(tt) + random_num
    # print(time.localtime())
    # print(random_time)
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(random_time))
    # print(date_time,type(date_time))
    # print(tt)
    return_time = date_time.replace('-', '').replace(':', '').replace(' ', '')
    # print(return_time)

    return return_time

def main():
    table_name = "load_stif_1k"
    with open(parm_file, 'r', encoding='utf-8') as f:
        res = f.read()

    parm = res.split(',')
    date = parm[2]
    file_date_time = date[:8] + "{}"
    print("file_date_time", file_date_time)
    n = int(date.split('-')[-1])
    print(n)
    begin_time = time.time()
    for mm in range(1):

        file_date_times = file_date_time.format(n)
        global log_name
        log_name = file_date_times
        print(file_date_times)
        begin, end = run(table_name, file_date_times)
        n += 1
        print(n)
        with open(parm_file, 'w', encoding='utf-8') as f:
            f.write("{},{},{}".format(begin, end, file_date_times))
    end_time = time.time() - begin_time
    log.info('cost_time: {}'.format(end_time))


if __name__ == "__main__":

    main()
