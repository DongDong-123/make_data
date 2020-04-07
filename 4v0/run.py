import time
import datetime
from create_data import main, main2
import os


def get_parm():
    with open('parm.txt', 'r', encoding='utf-8') as f:
        res = f.read()

    parm = res.split(',')
    n = int(parm[0])
    t = int(parm[1])
    return n,t


def updtae_parm(n, t):
    with open('parm.txt', 'w', encoding='utf-8') as f:
        f.write("{},{}".format(n, t))


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
    o = 100

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
        st = datetime.datetime.strptime(str(t), "%Y%m%d")
        file_date_time = str(st)[:10]
        stif_time = "{}100000".format(t)

        num = 0
        with open('busi_no.txt') as f:
            while num < 8:
                lines = f.readlines(1)
                num += 1
                print(lines)
                if isinstance(lines, list):
                    line = lines[0]
                    line = line.strip()
                    main2(stif_time, file_date_time, line)

    updtae_parm(n, t)


if __name__ == "__main__":
    run1()  # 自动生成客户号
    # run2()  # 传入已有客户号
