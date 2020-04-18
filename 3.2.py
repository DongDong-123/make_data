# from save_to_csv import write_to_csv
from Common import *


# 生成个人表
def make_stan_person(num1, num2):
    """字段列表
    "busi_reg_no":"客户号",
    "ctnm":"客户名称",
    "cten":"拼音/英文名称",
    "client_tp":"客户类别",1客户，2商户
    "account_tp":"账户分类",1/2/3代表1、2、3类账号
    "busi_type":"业务类型",
    "smid":"主体特约商户编号",
    "citp":"证件类型",
    "citp_ori":"证件类型原值",
    "citp_nt":"证件类型说明",
    "ctid":"证件号码",
    "ctid_edt":"证件有效期",
    "sex":"性别",
    "country":"国籍",
    "nation":"民族",
    "birthday":"出生日期",
    "education":"学历",
    "ctvc":"主体的职业类别",
    "picm":"个人年收入",
    "ficm":"家庭年收入",
    "marriage":"婚姻状况",
    "ceml":"电子邮件",
    "rgdt":"开户日期",
    "cls_dt":"销户日期",
    "remark":"备注",
    "indu_code":"行业代码",
    "stat_flag_ori":"客户状态原值",
    "stat_flag":"客户状态",
    "mer_prov":"省",
    "mer_city":"市",
    "mer_area":"区县",
    "address":"详细地址",
    "tel":"联系电话",
    "mer_unit":"管理机构",
    "is_line":"是否线上{注册}",
    "certification ":"建立渠道",
    "cer_num":"通过身份验证渠道数量",
    "con_acc_name":"经营名称",
    "bord_flag":"境内外标识",
    "web_info":"网络支付商户网址信息",
    "con_nation":"商户所属国家或地区",
    "bind_card":"银行绑定标识",
    "ip_code":"注册地IP地址",
    "mac_info":"注册设备MAC或IMEI地址",
    "self_acc_no":"特约商户收单结算账号",
    "acc_type1":"账户类型",
    "bank_acc_name":"银行账户名称",
    "reals":"客户真实有效性",
    "batch_pay":"批量代付标识",
    "statement_type":"结算类型"
    :return:
    """
    busi_reg_no = "per_{}_{}".format(num1, num2)
    ctnm = make_name_data()
    # cten = word_to_pinyin(ctnm)
    client_tp = random.choice(["1", "2"])
    busi_type = make_busi_type_data()
    account_tp = make_account_tp_data(busi_type)
    if client_tp == "2":
        smid = random.randint(1000, 9999)  # 该字段值待确定
        smid = str(smid)
    else:
        smid = ""
    # citp = make_citp_data()
    # citp_ori = citp  # 该值暂定
    # citp_nt = "有效证件"
    # ctid = make_ctid_data()
    # ctid_edt = make_Card_valid_date(ctid)
    sex = random.choice(['0','1'])
    country = choice_contry()
    nation = str(random.randint(1, 57))
    birthday = make_birthday_data()
    education = str(random.randint(1, 7))
    ctvc = random.choice(["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H"])
    # picm = "300000"
    # ficm = "500000"
    marriage = make_marriage_data(birthday)
    ceml = make_email_data()
    rgdt = make_register_date()
    cls_dt = make_cls_dt_data(busi_reg_no)
    remark = "这是一个备注"
    indu_code = make_indu_code_data()
    # stat_flag_ori = "888888"
    stat_flag = make_stat_flag_data(cls_dt)
    # mer_prov = get_province_data(ctid[:6])
    mer_area = make_province_code_data()
    mer_prov = get_province_code(mer_area)
    # mer_city = make_province_city_data(ctid[:6])[0]
    # mer_city = make_province_city_code_data(ctid[:6])
    # mer_area = make_province_city_data(ctid[:6])[-1]
    # address = make_address(ctid[:6])
    # tel = make_tel_num()
    mer_unit = make_mer_unit_data()
    is_line = random.choice(["0", "1"])
    # certification = random.choice(["1", "2", "3"])
    # cer_num = str(random.randint(0, 6))
    # con_acc_name = "默认经营名称"  # 网络支付、预付卡、银行卡收单必须填写,暂为空
    # bord_flag = make_bord_flag_data()
    # web_info = make_web_info_data(busi_type)  # 非网络支付业务，无网址用户可不填
    # con_nation = make_con_nation_data(bord_flag)
    # bind_card = make_bind_card_data(busi_type)  # 仅需网络支付填写
    # ip_code = make_ip_data(busi_type)  # 仅需网络支付填写
    # mac_info = make_mac_info_data(busi_type)  # PC机填写MAC，移动终端填写IMEI(需网络支付，预付卡填写), 暂为空
    # self_acc_no = make_self_acc_no_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    # acc_type1 = make_acc_type1_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    # bank_acc_name = make_bank_acc_name_data(acc_type1)
    # reals = make_reals_data()
    # batch_pay = make_batch_pay_data(busi_type, client_tp)
    # statement_type = make_statement_type_data(client_tp)

    # print(client_tp, account_tp, busi_type, busi_reg_no, ctnm, smid, education,
    #       marriage, ceml, ctvc, rgdt, cls_dt, country, nation, sex, birthday, remark, indu_code,
    #       stat_flag, mer_prov,  mer_area,  mer_unit, is_line)

    contect_data = make_connect_data([
        client_tp, account_tp, busi_type, busi_reg_no, ctnm, smid, education,
        marriage, ceml, ctvc, rgdt, cls_dt, country, nation, sex, birthday, remark, indu_code,
        stat_flag, mer_prov, mer_area, mer_unit, is_line
    ])
    return {
            "client_tp": client_tp,
            "account_tp": account_tp,
            "busi_type": busi_type,
            "busi_reg_no": busi_reg_no,
            "ctnm": ctnm,
            "smid": smid,
            "education": education,
            "marriage": marriage,
            "ceml": ceml,
            "ctvc": ctvc,
            "rgdt": rgdt,
            "cls_dt": cls_dt,
            "country": country,
            "nation": nation,
            "sex": sex,
            "birthday": birthday,
            "remark": remark,
            "indu_code": indu_code,
            "stat_flag": stat_flag,
            "mer_prov": mer_prov,
            "mer_area": mer_area,
            "mer_unit": mer_unit,
            "is_line": is_line
           }, contect_data


# 生成机构表
def make_stan_org(num1, num2):
    """
    busi_reg_no: 客户号
    ctnm: 客户名称
    cten: 拼音/英文名称
    client_tp: 客户类别
    account_tp: 账户分类
    busi_type: 业务类型
    smid: 主体特约商户编号
    citp: 证件类型_报送
    citp_ori: 证件类型原值
    ctid: 证件号码
    ctid_edt: 证件有效期
    citp_nt: 证件类型说明
    id_type: 证件类型_现场检查
    org_no: 组织机构代码
    linkman: 联系人姓名
    linktel: 联系人手机号
    linkjob: 联系人职务
    linkmail: 联系人邮箱
    linkphone: 联系人固定电话
    ceml: 电子邮件
    ctvc: 主体的行业类别
    crnm: 主体的法定代表人姓名
    crit: 主体的法定代表人身份证件类型
    crit_ori: 主体的法定代表人身份证件类型原值
    crit_nt: 主体的法定代表人身份证件类型说明
    crid: 主体的法定代表人身份证件号码
    crid_edt: 主体的法定代表人证件有效期
    rgdt: 开户日期
    cls_dt: 销户日期
    scale: 企业规模
    country: 注册国家
    crp_type: 组织机构类别
    fud_date: 成立日期
    reg_cptl: 注册资本
    remark_ctvc: 经营范围
    agency_ctnm: 代办理人姓名
    agency_citp: 代办理人证件类型
    agency_ctid: 代办理人证件号码
    agency_edt: 代办理人证件有效期限
    remark: 备注
    indu_code: 行业代码
    stat_flag_ori: 客户状态原值
    stat_flag: 客户状态
    mer_prov: 省
    mer_city: 市
    mer_area: 区县
    address: 详细地址
    tel: 联系电话
    mer_unit: 管理机构
    is_line: 是否线上
    certification : 建立渠道
    cer_num: 通过身份验证渠道数量
    con_acc_name: 经营名称
    bord_flag: 境内外标识
    web_info: 网络支付商户网址信息
    con_nation: 商户所属国家或地区
    majority_shareholder_ctnm: 控股股东或实际控制人姓名
    majority_shareholder_citp: 控股股东或实际控制人证件类型
    majority_shareholder_citp_ori: 控股股东或实际控制人证件类型原值
    majority_shareholder_ctid: 控股股东或实际控制人证件号码
    majority_shareholder_edt: 控股股东或实际控制人证件有效期限
    reg_cptl_code: 注册资本金币种
    bind_card: 银行绑定标识
    ip_code: 注册地IP地址
    mac_info: 注册设备MAC或IMEI地址
    self_acc_no: 特约商户收单结算账号
    acc_type1: 账户类型
    bank_acc_name: 银行账户名称
    reals: 客户真实有效性
    complex: 非自然人结构复杂度
    clear: 非自然人股权可辨识度
    batch_pay: 批量代付标识
    statement_type: 结算类型
    :return:
    """
    busi_reg_no = "org_{}_{}".format(num1, num2)
    ctnm = make_name_data()
    # cten = word_to_pinyin(ctnm)
    client_tp = random.choice(["1", "2"])
    busi_type = make_busi_type_data()
    account_tp = make_account_tp_data(busi_type)
    if client_tp == "2":
        smid = make_random_str(20)  # 该字段值待确定
    else:
        smid = ""
    # citp = random.choice(["21", "29"])
    # citp_ori = citp  # 该值暂定
    # ctid = make_ctid_data()
    # ctid_edt = make_Card_valid_date(ctid)
    # if citp == "29":
    #     citp_nt = random.choice(["营业执照", "统一社会信用代码"])
    # else:
    #     citp_nt = "证件类型"
    #
    # if citp_ori == "营业执照":
    #     id_type = "11"
    # else:
    #     id_type = "12"

    # org_no = make_random_num(9)  # 统一社会信用代码9-17位
    linkman = make_name_data()
    linktel = make_tel_num()
    linkjob = "联系人职务"
    linkmail = make_email_data()
    linkphone = make_random_num(9)
    ceml = make_email_data()
    ctvc = make_org_ctvc_data()
    crnm = make_name_data()
    crit = make_citp_data()
    # crit_ori = "证件原值"
    if crit == "19":
        crit_nt = "证件类型说明"
    else:
        crit_nt = ""
    crid = make_ctid_data()
    crid_edt = make_Card_valid_date(crid)
    rgdt = make_register_date()
    cls_dt = make_cls_dt_data(busi_reg_no)
    scale = make_scale_data()
    country = make_country_data()
    crp_type = make_crp_type_data()
    fud_date = "20151111"  # 成立日期，暂时写死
    reg_cptl = "1000000.00"  # 注册资金，暂时写死
    remark_ctvc = "经营范围"
    agency_ctnm = make_name_data()
    agency_citp = make_citp_data()
    agency_ctid = make_ctid_data()
    agency_edt = make_Card_valid_date(agency_ctid)
    remark = "备注，暂时不填"
    indu_code = make_indu_code_data()  # 支付机构行业代码，暂时默认为11111
    # stat_flag_ori = "11111"  # 客户状态原值，可是用支付系统码表，根据客户业务系统修改
    stat_flag = make_stat_flag_data(busi_reg_no)
    mer_area = make_province_code_data()
    mer_prov = get_province_code(mer_area)
    # mer_city = make_province_city_code_data(ctid[:6])
    # address = make_address(ctid[:6])
    # tel = make_tel_num()
    mer_unit = make_mer_unit_data()
    is_line = random.choice(["0", "1"])
    # certification = random.choice(["1", "2", "3"])
    # cer_num = str(random.randint(0, 6))
    # con_acc_name = "默认经营名称"  # 网络支付、预付卡、银行卡收单必须填写,暂为空
    # bord_flag = make_bord_flag_data()  # 网络支付、预付卡、银行卡收单必须填写
    # web_info = make_web_info_data(busi_type)  # 非网络支付业务，无网址用户可不填
    # con_nation = make_con_nation_data(bord_flag)  # 网络支付、预付卡、银行卡收单必须填写
    # majority_shareholder_ctnm = make_name_data()
    # majority_shareholder_citp = make_citp_data()
    # majority_shareholder_citp_ori = "控股股东或实际控制人证件类型原值"
    # majority_shareholder_ctid = make_ctid_data()
    # majority_shareholder_edt = make_Card_valid_date(majority_shareholder_ctid)
    # reg_cptl_code = "CNY"
    # bind_card = make_bind_card_data(busi_type)  # 仅需网络支付填写
    # ip_code = make_ip_data(busi_type)  # 仅需网络支付填写
    # mac_info = make_mac_info_data(busi_type)  # PC机填写MAC，移动终端填写IMEI(需网络支付，预付卡填写), 暂为空
    # self_acc_no = make_self_acc_no_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    # acc_type1 = make_acc_type1_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    # bank_acc_name = make_bank_acc_name_data(acc_type1)  # 当acc_type1=12时填写，银行账号对应账户名称（ 网络支付、预付卡、银行卡收单均需填写）
    # reals = str(random.randint(1, 5))
    # complex = make_complex_data()
    # clear = make_clear_data()
    # batch_pay = make_batch_pay_data(busi_type, client_tp)
    # statement_type = random.choice(["0", "1"])

    # print(client_tp, account_tp, busi_type, busi_reg_no, ctnm, smid, linkman, linktel, linkjob, linkmail, linkphone, ceml, ctvc, crnm, crit, crit_nt, crid, crid_edt, rgdt, cls_dt, scale, country, crp_type, fud_date, reg_cptl, remark_ctvc, agency_ctnm, agency_citp, agency_ctid, agency_edt, remark, indu_code, stat_flag, mer_prov, mer_area, mer_unit, is_line)
    contect_data = make_connect_data([
        client_tp, account_tp, busi_type, busi_reg_no, ctnm, smid, linkman, linktel, linkjob, linkmail, linkphone, ceml, ctvc, crnm, crit, crit_nt, crid, crid_edt, rgdt, cls_dt, scale, country, crp_type, fud_date, reg_cptl, remark_ctvc, agency_ctnm, agency_citp, agency_ctid, agency_edt, remark, indu_code, stat_flag, mer_prov, mer_area, mer_unit, is_line
    ])

    return {
               "client_tp": client_tp,
               "account_tp": account_tp,
               "busi_type": busi_type,
               "busi_reg_no": busi_reg_no,
               "ctnm": ctnm,
               # "cten": cten,
               "smid": smid,
               # "citp": citp,
               # "citp_ori": citp_ori,
               # "ctid": ctid,
               # "ctid_edt": ctid_edt,
               # "citp_nt": citp_nt,
               # "id_type": id_type,
               # "org_no": org_no,
               "linkman": linkman,
               "linktel": linktel,
               "linkjob": linkjob,
               "linkmail": linkmail,
               "linkphone": linkphone,
               "ceml": ceml,
               "ctvc": ctvc,
               "crnm": crnm,
               "crit": crit,
               # "crit_ori": crit_ori,
               "crit_nt": crit_nt,
               "crid": crid,
               "crid_edt": crid_edt,
               "rgdt": rgdt,
               "cls_dt": cls_dt,
               "scale": scale,
               "country": country,
               "crp_type": crp_type,
               "fud_date": fud_date,
               "reg_cptl": reg_cptl,
               "remark_ctvc": remark_ctvc,
               "agency_ctnm": agency_ctnm,
               "agency_citp": agency_citp,
               "agency_ctid": agency_ctid,
               "agency_edt": agency_edt,
               "remark": remark,
               "indu_code": indu_code,
               # "stat_flag_ori": stat_flag_ori,
               "stat_flag": stat_flag,
               "mer_prov": mer_prov,
               # "mer_city": mer_city,
               "mer_area": mer_area,
               # "address": address,
               # "tel": tel,
               "mer_unit": mer_unit,
               "is_line": is_line,
               # "certification": certification,
               # "cer_num": cer_num,
               # "con_acc_name": con_acc_name,
               # "bord_flag": bord_flag,
               # "web_info": web_info,
               # "con_nation": con_nation,
               # "majority_shareholder_ctnm": majority_shareholder_ctnm,
               # "majority_shareholder_citp": majority_shareholder_citp,
               # "majority_shareholder_citp_ori": majority_shareholder_citp_ori,
               # "majority_shareholder_ctid": majority_shareholder_ctid,
               # "majority_shareholder_edt": majority_shareholder_edt,
               # "reg_cptl_code": reg_cptl_code,
               # "bind_card": bind_card,
               # "ip_code": ip_code,
               # "mac_info": mac_info,
               # "self_acc_no": self_acc_no,
               # "acc_type1": acc_type1,
               # "bank_acc_name": bank_acc_name,
               # "reals": reals,
               # "complex": complex,
               # "clear": clear,
               # "batch_pay": batch_pay,
               # "statement_type": statement_type
           }, contect_data


def make_stan_stif(infos, ctif_tp_num, stif_time, stan_bact=None):
    """
    ctif_id: 主体客户号
    ctif_tp: 主体类别
    client_tp: 客户类别
    smid: 主体特约商户编码
    ctnm: 主体姓名/名称
    citp: 主体身份证件/证明文件类型
    citp_ori: 主体身份证件/证明文件类型原值
    citp_nt: 主体身份证件/证明文件类型说明
    ctid: 主体身份证件/证明文件号码
    cbat: 主体的银行账号种类
    cbac: 主体的银行账号
    cabm: 主体银行账号的开户行名称
    ctat: 主体的交易账号种类
    ctac: 主体的交易账号
    cpin: 主体所在支付机构的名称
    cpba: 主体所在支付机构的银行账号
    cpbn: 主体所在支付机构的银行账号的开户行名称
    ctip: 主体的交易IP地址
    tstm: 交易时间
    cttp: 货币资金转移方式
    tsdr: 资金收付标志
    crpp: 资金用途
    crtp: 交易币种
    crat: 交易金额
    tcif_id: 交易对手ID
    tcnm: 交易对手姓名/名称
    tsmi: 交易对手特约商户编码
    tcit: 交易对手证件/证明文件类型
    tcit_ori: 交易对手证件/证明文件类型原值
    tcit_nt: 交易对手证件/证明文件类型说明
    tcid: 交易对手证件/证明文件号码
    tcat: 交易对手的银行账号种类
    tcba: 交易对手的银行账号
    tcbn: 交易对手银行账号的开户行名称
    tctt: 交易对手的交易账号种类
    tcta: 交易对手的交易账号
    tcpn: 交易对手所在支付机构的名称
    tcpa: 交易对手所在支付机构的银行账号
    tpbn: 交易对手所在支付机构银行账号的开户行名称
    tcip: 交易对手的交易IP地址
    tmnm: 交易商品名称
    bptc: 银行与支付机构之间的业务交易编码
    pmtc: 支付机构与商户之间的业务交易编码
    ticd: 业务标识号
    busi_type: 业务类型
    trans_type: 交易类型
    pos_dev_id: 交易终端号或IMEI号等设备标识
    trans_stat: 交易状态
    bank_stat: 银行状态
    mer_prov: 地区省
    mer_area: 地区县
    pos_prov: 交易省
    pos_area: 交易县
    mer_unit: 管理机构
    extend1: 转换标识
    iofg: 境内外标识
    trans_channel: 交易渠道
    ctmac: 交易发生的mac地址
    balance: 主体支付账户的余额
    acc_flag: 交易对方账户类型
    ctid_edt: 主体身份证件/证明文件有效期截止日
    tran_flag: 对手账号标识
    trans_order: 交易订单号
    trans_cst_type: 交易类型(客户定义)
    crat_u: 交易金额折合美元
    crat_c: 交易金额折合人民币
    trans_way: 交易方式
    agency_ctnm: 代办人姓名
    agency_citp: 代办人身份证件（证明文件）类型
    agency_ctid: 代办人身份证件（证明文件）号码
    agency_country: 代办人国籍
    :param infos:
    :return:
    """
    ctif_id = infos.get("busi_reg_no")
    ctif_tp = ctif_tp_num
    client_tp = infos.get("client_tp")
    smid = infos.get("smid")
    ctnm = infos.get("ctnm")
    citp = infos.get("citp")
    citp_ori = infos.get("citp_ori")
    citp_nt = infos.get("citp_nt")
    ctid = infos.get("ctid")
    # cbat = stan_bact.get("act_tp")
    # cbac = stan_bact.get("act_cd")
    # cabm = stan_bact.get("cabm")
    cbat = make_bank_act_tp_data(ctif_tp)
    cbac = "62" + make_random_num(17)
    cabm = make_cabm_data(make_province_code_data())
    busi_type = make_busi_type_data()
    ctat = make_ctat_data(busi_type)
    ctac = make_random_num(17)
    cpin = "默认机构名称"
    cpba = make_random_num(17)
    cpbn = make_cabm_data(make_province_code_data())
    ctip = make_ip_data(busi_type)
    tstm = stif_time
    cttp = make_cttp_data()
    tsdr = random.choice(["01", "02"])
    crpp = "资金用途"
    crtp = "CNY"
    crat = make_crat_data()
    tcif_id = make_tcif_id_data(busi_type)
    tcnm = make_name_data()
    tsmi = make_random_num(20)
    tcit = make_cert_type_data()
    tcit_ori = "证件原值，需提供支付系统码表？"
    tcit_nt = "证件类型说明"
    tcid = make_random_num(20)
    tcat = random.choice(["01", "02", "03"])
    tcba = make_random_num(19)
    tcbn = make_cabm_data(make_province_code_data())
    tctt = random.choice(["01", "02"])
    tcta = make_random_num(19)
    tcpn = "默认支付机构名称"
    tcpa = make_random_num(19)
    tpbn = make_cabm_data(make_province_code_data())
    tcip = make_ip_data(busi_type)
    tmnm = "默认商品名称"
    bptc = make_random_num(25)
    pmtc = make_random_num(25)
    ticd = make_ticd_data()
    trans_type = make_trans_type_data(busi_type)
    pos_dev_id = make_pos_dev_id_data(busi_type)
    trans_stat = "交易状态"  # 交易状态，需提供支付系统码表
    bank_stat = "银行状态"  # 银行状态，需提供支付系统码表
    province_code = make_province_code_data()
    mer_prov = province_code
    mer_area = make_province_city_code_data(province_code)

    province_code2 = make_province_code_data()
    pos_prov = province_code2
    pos_area = make_province_city_code_data(province_code2)

    mer_unit = make_mer_unit_data()  # 需提供支付系统代码表
    extend1 = ""
    rate_rmb = ""   # 老接口字段
    rate_usa = ""  # 老接口字段
    iofg = "0"  # 暂时默认境内交易
    trans_channel = make_trans_channel_data()
    ctmac = make_mac_info_data(busi_type)
    balance = "10000"
    acc_flag = make_acc_flag_data(busi_type)
    ctid_edt = infos.get("ctid_edt")
    tran_flag = make_tran_flag_data(busi_type)
    trans_order = make_trans_order_data(busi_type)
    trans_cst_type = make_trans_cst_type_data()


    # print(ctif_id,ctif_tp,client_tp,smid,ctnm,citp,citp_ori,citp_nt,ctid,cbat,cbac,cabm,ctat,ctac,cpin,cpba,cpbn,ctip,tstm,cttp,tsdr,crpp,crtp,crat,tcif_id,tcnm,tsmi,tcit,tcit_ori,tcit_nt,tcid,tcat,tcba,tcbn,tctt,tcta,tcpn,tcpa,tpbn,tcip,tmnm,bptc,pmtc,ticd,busi_type,trans_type,pos_dev_id,trans_stat,bank_stat,mer_prov,mer_area,pos_prov,pos_area,mer_unit,extend1,rate_rmb,rate_usa,iofg,trans_channel,ctmac,balance,acc_flag,ctid_edt,tran_flag,trans_order,trans_cst_type)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, client_tp, smid, ctnm, citp, citp_ori, citp_nt, ctid, cbat, cbac, cabm, ctat, ctac, cpin,
        cpba, cpbn, ctip, tstm, cttp, tsdr, crpp, crtp, crat, tcif_id, tcnm, tsmi, tcit, tcit_ori, tcit_nt, tcid, tcat,
        tcba, tcbn, tctt, tcta, tcpn, tcpa, tpbn, tcip, tmnm, bptc, pmtc, ticd, busi_type, trans_type, pos_dev_id,
        trans_stat, bank_stat, mer_prov, mer_area, pos_prov, pos_area, mer_unit, extend1, rate_rmb, rate_usa, iofg,
        trans_channel, ctmac, balance, acc_flag, ctid_edt, tran_flag, trans_order, trans_cst_type
    ])
    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "client_tp": client_tp,
               "smid": smid,
               "ctnm": ctnm,
               "citp": citp,
               "citp_ori": citp_ori,
               "citp_nt": citp_nt,
               "ctid": ctid,
               "cbat": cbat,
               "cbac": cbac,
               "cabm": cabm,
               "ctat": ctat,
               "ctac": ctac,
               "cpin": cpin,
               "cpba": cpba,
               "cpbn": cpbn,
               "ctip": ctip,
               "tstm": tstm,
               "cttp": cttp,
               "tsdr": tsdr,
               "crpp": crpp,
               "crtp": crtp,
               "crat": crat,
               "tcif_id": tcif_id,
               "tcnm": tcnm,
               "tsmi": tsmi,
               "tcit": tcit,
               "tcit_ori": tcit_ori,
               "tcit_nt": tcit_nt,
               "tcid": tcid,
               "tcat": tcat,
               "tcba": tcba,
               "tcbn": tcbn,
               "tctt": tctt,
               "tcta": tcta,
               "tcpn": tcpn,
               "tcpa": tcpa,
               "tpbn": tpbn,
               "tcip": tcip,
               "tmnm": tmnm,
               "bptc": bptc,
               "pmtc": pmtc,
               "ticd": ticd,
               "busi_type": busi_type,
               "trans_type": trans_type,
               "pos_dev_id": pos_dev_id,
               "trans_stat": trans_stat,
               "bank_stat": bank_stat,
               "mer_prov": mer_prov,
               "mer_area": mer_area,
               "pos_prov": pos_prov,
               "pos_area": pos_area,
               "mer_unit": mer_unit,
               "extend1": extend1,
               "rate_rmb": rate_rmb,
               "rate_usa": rate_usa,
               "iofg": iofg,
               "trans_channel": trans_channel,
               "ctmac": ctmac,
               "balance": balance,
               "acc_flag": acc_flag,
               "ctid_edt": ctid_edt,
               "tran_flag": tran_flag,
               "trans_order": trans_order,
               "trans_cst_type": trans_cst_type
           }, contect_data




def write_to_csv(file_name, datas):
    path = os.getcwd()
    new_path = os.path.join(path, "3.2")
    if not os.path.exists(new_path):
        os.makedirs(new_path, exist_ok=False)

    t_stan_person_header = [u"client_tp（客户类别(1代表客户,2代表商户)）", u"account_tp（账户分类）", u"busi_type（业务类型）", u"busi_reg_no（客户号）", u"ctnm（主体名称）", u"smid（主体特约商户编号）", u"education（学历）", u"marriage（婚姻状况）", u"ceml（电子邮件）", u"ctvc（主体的行业类别）", u"rgdt（开户日期）", u"cls_dt（销户日期）", u"country（国籍）", u"nation（民族）", u"sex（性别）", u"birthday（出生日期）", u"remark", u"indu_code", u"stat_flag", u"mer_prov", u"mer_area", u"mer_unit", u"is_line"]
    t_stan_org_header = [u"client_tp(类别(1代表客户,2代表商户)", u"account_tp(账户分类)", u"busi_type(业务类型)", u"busi_reg_no(客户号)", u"ctnm(主体名称)", u"smid(主体特约商户编号)", u"linkman(联系人姓名)", u"linktel(联系人手机号)", u"linkjob(联系人职务)", u"linkmail(联系人邮箱)", u"linkphone(联系人固定电话)", u"ceml(电子邮件)", u"ctvc(主体的行业类别)", u"crnm(主体的法定代表人姓名)", u"crit(主体的法定代表人身份证件类型)", u"crit_nt(法人证件类型说明)", u"crid(主体的法定代表人身份证件号码)", u"crid_edt(法人证件有效期)", u"rgdt(开户日期)", u"cls_dt(销户日期)", u"scale(企业规模)", u"country(注册国家)", u"crp_type机构类别", u"fud_date", u"reg_cptl注册资本", u"remark_ctvc经营范围", u"agency_ctnm代办理人姓名", u"agency_citp代办理人证件类型", u"agency_ctid代办理人证件号码", u"agency_edt代办理人证件有效期限", u"remark", u"indu_code", u"stat_flag", u"mer_prov", u"mer_area", u"mer_unit", u"is_line"]
    t_stan_stif_header = ["CTIF_ID主体客户号", "CTIF_TP 1个人2 机构主体类别", "CLIENT_TP 1客户 2商户客户类别(1代表客户2代表商户)", "SMID主体特约商户编码(30)", "CTNM", "CITP主体身份证件/证明文件类型(2)", "citp_ori主体身份证件/证明文件类型原值", "CITP_NT主体身份证件/证明文件类型说明(32)", "CTID可疑主体身份证件/证明文件号码(32)", "CBAT交易主体的银行账号种类(2)", "CBAC交易主体的银行账号(64)", "CABM交易主体银行账号的开户行名称(128)", "CTAT主体的交易账号种类（2）", "CTAC主体的交易账号（64）", "CPIN主体所在支付机构的名称（128）", "CPBA主体所在支付机构的银行账号（64）", "CPBN主体所在支付机构的银行账号的开户行名称（128）", "CTIP主体的交易IP地址", "TSTM交易日期", "CTTP货币资金转移方式（4）", "TSDR资金收付标志", "CRPP资金用途（500）", "CRTP交易币种（3）", "CRAT交易金额（接口20）", "TCIF_ID交易对手ID（32）", "TCNM交易对手姓名/名称（128）", "TSMI交易对手特约商户编码（30）", "TCIT交易对手证件/证明文件类型（2）", "tcit_ori交易对手证件/证明文件类型原值", "TCIT_NT交易对手证件/证明文件类型说明（32）", "TCID交易对手证件/证明文件号码（32）", "TCAT交易对手的银行账号种类（）", "TCBA交易对手的银行账号（64）", "TCBN交易对手银行账号的开户行名称（128）", "TCTT交易对手的交易账号种类（2）", "TCTA交易对手的交易账号（64）", "TCPN交易对手所在支付机构的名称（128）", "TCPA交易对手所在支付机构的银行账号（64）", "TPBN交易对手所在支付机构银行账号的开户行名称（128）", "TCIP交易对手的交易IP地址（15）", "TMNM交易商品名称（64）", "BPTC银行与支付机构之间的业务交易编码（64）", "PMTC支付机构与商户之间的业务交易编码（64）", "ticd业务标识号（128）", "BUSI_TYPE", "trans_type", "pos_dev_id", "trans_stat", "bank_stat", "mer_prov", "mer_area", "pos_prov", "pos_area", "mer_unit", "extend1转换标识", "rate_rmb 人民币汇率", "rate_usa 美元汇率", "iofg 境内外标识", "trans_channel交易渠道", "ctmac交易主体发生的mac地址(32)", "balance账户余额", "acc_flag交易对方账户类型", "ctid_edt主体身份证件/证明文件有效期截止日", "tran_flag对手账号标识", "trans_order交易订单号", "trans_cst_type交易类型(客户定义)"]
    file_path = os.path.join(new_path, file_name)
    if not os.path.exists(file_path):
        head = os.path.split(file_name)[-1]
        head = head.split(".")[0]
        head = "t_stan_"+ head.split("_")[0] + "_header"
        head = "&#@".join([str(elem) for elem in eval(head)])
        # print(head)

        csvFile = open(file_path, "a", encoding="utf-8-sig", newline='')
        writer = csv.writer(csvFile)
        writer.writerows([[head], [datas]])
        csvFile.close()
    else:
        csvFile = open(file_path, "a", encoding="utf-8-sig", newline='')
        writer = csv.writer(csvFile)
        writer.writerows([datas])
        csvFile.close()



def person(num1):
    # print("个人")
    data_per = []
    for num2 in range(100):
        persion_infos, stan_person_connect = make_stan_person(num1, num2)
        data_per.append(stan_person_connect)
    file_name = "t_stan_person"
    file_name = file_name.split("_")[-1] + "_" + file_date_time
    write_to_csv(file_name + ".csv", data_per)


def org(num1):
    # print("机构")
    data_org = []
    for num2 in range(100):
        org_infos, stan_org_connect = make_stan_org(num1, num2)
        data_org.append(stan_org_connect)
        t_stan_stif, stan_stif_connect = make_stan_stif(org_infos, '2', file_date_time)
    file_name = "t_stan_org"
    file_name = file_name.split("_")[-1] + "_" + file_date_time
    write_to_csv(file_name + ".csv", data_org)


def main(begin, end):
    for num in range(begin, end):
        # person(num)
        org(num)


if __name__ == "__main__":
    file_date_time = "2019-02-16"
    start_time = time.time()
    main(0, 10)
    end_time = time.time()
    print(end_time - start_time)  # 13

