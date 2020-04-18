import time
import datetime
from create_data import main, main2


def get_parm():
    with open('parm.txt', 'r', encoding='utf-8') as f:
        res = f.read()

    parm = res.split(',')
    n = int(parm[0])
    t = int(parm[1])
    return n, t


def updtae_parm(n, t):
    with open('parm.txt', 'w', encoding='utf-8') as f:
        f.write("{},{}".format(n, t))


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


def run1():

    n, t = get_parm()
    start_time = time.time()
    # threads = []
    # for count in range(10):
    #     t = Thread(target=main, args=(count*10, (count+1)*10))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()
    # -------------------------单线程
    # 数据条数
    o = 200000

    for m in range(1):
        st = datetime.datetime.strptime(str(t), "%Y%m%d")
        file_date_time = str(st)[:10]
        stif_time = "{}100000".format(t)

        main(n, n + o, stif_time, file_date_time)
        n += o
        t += 1
    end_time = time.time()
    print(end_time - start_time)  # 13

    # for i in range(100):
    #     # tt = make_register_date()
    #     ss = random.choice([
    #         "01",  # 互联网支付
    #         "02",  # 银行卡收单
    #         "03",  # 预付卡发行与受理
    #         "04",  # 移动电话支付
    #         "05",  # 固定电话支付
    #         "06",  # 数字电视支付
    #         "07"  # 货币汇兑
    #     ])
    #     print(ss)
    #     tt = make_tcif_id_data(ss)
    #
    #     print(tt)

    # ctid_edt = "20170506"
    # ctid_edt = "99991231"
    # tt = make_iss_dt_data(ctid_edt)
    # print(tt)
    #
    # dd = make_country_data()
    # print(dd)
    # tt = make_province_city_process_data("412825")
    # print(tt)
    updtae_parm(n, t)


def run2():
    n, t = get_parm()
    for m in range(1):
        non_line = 0

        st = datetime.datetime.strptime(str(t), "%Y%m%d")
        file_date_time = str(st)[:10]
        stif_time = "{}100000".format(t)
        t += 1
        num = 0
        with open('{}.txt'.format(file_date_time)) as f:
            while num < 8:
                try:
                    lines = f.readlines(1)
                except Exception as e:
                    print(e)
                    break
                num += 1
                print(lines)
                if isinstance(lines, list) and not lines:
                    line = lines[0]
                    line = line.strip()
                    main2(stif_time, file_date_time, line)
                else:
                    non_line += 1

                if non_line > 3:
                    break

    updtae_parm(n, t)


def run3():
    ''' 无交易 '''
    n, t = get_parm()
    non_line = 0

    st = datetime.datetime.strptime(str(t), "%Y%m%d")
    file_date_time = str(st)[:10]
    stif_time = "{}100000".format(t)
    t += 1
    num = 0
    # with open('{}.txt'.format(file_date_time)) as f:
    with open('file2.txt', 'r', encoding='utf-8') as f:
    # with open('busi_no.txt', 'r', encoding='utf-8') as f:

        try:
            lines = f.readlines()
        except Exception as e:
            print(e)

    while num < len(lines):
        line = lines.pop()
        line = line.strip()
        # line = 'a' + line
        main2(stif_time, file_date_time, line)

        # for test
        num += 1
        if num >200000:
            break

    updtae_parm(n, t)

import random




def run4():
    """
    一条主体，250万交易
    :return:
    """
    # 主体客户号
    # 当天随机交易时间
    n, t = get_parm()
    non_line = 0

    st = datetime.datetime.strptime(str(t), "%Y%m%d")
    file_date_time = str(st)[:10]
    stif_time = make_random_trade_time(t)
    t += 1
    num = 0
    # with open('{}.txt'.format(file_date_time)) as f:
    with open('less_busi.txt', 'r', encoding='utf-8') as f:
        try:
            lines = f.readlines()
        except Exception as e:
            print(e)

    while num < len(lines):
        line = lines.pop()
        line = line.strip()
        line = 'a' + line
        main2(stif_time, file_date_time, line)

        num += 1
        # for test
        # if num > 1:
        #     break

    updtae_parm(n, t)



if __name__ == "__main__":
    # run1()  # 自动生成客户号
    # run2()  # 传入已有客户号
    run3()  # 传入已有客户号
