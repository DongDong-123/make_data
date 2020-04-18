import cx_Oracle as oracle


def connect_46(info, sql):

    db = oracle.connect(info)
    # user用户名；password密码；服务器地址+端口号；service_name服务名
    # （注：在plsql连接Oracle的instanceclient中的tnsnames.ora中配置的有。但是Python连接Oracle不需要配置tnsnames.ora）
    cursor = db.cursor()
    # contract_inst_id

    cursor.execute(sql)
    # data = cursor.fetchone()
    data = cursor.fetchall()
    print(len(data), data)
    cursor.close()
    db.close()
    return data


# ctnm = opposite_name


if __name__ == "__main__":
    info = ''  # 投行新系统
    # sql = 'select contract_inst_id from V_RH_CONTRACT_INFO'
    # TCNM,
    sql = 'select contract_inst_id,TCNM from V_RH_CONTRACT_INFO'

    data1 = connect_46(info, sql)


    info = ''
    # contract_name,
    sql = 'select contract_id,contract_name from V_INV_CONTRACT'
    data2 = connect_46(info, sql)
    n = 0
    for name in data2:
        name2 = int(name[0])
        # print(name2)
        for elem in data1:
            if int(elem[0]) == name2:
                print(name, elem)
                n+=1

    print(n)
        # else:
        #     print("no")

