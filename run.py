import time

def to_csv():
    from create_data import main
    start_time = time.time()
    # threads = []
    # for count in range(10):
    #     t = Thread(target=main, args=(count*10, (count+1)*10))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()
    # -------------------------单线程
    # file_date_time = "2019-10-17"
    # stif_time = "201910170900"
    # person_new3_25748
    main(4000, 6000)
    end_time = time.time()
    print(end_time - start_time)  # 13


def to_mysql():
    from create_data_sql import main
    start_time = time.time()
    # threads = []
    # for count in range(10):
    #     t = Thread(target=main, args=(count*10, (count+1)*10))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()
    # -------------------------单线程
    # file_date_time = "2019-10-17"
    stif_time = "201910170900"
    main(100000, 200000, 10, stif_time)
    end_time = time.time()
    print(end_time - start_time)  # 13


def mysql_to_csv():
    from mysql_to_file import main
    table_name = "t_stan_tel"
    begin = 1
    end = 10
    file_date_time = "2019-10-17"
    main(table_name, begin, end, file_date_time)


def data_to_file():
    threads = []
    # for count in range(10):
    #     t = Thread(target=main, args=(count*10, (count+1)*10))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()

if __name__ == "__main__":
    # to_mysql()
    to_csv()

    # mysql_to_csv()