import csv
import random
from xpinyin import Pinyin
import unicodedata
import time
import xlrd
import json
import jieba
import os
from save_to_csv import write_to_csv


# from test_save import write_to_csv


def make_tel_data():
    num = 1
    while num < 100:
        ctif_id = "test_{}".format(num)
        ctif_tp = random.choice(["1", "2"])
        tel_tp = random.choice(["11", "12", "21", "22", "23"])
        tel = random.randint(13000000000, 19999999999)
        is_rp = random.choice(["1", "0"])
        tel_data = [ctif_id, ctif_tp, tel_tp, str(tel), is_rp]
        tel_data = "&#@".join(tel_data)
        num += 1
        yield tel_data


def write_to_tel():
    header = [u"ctif_id客户号", u"ctif_tp主体类型", u"tel_tp电话类型", "tel", "is_rp"]
    header = "&#@".join(header)
    tel_data = make_tel_data()
    csvFile = open("tel.csv", "w", encoding="utf-8-sig", newline='')
    writer = csv.writer(csvFile)
    writer.writerow([header])
    writer.writerows([[data] for data in tel_data])
    csvFile.close()


# write_to_tel()

def make_relation_data():
    num = 1
    while num < 100:
        ctif_id = "test_{}".format(num)
        ctif_tp = random.choice(["1", "2"])
        tel_tp = random.choice(["11", "12", "21", "22", "23"])
        tel = random.randint(13000000000, 19999999999)
        is_rp = random.choice(["1", "0"])
        tel_data = [ctif_id, ctif_tp, tel_tp, str(tel), is_rp]
        tel_data = "&#@".join(tel_data)
        num += 1
        yield tel_data


def write_to_relation():
    header = ["ctif_id客户号", "ctif_tp主体类型1个人 2机构", "rel_tp关系类型", "rel_layer关系人层级",
              "rel_ctif关系人客户号", "rel_cstp关系人类别 1个人 2机构", "rel_name关系人姓名", "rcnt关系人国籍/国家",
              "citp证件类型", "citp_ori关系人证件类型原值", "ctid证件号码", "citp_nt证件类型说明", "hold_per持股比例(5)",
              "hold_amt持股金额", "ctid_edt证件有效期", "rel_prov关系人省", "rel_city关系人市", "rel_area关系人区县",
              "rear关系人详细地址", "retl关系人联系电话"]
    header = "&#@".join(header)
    tel_data = make_tel_data()
    csvFile = open("relation.csv", "w", encoding="utf-8-sig", newline='')
    writer = csv.writer(csvFile)
    writer.writerow([header])
    writer.writerows([[data] for data in tel_data])
    csvFile.close()


# 拼接数据
def make_connect_data(one_data):
    """
    接收数据，使用特定的字符拼接，返回拼接好的数据
    :param one_data:
    :return:
    """
    data = "&#@".join([str(elem) for elem in one_data])
    return data


# write_to_relation()

# -------------------------分界线----------------------------

# def read_province_data():
#     """
#     读取、处理源数据文件，生成省市区代码，保存到新文件，运行一次即可注释掉，使用新文件获取数据
#     :return:
#     """
#     with open("province_code.txt", 'r', encoding="utf-8") as f:
#         res = f.read()
#
#     # print(len(res), res, type(res))
#     res_list = res.split(",")
#
#     # 处理数据
#     extent_data = []
#     # print(len(res_list))
#     for elem in res_list:
#         if elem[2:] == "0000" and elem not in ["710000", "810000", "820000"]:
#             res_list.remove(elem)
#         elif elem[-2:] == "00" and elem[:2] not in ["11", "12", "31", "50", "71", "81", "82"]:
#             res_list.remove(elem)
#
#     # print(len(res_list))
#
#     for x in res_list:
#         with open("province_code1.txt", 'w', encoding="utf-8") as f:
#             f.write(x + ',')
#     # print(len(res_list))
#     return random.choice(res_list)

# 生成省市区代码
def make_province_code_data():
    """
    读取处理好的数据文件
    :return:区域代码
    """
    with open("province_code1.txt", 'r', encoding="utf-8") as f:
        res = f.read()
    res_list = res.split(",")
    data = random.choice(res_list)
    while data in ["130100", "140100", "150100", "210100", "220100", "230100", "320100", "330100", "340100", "350100",
                   "370100", "410100", "420100", "430100", "440100", "442000", "450100", "460100", "500300", "510100",
                   "520100", "530100", "540100", "610100", "620100", "630100", "640100", "650100"]:
        data = random.choice(res_list)
    return data


# 生成省市区地址
# def read_excel():
#     """
#     从源文件中读取省市代码表，提取省市县二级地址，写入新文件，并且根据传入字符串参数code，返回对应的地址，
#     第一次运行，后续可从新文件中读取
#     :return:
#     """
#     booksheet = xlrd.open_workbook(r'省市号码表.xlsx')
#     ret1 = booksheet.sheets()[0]
#     # ret2 = booksheet.sheet_by_index(0)  # 按索引找sheet
#     row_num = ret1.nrows
#     # print(row_num)
#     data_dict = {}
#     # 指定分词缓存路径及文件名
#     path = os.getcwd()
#     jieba.dt.tmp_dir = path
#     jieba.dt.cache_file = "jieba.cache"
#     jieba.load_userdict("userdict.txt")
#     jieba.suggest_freq(('上海市', '浦东新区'), True)
#     for num in range(1, row_num):
#         row_data = ret1.row_values(num)
#         # print(row_data[0], type(row_data[0]),row_data[1], type(row_data[1]))
#         elem = str(int(row_data[0]))
#         # print(elem,type(elem))
#         if elem[2:] == "0000" and elem not in ["710000", "810000", "820000"]:
#             # print(elem)
#             continue
#         elif elem[-2:] == "00" and elem[:2] not in ["11", "12", "31", "50", "71", "81", "82"]:
#             # print(elem)
#             continue
#         else:
#             data_list = [data for data in jieba.cut(row_data[1], cut_all=False)]
#             data_dict[elem] = data_list
#             print(data_list)
#     # print(len(data_dict), data_dict)
#     with open("data2.txt", "w", encoding="utf-8") as f:
#         f.write(json.dumps(data_dict, ensure_ascii=False))
#
#     # return data_dict.get(code, "空")

# 提取省码表，写入文件
# def write_province_data():
#     """
#     提取省码表，写入文件,一次性函数
#     :return:
#     """
#     booksheet = xlrd.open_workbook(r'省市号码表.xlsx')
#     ret1 = booksheet.sheets()[0]
#     # ret2 = booksheet.sheet_by_index(0)  # 按索引找sheet
#     row_num = ret1.nrows
#     # print(row_num)
#     data_dict = {}
#
#     for num in range(1, row_num):
#         row_data = ret1.row_values(num)
#         # print(row_data[0], type(row_data[0]),row_data[1], type(row_data[1]))
#         elem = str(int(row_data[0]))
#         # print(elem,type(elem))
#         if elem[2:] == "0000":
#             print(elem)
#             data_dict[elem] = row_data[1]
#
#         # elif elem[-2:] == "00" and elem[:2] not in ["11", "12", "31", "50", "71", "81", "82"]:
#         #     # print(elem)
#         #     continue
#         else:
#             continue
#     # print(len(data_dict), data_dict)
#     with open("province_data.txt", "w", encoding="utf-8") as f:
#         f.write(json.dumps(data_dict, ensure_ascii=False))
#
#     # return data_dict.get(code, "空")


# 返回省名数据
def get_province_data(code):
    """
    根据省市代码的前2位，后4位默认全为0，获取省级名称
    :param code: 2位字符串（数字)
    :return: 省名
    """
    with open("province_data.txt", "r", encoding="utf-8") as f:
        province_data = f.read()
    province_data = json.loads(province_data)
    return province_data.get(code[:2] + "0000")


# 市县地址数据
def make_province_city_data(code):
    """
    获取省市县地址
    :param code: 省市县代码，字符串格式
    :return: 返回对应的市、县拆分的中文列表
    """
    with open("data2.txt", 'r', encoding="utf-8") as f:
        file = f.read()
    file = json.loads(file)
    data = file.get(code, ["无地址", "无地址"])
    return data


# 市县数据
def make_province_city_process_data(code):
    """
    中间处理函数，插入省，拼接省市县,
    :param code:
    :return:
    """
    # print(code)
    province = get_province_data(code[:2])
    # print(province)
    data = make_province_city_data(code)
    # print("2", data)
    # if not data:
    #     data = ["{}无市数据".format(code), "{}无县数据".format(code)]
    if not province:
        province = "无省数据"
    if province == data[0]:
        data = "".join(data)
    else:
        data.insert(0, province)
        data = "".join(data)
    return data


# # 返回县数据
# def make_province_data(data):
#     """
#     根据传入县市名，使用分词工具分词，提取最后一级
#     :param data:
#     :return: 县级市或区
#     """
#     cut_data = jieba.cut(data, cut_all=False)
#     data_list = [word for word in cut_data]
#     # print(data_list)
#     return data_list[-1]


# 生成证件类型数据
def make_cert_type_data():
    return random.choice([
        "11",  # 居民身份证或临时身份证
        "12",  # 军人或武警身份证件
        "13",  # 港澳台通行证
        "14",  # 外国公民护照
        "19",  # 其他个人有效证件(需进一步说明)
        "21",  # 组织机构代码
        "29"  # 其他机构代码(需进一步说明)
    ])


# 生成姓名拼音数据
def word_to_pinyin(word):
    """
    中文姓名转换为拼音
    :param word: 中文姓名
    :return: 中文全拼
    """
    if word:
        word_pinyin = Pinyin()
        result = word_pinyin.get_pinyin(u"{}".format(word), tone_marks='marks')
        # 去除声调
        res = unicodedata.normalize('NFKD', result).encode('ascii', 'ignore')
        res = res.decode()
        res = res.replace("-", "")  # 去除连接符
        return res
    else:
        raise ValueError("姓名为空，无法转换成拼音！")


# 身份证号数据
def make_IDCard():
    """
    # 生成身份证号，年龄范围，1940年至2003年出生的人，
    """
    area_extent = make_province_code_data()  # 地区号段
    age_extent = str(random.randint(1940, 2003))  # 年区间，
    month_extent = str(random.randint(1, 12))  # 月区间
    if eval(month_extent) < 10:
        month_extent = "0" + month_extent
    # 日区间，2月特殊处理，计28天，其他自然月按30天
    if month_extent == "2":
        day_extent = str(random.randint(1, 28))
    else:
        day_extent = str(random.randint(1, 30))
    if eval(day_extent) < 10:
        day_extent = "0" + day_extent
    # 4位尾号
    tail_extent = str(random.randint(1, 9999))
    if len(tail_extent) < 4:
        tail_extent = (4 - len(tail_extent)) * "0" + tail_extent

    return "".join([area_extent, age_extent, month_extent, day_extent, tail_extent])


# 生成随机数
def make_random_num(num):
    """ 接收int类型参数num，根据参数随机生成数字,返回字符串"""
    res_list = []
    while len(res_list) < num:
        elem = random.randint(0, 9)
        if res_list or elem:
            res_list.append(str(elem))

    return "".join(res_list)


# 身份证有效期数据
def make_Card_valid_date(IDCard):
    """生成身份证有效期数据，1965年以后出生的身份证有效期,在今年的基础上随机增加/减少年数，80年之前的，有效期长期"""
    if int(IDCard[6:10]) > 1965:
        date = random.choice(["-2", "-1", "0", "1", "3", "5", "10", "15", "20"])
        year = time.strftime("%Y", time.localtime())
        born_month_day = IDCard[10:14]  # 拼接月、日
        born_year = str(int(year) + int(date))
        return born_year + born_month_day
    else:
        return "99991231"


# 性别数据
def make_sex(IDCard):
    """根据身份证号区分性别,性别号码为0时，设置性别未知、保密"""
    code = int(IDCard[17:18])
    if code == 0:
        return "0"  # 未知/保密
    elif code % 2 == 0:
        return "1"  # 男
    else:
        return "2"  # 女


# 国家数据
def choice_contry():
    """
    国家，暂时默认为中国
    :return:
    """
    # country = [
    #     "CHN", "ALB", "DZA", "AFG", "ARG", "ARE", "ABW", "OMN", "AZE", "EGY", "ETH", "IRL", "EST", "AND", "AGO", "AIA",
    #     "ATG", "AUT", "ALA", "AUS", "MAC", "BRB", "PNG", "BHS", "PAK", "PRY", "PSE", "BHR", "PAN", "BRA", "BLR", "BMU",
    #     "BGR", "MNP", "BEN", "BEL", "ISL", "PRI", "BIH", "POL", "BOL", "BLZ", "BWA", "BTN", "BFA", "BDI", "BVT", "PRK",
    #     "GNQ", "DNK", "DEU", "TLS", "TGO", "DOM", "DMA", "RUS", "ECU", "ERI", "FRA", "FRO", "PYF", "GUF", "ATF", "MAF",
    #     "VAT", "PHL", "FJI", "FIN", "CPV", "GMB", "COG", "COD", "COL", "CRI", "GRD", "GRL", "GEO", "GGY", "CUB", "GLP",
    #     "GUM", "GUY", "KAZ", "HTI", "KOR", "NLD", "BES", "SXM", "HMD", "MNE", "HND", "KIR", "DJI", "KGZ", "GIN", "GNB",
    #     "CAN", "GHA", "GAB", "KHM", "CZE", "ZWE", "CMR", "QAT", "CYM", "CCK", "COM", "CIV", "KWT", "HRV", "KEN", "COK",
    #     "CUW", "LVA", "LSO", "LAO", "LBN", "LTU", "LBR", "LBY", "LIE", "REU", "LUX", "RWA", "ROU", "MDG", "IMN", "MDV",
    #     "FLK", "MLT", "MWI", "MYS", "MLI", "MKD", "MHL", "MTQ", "MYT", "MUS", "MRT", "USA", "UMI", "ASM", "VIR", "MNG",
    #     "MSR", "BGD", "PER", "FSM", "MMR", "MDA", "MAR", "MCO", "MOZ", "MEX", "NKR", "NAM", "ZAF", "ATA", "SGS", "SSD",
    #     "NRU", "NPL", "NIC", "NER", "NGA", "NIU", "NOR", "NFK", "PLW", "PCN", "PRT", "JPN", "SWE", "CHE", "SLV", "WSM",
    #     "SRB", "SLE", "SEN", "CYP", "SYC", "SAU", "BLM", "CXR", "STP", "SHN", "KNA", "LCA", "SMR", "SPM", "VCT", "LKA",
    #     "SVK", "SVN", "SJM", "SWZ", "SDN", "SUR", "SLB", "SOM", "TJK", "THA", "TZA", "TON", "TCA", "TTO", "TUN", "TUV",
    #     "TUR", "TKM", "TKL", "WLF", "VUT", "GTM", "VEN", "BRN", "UGA", "UKR", "URY", "UZB", "ESP", "ESH", "GRC", "HKG",
    #     "SGP", "NCL", "NZL", "HUN", "SYR", "JAM", "ARM", "YEM", "IRQ", "IRN", "ISR", "ITA", "IND", "IDN", "GBR", "VGB",
    #     "IOT", "JOR", "VNM", "ZMB", "JEY", "TCD", "GIB", "CHL", "CAF", "TWN"
    #     ]
    country = "CHN"
    return country


# 客户状态数据
def make_stat_flag_data(name):
    """
    # n-正常， c-关闭
    :return:
    """
    num = name.split("_")
    if num[-1] == "1":
        stat_flag = "c"
    else:
        stat_flag = "n"
    return stat_flag


# 开户日期数据
def make_register_date():
    """
    生成开户日期,日期范围，本年本月本日起至前推20年之间，
    :return:
    """
    year_now = eval(time.strftime("%Y", time.localtime()))
    num = random.randint(0, 20)
    year = year_now - num
    month_now = int(time.strftime("%m", time.localtime()))
    if year == year_now:
        month = random.randint(1, month_now)
    else:
        month = random.randint(1, 12)
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)
    day_now = int(time.strftime("%d", time.localtime()))
    if month == "02":
        if year == year_now and int(month) == month_now:
            day = str(random.randint(1, day_now))
        else:
            day = str(random.randint(1, 28))
    else:
        if year == year_now and int(month) == month_now:
            day = str(random.randint(1, day_now))
        else:
            day = str(random.randint(1, 30))
    if eval(day) < 10:
        day = "0" + day

    return str(year) + month + day


# 地址数据
def make_address(code):
    """

    :param code: 省市区代码
    :return: 详细地址
    """
    three_level_addr = make_province_city_process_data(code)
    street_address = random.choice([
        "解放路", "千佛山", "趵突泉", "泉城路", "大明湖", "东关", "文东", "建新", "甸柳", "燕山", "姚家", "龙洞", "智远", "舜华路", "大观园", "杆石桥", "四里村",
        "魏家庄", "二七", "七里山", "六里山", "舜玉路", "泺源", "王官庄", "舜耕", "白马山", "七贤", "十六里河", "兴隆", "党家", "陡沟", "振兴街", "中大槐树",
        "道德街", "西市场", "五里沟", "营市街", "青年公园", "南辛庄", "段店北路", "张庄路", "匡山", "美里湖", "吴家堡", "腊山", "兴福", "玉清湖", "无影山", "天桥东街",
        "北村", "南村", "堤口路", "北坦", "制锦市", "宝华", "官扎营", "纬北路", "药山", "北园", "泺口", "桑梓店", "大桥", "山大路", "洪家楼", "东风", "全福",
        "孙村", "巨野河", "华山", "荷花路", "王舍人", "鲍山", "郭店", "唐冶", "港沟", "遥墙", "临港", "仲宫", "柳埠", "董家", "彩石", "文昌", "崮云湖", "平安",
        "五峰山", "归德", "万德", "张夏", "明水", "双山", "圣井", "埠村", "枣园", "龙山", "普集", "官庄", "相公庄", "绣惠", "文祖", "曹范", "白云湖", "高官寨",
        "宁家埠", "济阳", "济北", "回河", "孙耿", "崔寨", "太平", "榆山", "锦水"
    ])
    areas_name = random.choice([
        "万豪国际公寓", "晓月苑", "永定路商住中心", "橙色年代", "嘉慧苑", "致雅居", "彩虹城", "松园小区", "燕归园", "北京青年城", "金宝纯别墅", "翌景嘉园", "涧桥·泊屋馆",
        "京东丽景", "旭风苑公寓", "朝阳无限", "庄胜二期", "潇雅居", "GOGO新世代", "飞腾家园", "英嘉公寓", "高第", "金榜园", "迎曦园", "风格与林", "太阳国际公馆(瑞景嘉园)",
        "永合馨苑", "澳洲新星", "丰润世家", "洋桥花园", "长安新城", "金隅丽港城", "兴涛社区", "糖人街", "时代芳群", "运河园", "浉城百郦", "测试项目", "新洲商务大厦", "加来小镇",
        "新新公寓", "颍泽洲", "城市印象", "上河美墅", "同泰苑", "和枫雅居", "建兴家园", "昊腾花园", "高苑·花样年华", "金码大厦", "天辉公寓", "NOLITA那里", "政馨家园",
        "文林商苑", "蝶翠华庭", "晋元庄小区", "幸福源", "当代城市家园", "非常生活", "祥瑞苑", "雪梨澳乡", "清欣园", "晟丰阁", "倚林佳园", "华龙小区", "秀安园", "新华联锦园",
        "乐澜宝邸", "棉花城", "CLASS", "金宸公寓", "燕景佳园", "珠江帝景", "龙山新新小镇", "万景公寓", "飘HOME", "蓝堡", "新纪元公寓", "中信红树湾", "海德堡花园",
        "天缘公寓", "长城盛世mm", "鲁艺上河村", "瑞馨公寓", "鼎诚国际MM", "德胜世嘉", "榆园新居", "远洋天地", "星河城", "黎明新座", "世纪城", "大观园中华商住区", "中国第一商城",
        "后现代城", "中海凯旋", "新都丽苑", "陶然北岸", "观河锦苑", "星光公寓", "观筑", "绿城星洲花园", "御鹿家园", "都市心海岸", "山水汇豪", "漪内轩", "颐园(碧水云天)",
        "新荣家园", "双桥温泉北里住宅", "恬心家园", "正邦嘉园", "依翠园", "万科西山庭院", "新御景", "天行建商务大厦", "浉城百丽", "华腾园", "同仁园", "格林小镇",
        "东华经典(东华金座)", "俊景苑", "朗琴园", "快乐洋城", "新中环公寓", "非常宿舍", "清城名苑", "兴都苑(水榭楼台)", "雍景台", "风林绿洲(奕翠庭)", "团结公寓"
    ])
    building_name = str(random.randint(1, 50))
    unit_num = str(random.randint(1, 9))
    floor_num = str(random.randint(1, 30))
    room_num = str(random.randint(1, 4))
    return three_level_addr + street_address + "街道" + areas_name + building_name + "楼" + unit_num + "单元" + floor_num + "层" + room_num + "号"


# 电话号码数据
def make_tel_num():
    """
    随机生成手机号码
    :return: 返回字符串类型
    """
    one_two = random.choice(["13", "14", "15", "16", "17", "18", "19"])

    three_nine = []
    for num in range(9):
        elem = random.randint(0, 9)
        three_nine.append(str(elem))

    return one_two + "".join(three_nine)


def make_random_str(num):
    str_col = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for elem in range(num):
        res += random.choice(str_col)
    return res


# 邮箱数据
def make_email_data():
    extend = random.choice(["163.com", "126.com", "gmail.com", "qq.com", "sina.com", "outlook.com"])
    name_1 = make_random_str(6)
    name_2 = make_random_num(6)
    return name_1 + "_" + name_2 + "@" + extend


# ip地址数据
def make_ip_data(busi_type):
    """
    生成ip数据，当支付类型为网络支付时，生成ip并返回，否则，返回空
    :param busi_type:
    :return:
    """
    if busi_type == "01":
        first = random.randint(1, 254)
        if first in [10, 127, 192, 172]:
            first += 1
        second = random.randint(0, 255)
        third = random.randint(0, 255)
        fouth = random.randint(1, 255)
        ip = ".".join([str(first), str(second), str(third), str(fouth)])
    else:
        ip = ''
    return ip

# 生成姓名数据
def make_name_data():
    first_name = random.choice([
        "赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨",
        "朱", "秦", "尤", "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜",
        "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏", "潘", "葛", "奚", "范", "彭", "郎",
        "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳", "酆", "鲍", "史", "唐",
        "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常",
        "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余", "元", "卜", "顾", "孟", "平", "黄",
        "和", "穆", "萧", "尹", "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米", "贝", "明", "臧",
        "计", "伏", "成", "戴", "谈", "宋", "茅", "庞", "熊", "纪", "舒", "屈", "项", "祝", "董", "梁",
        "杜", "阮", "蓝", "闵", "席", "季", "麻", "强", "贾", "路", "娄", "危", "江", "童", "颜", "郭",
        "梅", "盛", "林", "刁", "钟", "徐", "邱", "骆", "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍",
        "虞", "万", "支", "柯", "昝", "管", "卢", "莫", "经", "房", "裘", "缪", "干", "解", "应", "宗",
        "丁", "宣", "贲", "邓", "郁", "单", "杭", "洪", "包", "诸", "左", "石", "崔", "吉", "钮", "龚",
        "程", "嵇", "邢", "滑", "裴", "陆", "荣", "翁", "荀", "羊", "於", "惠", "甄", "曲", "家", "封",
        "芮", "羿", "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫", "乌", "焦", "巴", "弓"])
    second_name = random.choice([
        "一", "是", "我", "不", "在", "人", "们", "有", "来", "他", "这", "上", "着", "个", "地", "到",
        "大", "里", "说", "去", "子", "得", "也", "和", "那", "要", "下", "看", "天", "时", "过", "出",
        "小", "么", "起", "你", "都", "把", "好", "还", "多", "没", "为", "又", "可", "家", "学", "只",
        "以", "主", "会", "样", "年", "想", "能", "生", "同", "老", "中", "从", "自", "面", "前", "头",
        "到", "它", "后", "然", "走", "很", "像", "见", "两", "用", "国", "动", "进", "成", "回", "什",
        "边", "作", "对", "开", "而", "已", "些", "现", "山", "民", "候", "经", "发", "工", "向", "事",
        "命", "给", "长", "水", "义", "三", "声", "于", "高", "正", "手", "知", "理", "眼", "志", "点",
        "心", "战", "二", "问", "但", "身", "方", "实", "做", "叫", "当", "住", "听", "革", "打", "呢",
        "真", "党", "全", "才", "四", "已", "所", "敌", "之", "最", "光", "产", "情", "路", "分", "总",
        "条", "白", "话", "东", "席", "次", "亲", "如", "被", "花", "口", "放", "儿", "常", "西", "气",
        "五", "第", "使", "写", "军", "吧", "文", "运", "在", "果", "怎", "定", "许", "快", "明", "行",
        "因", "别", "飞", "外", "树", "物", "活", "部", "门", "无", "往", "船", "望", "新", "带", "队",
        "先", "力", "完", "间", "却", "站", "代", "员", "机", "更", "九", "每", "风", "级", "跟", "笑",
        "啊", "孩", "万", "少", "直", "意", "夜", "比", "阶", "连", "车", "重", "便", "斗", "马", "哪",
        "化", "太", "指", "变", "社", "似", "士", "者", "干", "石", "满", "决", "百", "原", "群",
        "究", "各", "六", "本", "思", "解", "立", "河", "爸", "村", "八", "难", "早", "论", "根",
        "共", "让", "相", "研", "今", "其", "书", "接", "应", "关", "信", "觉", "步", "反", "处",
        "记", "将", "千", "找", "争", "领", "或", "师", "结", "块", "跑", "谁", "草", "越", "字", "加",
        "紧", "爱", "等", "习", "阵", "月", "青", "半", "火", "法", "题", "建", "赶", "位",
        "唱", "海", "七", "任", "件", "感", "准", "张", "团", "屋", "离", "片", "科", "倒", "睛", "利",
        "世", "刚", "且", "由", "送", "切", "星", "晚", "表", "够", "整", "认", "响", "雪", "流", "未",
        "场", "该", "并", "底", "深", "刻", "平", "伟", "忙", "提", "确", "近", "亮", "轻", "讲", "农",
        "古", "黑", "告", "界", "拉", "名", "呀", "土", "清", "阳", "照", "办", "史", "改", "历", "转",
        "画", "造", "嘴", "此", "治", "北", "必", "服", "雨", "穿", "内", "识", "验", "传", "业", "菜", "兴"])
    last_name = random.choice([
        "命", "给", "长", "水", "义", "三", "声", "于", "高", "正", "手", "知", "理", "眼", "志", "点",
        "心", "战", "二", "问", "但", "身", "方", "实", "做", "叫", "当", "住", "听", "革", "打", "呢",
        "真", "党", "全", "才", "四", "已", "所", "敌", "之", "最", "光", "产", "情", "路", "分", "总",
        "条", "白", "话", "东", "席", "次", "亲", "如", "被", "花", "口", "放", "儿", "常", "西", "气",
        "五", "第", "使", "写", "军", "吧", "文", "运", "在", "果", "怎", "定", "许", "快", "明", "行",
        "因", "别", "飞", "外", "树", "物", "活", "部", "门", "无", "往", "船", "望", "新", "带", "队",
        "先", "力", "完", "间", "却", "站", "代", "员", "机", "更", "九", "每", "风", "级", "跟", "笑",
        "啊", "孩", "万", "少", "直", "意", "夜", "比", "阶", "连", "车", "重", "便", "斗", "马", "哪",
        "化", "太", "指", "变", "社", "似", "士", "者", "干", "石", "满", "决", "百", "原", "群",
        "究", "各", "六", "本", "思", "解", "立", "河", "爸", "村", "八", "难", "早", "论", "根",
        "共", "让", "相", "研", "今", "其", "书", "接", "应", "关", "信", "觉", "步", "反", "处",
        "记", "将", "千", "找", "争", "领", "或", "师", "结", "块", "跑", "谁", "草", "越", "字"])
    return first_name + second_name + last_name


# 支付账号数据
def make_act_cd_data(act_tp):
    # 互联网支付账号，虚拟账户号
    """
    生成支付账号
    :param act_tp: 账号类型
    :return: 随机账号
    """
    if act_tp == "11":
        act_cd = make_random_num(13)
    elif act_tp == "211":
        act_cd = make_random_num(19)
    elif act_tp == "212":
        act_cd = make_random_num(15)
    else:
        raise TypeError("act_tp类型错误！")
    return act_cd


# 账号等级数据
def make_act_type_data(act_tp):
    """
    随机生成账号等级，提高高级别账号权重
    :param act_tp: 账号类型
    :return: 随机账号类别，高级别账号权限较大
    """
    if act_tp == "11":
        act_typ = random.choice(["III", "III", "III", "II", "II", "I"])
    elif act_tp == "211":
        act_typ = random.choice(["I", "I", "I", "II", "II", "III"])
    elif act_tp == "212":
        act_typ = "I"
    else:
        raise TypeError("act_tp类型错误！")
    return act_typ


# 限额数据
def make_act_limit_data(act_tp, act_typ):
    """
    限额
    :param act_tp:
    :param act_typ:
    :return:
    """
    if act_tp == "11":
        if act_typ == "III":
            act_limit = float(100000)
        elif act_typ == "II":
            act_limit = float(10000)
        elif act_typ == "I":
            act_limit = float(1000)
        else:
            raise TypeError("act_tye类型错误！")
    elif act_tp == "211":
        if act_typ == "I":
            act_limit = float(100000)
        elif act_typ == "II":
            act_limit = float(10000)
        elif act_typ == "III":
            act_limit = float(1000)
        else:
            raise TypeError("act_tye类型错误！")
    elif act_tp == "212":
        act_limit = float(1000)
    else:
        raise TypeError("act_tp类型错误！")

    return act_limit


# 预付卡数据
def make_prepaid_card_data(infos):
    """
    如果业务类型为预付卡，生成预付卡数据，否则，置空
    :param infos: person/org表信息
    :return:预付卡数据
    """
    if infos.get("busi_type") == "03":
        sales_name = infos.get("ctnm")
        cst_sex = infos.get("sex", "0")
        nation = infos.get("country")
        occupation = "职业待定"  # 待定，是否有职业表
        id_type = infos.get("citp")
        id_type_ori = infos.get("citp_ori")
        id_no = infos.get("ctid")
        id_deadline = infos.get("ctid_edt")
        contact = infos.get("tel")
        address = infos.get("address")
        sales_flag = random.choice(["11", "12"])
    else:
        sales_name = ""
        cst_sex = ""
        nation = ""
        occupation = ""
        id_type = ""
        id_type_ori = ""
        id_no = ""
        id_deadline = ""
        contact = ""
        address = ""
        sales_flag = ""

    return sales_name, cst_sex, nation, occupation, id_type, id_type_ori, id_no, id_deadline, contact, address, sales_flag


# 互联网账号数据
def make_bind_mob_data(infos):
    """
    如果是互联网账号，返回手机号，否则，值为空
    :param infos:
    :return: bind_mob值
    """
    if infos.get("busi_type") == "01":
        bind_mob = infos.get("tel")
    else:
        bind_mob = ""
    return bind_mob


# 银行账号种类数据
def make_bank_act_tp_data(ctif_tp):
    """
    生成银行账号种类
    :param ctif_tp: 主体类型
    :return: 账号类型
    """
    if ctif_tp == "1":
        act_tp = random.choice(["02", "03"])
    elif ctif_tp == "2":
        act_tp = random.choice(["01", "03"])
    else:
        raise TypeError("ctif_tp类型错误！")

    return act_tp


# 开户行数据
def make_cabm_data(code):
    """
    根据身份证所属省市，随机生成开户行名称
    :param code: 身份证号前6位字符串
    :return: 开户行名称
    """
    province = make_province_city_process_data(code)
    street_address = random.choice([
        "解放路", "千佛山", "趵突泉", "泉城路", "大明湖", "东关", "文东", "建新", "甸柳", "燕山", "姚家", "龙洞", "智远", "舜华路", "大观园", "杆石桥", "四里村",
        "魏家庄", "二七", "七里山", "六里山", "舜玉路", "泺源", "王官庄", "舜耕", "白马山", "七贤", "十六里河", "兴隆", "党家", "陡沟", "振兴街", "中大槐树",
        "道德街", "西市场", "五里沟", "营市街", "青年公园", "南辛庄", "段店北路", "张庄路", "匡山", "美里湖", "吴家堡", "腊山", "兴福", "玉清湖", "无影山", "天桥东街",
        "北村", "南村", "堤口路", "北坦", "制锦市", "宝华", "官扎营", "纬北路", "药山", "北园", "泺口", "桑梓店", "大桥", "山大路", "洪家楼", "东风", "全福",
        "孙村", "巨野河", "华山", "荷花路", "王舍人", "鲍山", "郭店", "唐冶", "港沟", "遥墙", "临港", "仲宫", "柳埠", "董家", "彩石", "文昌", "崮云湖", "平安",
        "五峰山", "归德", "万德", "张夏", "明水", "双山", "圣井", "埠村", "枣园", "龙山", "普集", "官庄", "相公庄", "绣惠", "文祖", "曹范", "白云湖", "高官寨",
        "宁家埠", "济阳", "济北", "回河", "孙耿", "崔寨", "太平", "榆山", "锦水"
    ])
    bank_name = random.choice(["工商银行", "建设银行", "邮政储蓄银行", "招商银行", "光大银行", "农业银行", "中国银行", "浦发银行", "浙商银行"])
    return province + bank_name + street_address + "支行"


# 交易时间数据
def make_trade_time_data():
    # 全局变量，交易日期与文件名日期一致
    global file_date_time
    # trade_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    trade_year = time.strftime("%Y", time.localtime())
    trade_month = time.strftime("%m", time.localtime())
    trade_date = time.strftime("%d", time.localtime())
    trade_year = str(eval(trade_year))
    trade_month = str(eval(trade_month))
    trade_date = "16"  # 暂时默认为14号
    # trade_date = str(eval(trade_date)-11)
    file_date_time = "-".join([trade_year, trade_month, trade_date])
    trade_time = trade_year + trade_month + trade_date + "090000"
    # trade_time = trade_time.replace("25", "14")
    return trade_time


# 货币资金转移方式数据
def make_cttp_data():
    cttp = random.choice([
        "0000",  # 即向支付账户充值——通过银行账户
        "0001",  # 即向支付账户充值——通过仅限线上实名支付账户充值的预付卡
        "0100",  # 即互联网支付——付款方银行账户向收款方银行账户转出
        "0101",  # 即互联网支付——付款方银行账户向收款方支付账户转出
        "0102",  # 即互联网支付——付款方支付账户向收款方支付账户转出
        "0103",  # 即互联网支付——付款方支付账户向收款方银行账户转出
        "0200",  # 即移动电话支付、固定电话支付、数字电视支付——付款方银行账户向收款方银行账户转出
        "0201",  # 即移动电话支付、固定电话支付、数字电视支付——付款方银行账户向收款方支付账户转出
        "0202",  # 即移动电话支付、固定电话支付、数字电视支付——付款方支付账户向收款方支付账户转出
        "0203",  # 即移动电话支付、固定电话支付、数字电视支付——付款方支付账户向收款方银行账户转出
        "0300",  # 即从支付账户结算提款
        "0400",  # 即预付卡发行业务——现金购买
        "0401",  # 即预付卡发行业务——银行转账方式购买
        "0500",  # 即预付卡充值业务——通过现金充值
        "0501",  # 即预付卡充值业务——通过银行账户充值
        "0600",  # 即预付卡受理业务
        "0700",  # 即预付卡赎回业务——现金赎回
        "0701",  # 即预付卡赎回业务——银行转账方式赎回
        "0800"  # 即银行卡收单业务
    ])
    return cttp


# 交易金额数据
def make_trade_amount_data():
    """
    随机生成交易金额，保留2位小数
    :return:
    """
    amount_1 = random.randint(1, 10000000)
    amount_2 = random.randint(0, 100)
    return amount_1 + amount_2 / 100


# 行业类别数据(机构专用）
def make_org_ctvc_data():
    ctvc = random.choice([
        "2A",  # 农、林、牧、渔业
        "2B",  # 采矿业
        "2C",  # 制造业
        "2D",  # 电力、燃气及水的生产和供应业
        "2E",  # 建筑业
        "2F",  # 交通运输、仓储和邮政业
        "2G",  # 信息传输、计算机服务和软件业
        "2H",  # 批发和零售业
        "2I",  # 住宿和餐饮业
        "2J",  # 金融业
        "2K",  # 房地产业
        "2L",  # 租赁和商务服务业
        "2M",  # 科学研究、技术服务和地质勘查业
        "2N",  # 水利、环境和公共设施管理业
        "2O",  # 居民服务和其他服务业
        "2P",  # 教育
        "2Q",  # 卫生、社会保障和社会福利业
        "2R",  # 文化、体育和娱乐业
        "2S",  # 公共管理和社会组织
        "2T"  # 国际组织
    ])
    return ctvc


# 业务识别号数据
def make_ticd_data():
    """
    交易流水的唯一识别码，时间戳加地区代码
    :return:
    """
    timestmp = time.time()
    area_code = make_province_code_data()
    ticd = str(timestmp).replace(".", "") + area_code
    return ticd


# mac设备数据
def make_mac_info_data(busi_type):
    """银行卡收单不需要"""
    if busi_type == "02":
        mac_info = ""
    else:
        strs = make_random_str(10)
        nums = make_random_num(5)
        mac_info = strs + nums
    return mac_info


# 业务类型数据
def make_busi_type_data():
    busi_type = random.choice([
        "01",  # 互联网支付
        "02",  # 银行卡收单
        "03"  # 预付卡发行与受理
        # "04",  # 移动电话支付
        # "05",  # 固定电话支付
        # "06",  # 数字电视支付
        # "07"  # 货币汇兑
    ])
    return busi_type


# 交易类型数据
def make_trans_type_data(busi_type):
    """
    根据业务类型生成交易类型数据
    :param busi_type:
    :return:
    """
    if busi_type == "01":
        trans_type = random.choice([
            "A10",  # 消费收单
            "A11",  # 退货退款
            "A12",  # 提现
            "A13",  # 转账
            "A14",  # 充值
            "A15",  # 消费
            "A16",  # 其他
            "A17",  # 代收
            "A18",  # 代付
            "A19",  # 批量代付
            "A20",  # 条码消费
            "A21",  # 条码转账
            "A80",  # D0、T0消费收单
            "A90"  # D0、T0条码消费收单
        ])
    elif busi_type == "03":
        trans_type = random.choice([
            "B11",  # 购买
            "B12",  # 充值
            "B13",  # 赎回
            "B14"  # 消费
        ])
    elif busi_type == "02":
        trans_type = random.choice([
            "C11",  # 取现
            "C12",  # 预授权完成（请求）
            "C13",  # MOTO预授权完成（请求）
            "C14",  # 预授权完成（通知）
            "C15",  # MOTO预授权完成（通知）
            "C16",  # 手工预授权完成
            "C17",  # 手工MOTO预授权完成
            "C18",  # 消费
            "C19",  # 消费（分期付款）
            "C20",  # 消费（积分）
            "C21",  # MOTO消费
            "C22",  # MOTO退货
            "C23",  # 退货（联机）
            "C24",  # 存款（或存款确认）
            "C25",  # 余额查询
            "C26",  # 汇款（仅指汇款交易本身而不包括汇款验证交易）
            "C27",  # 手工汇款
            "C28",  # 磁条卡现金充值（充值确认）
            "C29",  # 脱机消费（仅受理方包含）
            "C30",  # 代收
            "C31",  # 代付（代付确认）
            "C32",  # 撤销
            "C33",  # 冲正
            "C90"  # D0、T0消费
        ])
    else:
        trans_type = random.choice([
            "D11",  # 委托付款
            "D12",  # 受益收款
            "D13",  # 委托转让
            "D14",  # 委托受让
            "D15",  # 委托赎回
            "D16",  # 运用拨款
            "D17",  # 运用收款
            "D18",  # 运用转让
            "D19"  # 提前还款
        ])

    return trans_type


# IMEI设备标识数据
def make_pos_dev_id_data(busi_type):
    """
    网络支付业务必须填，其他业务，应填
    :param busi_type:交易类型
    :return: IMEI数据
    """
    if busi_type == "01":
        pos_dev_id = make_random_num(10)
    else:
        pos_dev_id = random.choice([make_random_num(10), ""])

    return pos_dev_id


# 交易渠道数据
def make_trans_channel_data():
    """
    随机生成交易渠道
    :return:
    """
    trans_channel = random.choice([
        "01",  # 支付账户
        "02",  # 银行账户
        "03",  # 网关支付
        "04",  # 快捷支付
        "05",  # 银联通道
        "06"  # 网联渠道
    ])
    return trans_channel


# 账户类型数据
def make_acc_flag_data(busi_type):
    if busi_type == "01":  # 网络支付
        acc_flag = random.choice([
            "A11",  # 银行账户
            "A12",  # 支付账户
            "A13"  # 预付卡账户
        ])
    elif busi_type == "03":  # 预付卡支付
        acc_flag = random.choice([
            "B11",  # 银行账户
            "B12",  # 支付账户
            "B13",  # 预付卡账户
        ])
    elif busi_type == "02":  # 银行收单
        acc_flag = random.choice([
            "C11",  # 借记卡
            "C12"  # 贷记卡
        ])
    else:
        acc_flag = ""
    return acc_flag


# 交易类型代码数据
def make_trans_cst_type_data():
    """根据客户自己的交易类型，建立字典"""
    trans_cst_type = random.choice([
        "000000",  # 人民币-现钞-银行汇票
        "000001",  # 人民币-现钞-银行承兑汇票
        "000002",  # 人民币-现钞-商业承兑汇票
        "000003",  # 人民币-现钞-本票
        "000004",  # 人民币-现钞-支票
        "000010",  # 人民币-现钞-银行卡
        "000011",  # 人民币-现钞-境外银行卡（非柜台方式交易）
        "000012",  # 人民币-现钞-银行卡（通过POS）
        "000013",  # 人民币-现钞-银行卡（通过ATM 且跨行交易）
        "000014",  # 人民币-现钞-银行卡（通过ATM 且非跨行交易）
        "000015",  # 人民币-现钞-境外银行卡（非柜台方式交易—通过POS）
        "000016",  # 人民币-现钞-境外银行卡（非柜台方式交易—通过ATM）
        "000017",  # 人民币-现钞-境外银行卡（柜台方式交易）
        "000020",  # 人民币-现钞-网上支付
        "000021",  # 人民币-现钞-移动支付
        "000030",  # 人民币-现钞-现金支付
        "000031",  # 人民币-现钞-汇兑
        "000032",  # 人民币-现钞-托收承付
        "000033",  # 人民币-现钞-委托收款
        "000034",  # 人民币-现钞-定期借记
        "000035",  # 人民币-现钞-定期贷记
        "000036",  # 人民币-现钞-国内信用证
        "000051",  # 人民币-现钞-其他
        "000100",  # 人民币-非现钞
        "000101",  # 人民币-非现钞-银行承兑汇票
        "000102",  # 人民币-非现钞-商业承兑汇票
        "000103",  # 人民币-非现钞-本票
        "000104",  # 人民币-非现钞-支票
        "000110",  # 人民币-非现钞-银行卡
        "000111",  # 人民币-非现钞-境外银行卡（非柜台方式交易）
        "000112",  # 人民币-非现钞-银行卡（通过POS）
        "000113",  # 人民币-非现钞-银行卡（通过ATM 且跨行交易）
        "000114",  # 人民币-非现钞-银行卡（通过ATM 且非跨行交易）
        "000115",  # 人民币-非现钞-境外银行卡（非柜台方式交易—通过POS）
        "000116",  # 人民币-非现钞-境外银行卡（非柜台方式交易—通过ATM）
        "000117",  # 人民币-非现钞-境外银行卡（柜台方式交易）
        "000120",  # 人民币-非现钞-网上支付
        "000121",  # 人民币-非现钞-移动支付
        "000130",  # 人民币-非现钞-现金支付
        "000131",  # 人民币-非现钞-汇兑
        "000132",  # 人民币-非现钞-托收承付
        "000133",  # 人民币-非现钞-委托收款
        "000134",  # 人民币-非现钞-定期借记
        "000135",  # 人民币-非现钞-定期贷记
        "000136",  # 人民币-非现钞-国内信用证
        "000151",  # 人民币-非现钞-其他
        "010001",  # 外币-现金
        "010002",  # 外币-现金结售汇
        "010003",  # 外币-现钞兑换
        "010004",  # 外币-其他现金
        "010005",  # 外币-境外银行卡（非柜台方式现金交易）
        "010101",  # 外币-信用证
        "010102",  # 外币-托收
        "010103",  # 外币-保函
        "010104",  # 外币-电汇
        "010105",  # 外币-票汇
        "010106",  # 外币-信汇
        "010107",  # 外币-其他非现金支付
        "010108",  # 外币-境外银行卡（非柜台方式非现金交易）
        "010006",  # 外币-境外银行卡（非柜台方式现金交易—通过 ATM）
        "010007",  # 外币-境外银行卡（柜台方式现金交易）
        "010109",  # 外币-境外银行卡（非柜台方式非现金交易—通过 ATM）
        "010110",  # 外币-境外银行卡（非柜台方式非现金交易—通过 POS）
        "010111",  # 外币-旅行支票
        "020001",  # 代理西联国际汇款（现金业务）
        "020002",  # 代理速汇金国际汇款（现金业务）
        "020003",  # 代理银星速汇国际汇款（现金业务）
        "020004",  # 代理侨汇通国际汇款（现金业务）
        "020005",  # 代理 Paystone国际汇款（现金业务）
        "020099",  # 代理其他公司国际汇款（现金业务）
        "020101",  # 代理西联国际汇款（非现金业务）
        "020102",  # 代理速汇金国际汇款（非现金业务）
        "020103",  # 代理银星速汇国际汇款（非现金业务）
        "020104",  # 代理侨汇通国际汇款（非现金业务）
        "020105",  # 代理 Paystone国际汇款（非现金业务）
        "020199",  # 代理其他公司国际汇款（非现金业务）
        "030100",  # 通过人民币账户购汇并转账
        "030110",  # 通过外币账户结汇并转账
        "030120"  # 本外币间兑换并转账
    ])
    return trans_cst_type


# 代办人国籍数据
def make_country_data():
    agency_country = random.choice([
        "CHN",  # 中国
        "ALB",  # 阿尔巴尼亚
        "DZA",  # 阿尔及利亚
        "AFG",  # 阿富汗
        "ARG",  # 阿根廷
        "ARE",  # 阿联酋
        "ABW",  # 阿鲁巴
        "OMN",  # 阿曼
        "AZE",  # 阿塞拜疆
        "EGY",  # 埃及
        "ETH",  # 埃塞俄比亚
        "IRL",  # 爱尔兰
        "EST",  # 爱沙尼亚
        "AND",  # 安道尔
        "AGO",  # 安哥拉
        "AIA",  # 安圭拉
        "ATG",  # 安提瓜和巴布达
        "AUT",  # 奥地利
        "ALA",  # 奥兰群岛
        "AUS",  # 澳大利亚
        "MAC",  # 澳门
        "BRB",  # 巴巴多斯
        "PNG",  # 巴布亚新几内亚
        "BHS",  # 巴哈马
        "PAK",  # 巴基斯坦
        "PRY",  # 巴拉圭
        "PSE",  # 巴勒斯坦
        "BHR",  # 巴林
        "PAN",  # 巴拿马
        "BRA",  # 巴西
        "BLR",  # 白俄罗斯
        "BMU",  # 百慕大
        "BGR",  # 保加利亚
        "MNP",  # 北马里亚纳群岛
        "BEN",  # 贝宁
        "BEL",  # 比利时
        "ISL",  # 冰岛
        "PRI",  # 波多黎各
        "BIH",  # 波黑
        "POL",  # 波兰
        "BOL",  # 玻利维亚
        "BLZ",  # 伯利兹
        "BWA",  # 博茨瓦纳
        "BTN",  # 不丹
        "BFA",  # 布基纳法索
        "BDI",  # 布隆迪
        "BVT",  # 布韦岛
        "PRK",  # 朝鲜
        "GNQ",  # 赤道几内亚
        "DNK",  # 丹麦
        "DEU",  # 德国
        "TLS",  # 东帝汶
        "TGO",  # 多哥
        "DOM",  # 多米尼加
        "DMA",  # 多米尼克
        "RUS",  # 俄罗斯
        "ECU",  # 厄瓜多尔
        "ERI",  # 厄立特里亚
        "FRA",  # 法国
        "FRO",  # 法罗群岛
        "PYF",  # 法属波利尼西亚
        "GUF",  # 法属圭亚那
        "ATF",  # 法属南部领地
        "MAF",  # 法属圣马丁
        "VAT",  # 梵蒂冈
        "PHL",  # 菲律宾
        "FJI",  # 斐济群岛
        "FIN",  # 芬兰
        "CPV",  # 佛得角
        "GMB",  # 冈比亚
        "COG",  # 刚果（布）
        "COD",  # 刚果（金）
        "COL",  # 哥伦比亚
        "CRI",  # 哥斯达黎加
        "GRD",  # 格林纳达
        "GRL",  # 格陵兰
        "GEO",  # 格鲁吉亚
        "GGY",  # 根西岛
        "CUB",  # 古巴
        "GLP",  # 瓜德罗普
        "GUM",  # 关岛
        "GUY",  # 圭亚那
        "KAZ",  # 哈萨克斯坦
        "HTI",  # 海地
        "KOR",  # 韩国
        "NLD",  # 荷兰
        "BES",  # 荷兰加勒比区
        "SXM",  # 荷属圣马丁
        "HMD",  # 赫德岛和麦克唐纳群岛
        "MNE",  # 黑山
        "HND",  # 洪都拉斯
        "KIR",  # 基里巴斯
        "DJI",  # 吉布提
        "KGZ",  # 吉尔吉斯斯坦
        "GIN",  # 几内亚
        "GNB",  # 几内亚比绍
        "CAN",  # 加拿大
        "GHA",  # 加纳
        "GAB",  # 加蓬
        "KHM",  # 柬埔寨
        "CZE",  # 捷克
        "ZWE",  # 津巴布韦
        "CMR",  # 喀麦隆
        "QAT",  # 卡塔尔
        "CYM",  # 开曼群岛
        "CCK",  # 科科斯群岛
        "COM",  # 科摩罗
        "CIV",  # 科特迪瓦
        "KWT",  # 科威特
        "HRV",  # 克罗地亚
        "KEN",  # 肯尼亚
        "COK",  # 库克群岛
        "CUW",  # 库拉索
        "LVA",  # 拉脱维亚
        "LSO",  # 莱索托
        "LAO",  # 老挝
        "LBN",  # 黎巴嫩
        "LTU",  # 立陶宛
        "LBR",  # 利比里亚
        "LBY",  # 利比亚
        "LIE",  # 列支敦士登
        "REU",  # 留尼汪
        "LUX",  # 卢森堡
        "RWA",  # 卢旺达
        "ROU",  # 罗马尼亚
        "MDG",  # 马达加斯加
        "IMN",  # 马恩岛
        "MDV",  # 马尔代夫
        "FLK",  # 马尔维纳斯群岛（福克兰）
        "MLT",  # 马耳他
        "MWI",  # 马拉维
        "MYS",  # 马来西亚
        "MLI",  # 马里
        "MKD",  # 马其顿
        "MHL",  # 马绍尔群岛
        "MTQ",  # 马提尼克
        "MYT",  # 马约特
        "MUS",  # 毛里求斯
        "MRT",  # 毛里塔尼亚
        "USA",  # 美国
        "UMI",  # 美国本土外小岛屿
        "ASM",  # 美属萨摩亚
        "VIR",  # 美属维尔京群岛
        "MNG",  # 蒙古国；蒙古
        "MSR",  # 蒙塞拉特岛
        "BGD",  # 孟加拉国
        "PER",  # 秘鲁
        "FSM",  # 密克罗尼西亚联邦
        "MMR",  # 缅甸
        "MDA",  # 摩尔多瓦
        "MAR",  # 摩洛哥
        "MCO",  # 摩纳哥
        "MOZ",  # 莫桑比克
        "MEX",  # 墨西哥
        "NKR",  # 纳戈尔诺-卡拉巴赫
        "NAM",  # 纳米比亚
        "ZAF",  # 南非
        "ATA",  # 南极洲
        "SGS",  # 南乔治亚岛和南桑威奇群岛
        "SSD",  # 南苏丹
        "NRU",  # 瑙鲁
        "NPL",  # 尼泊尔
        "NIC",  # 尼加拉瓜
        "NER",  # 尼日尔
        "NGA",  # 尼日利亚
        "NIU",  # 纽埃
        "NOR",  # 挪威
        "NFK",  # 诺福克岛
        "PLW",  # 帕劳
        "PCN",  # 皮特凯恩群岛
        "PRT",  # 葡萄牙
        "JPN",  # 日本
        "SWE",  # 瑞典
        "CHE",  # 瑞士
        "SLV",  # 萨尔瓦多
        "WSM",  # 萨摩亚
        "SRB",  # 塞尔维亚
        "SLE",  # 塞拉利昂
        "SEN",  # 塞内加尔
        "CYP",  # 塞浦路斯
        "SYC",  # 塞舌尔
        "SAU",  # 沙特阿拉伯
        "BLM",  # 圣巴泰勒米岛
        "CXR",  # 圣诞岛
        "STP",  # 圣多美和普林西比
        "SHN",  # 圣赫勒拿
        "KNA",  # 圣基茨和尼维斯
        "LCA",  # 圣卢西亚
        "SMR",  # 圣马力诺
        "SPM",  # 圣皮埃尔和密克隆
        "VCT",  # 圣文森特和格林纳丁斯
        "LKA",  # 斯里兰卡
        "SVK",  # 斯洛伐克
        "SVN",  # 斯洛文尼亚
        "SJM",  # 斯瓦尔巴群岛和扬马延岛
        "SWZ",  # 斯威士兰
        "SDN",  # 苏丹
        "SUR",  # 苏里南
        "SLB",  # 所罗门群岛
        "SOM",  # 索马里
        "TJK",  # 塔吉克斯坦
        "THA",  # 泰国
        "TZA",  # 坦桑尼亚
        "TON",  # 汤加
        "TCA",  # 特克斯和凯科斯群岛
        "TTO",  # 特立尼达和多巴哥
        "TUN",  # 突尼斯
        "TUV",  # 图瓦卢
        "TUR",  # 土耳其
        "TKM",  # 土库曼斯坦
        "TKL",  # 托克劳
        "WLF",  # 瓦利斯和富图纳
        "VUT",  # 瓦努阿图
        "GTM",  # 危地马拉
        "VEN",  # 委内瑞拉
        "BRN",  # 文莱
        "UGA",  # 乌干达
        "UKR",  # 乌克兰
        "URY",  # 乌拉圭
        "UZB",  # 乌兹别克斯坦
        "ESP",  # 西班牙
        "ESH",  # 西撒哈拉
        "GRC",  # 希腊
        "HKG",  # 香港
        "SGP",  # 新加坡
        "NCL",  # 新喀里多尼亚
        "NZL",  # 新西兰
        "HUN",  # 匈牙利
        "SYR",  # 叙利亚
        "JAM",  # 牙买加
        "ARM",  # 亚美尼亚
        "YEM",  # 也门
        "IRQ",  # 伊拉克
        "IRN",  # 伊朗
        "ISR",  # 以色列
        "ITA",  # 意大利
        "IND",  # 印度
        "IDN",  # 印尼
        "GBR",  # 英国
        "VGB",  # 英属维尔京群岛
        "IOT",  # 英属印度洋领地
        "JOR",  # 约旦
        "VNM",  # 越南
        "ZMB",  # 赞比亚
        "JEY",  # 泽西岛
        "TCD",  # 乍得
        "GIB",  # 直布罗陀
        "CHL",  # 智利
        "CAF",  # 中非
        "TWN"  # 中国台湾
    ])
    return agency_country


# 身份证件类型
def make_citp_data():
    citp = random.choice([
        "11",  # 居民身份证或临时身份证
        "12",  # 军人或武警身份证件
        "13",  # 港澳台通行证
        "14",  # 外国公民护照
        "19"  # 其他个人有效证件(需进一步说明) 中国公民护照填写'19'
    ])
    return citp


# 企业规模数据
def make_scale_data():
    scale = random.choice([
        "1",  # 500人以上
        "2",  # 200-500人
        "3",  # 10-200人
        "4"  # 10人及以下
    ])
    return scale


# 组织机构类别数据
def make_crp_type_data():
    crp_type = random.choice([
        "1",  # 企业
        "2",  # 机关
        "3",  # 事业单位
        "4",  # 社会团体
        "5"  # 其他组织机构
    ])
    return crp_type


# 股权复杂度数据
def make_complex_data():
    complex = random.choice([
        "1",  # 股权 3层以下
        "2",  # 股权 3层及以上，有商业目的
        "3"  # 股权 3层以上；或3个及以上注册地；涉及信托/不受监管的投资基金/代名人股东等；及没有明显商业目的
    ])
    return complex

# 交易对手id数据
def make_tcif_id_data(busi_type):
    """
    交易对手id，不适用于收单，当交易类型为银行收单时返回空
    :param busi_type:
    :return:
    """
    if busi_type == "02":
        tcif_id = ''
    else:
        tcif_id = make_random_num(22)
    return tcif_id


# 特约商户收单结算账号数据
def make_self_acc_no_data(client_tp):
    """
    非商户不填（网络支付、预付卡、银行卡收单均需填写）
    :param client_tp:
    :return:
    """
    if client_tp == "02":
        self_acc_no = make_random_num(20)
    else:
        self_acc_no = ""
    return self_acc_no


# 账户类型数据
def make_acc_type1_data(client_tp):
    """
    非商户不填（网络支付、预付卡、银行卡收单均需填写）
    :param client_tp:
    :return:
    """
    if client_tp == "02":
        acc_type1 = random.choice(["11", "12"])
    else:
        acc_type1 = ""
    return acc_type1


# 银行账户名称数据
def make_bank_acc_name_data(acc_type1):
    """
    当acc_type1=12时填写，银行账号对应账户名称（网络支付、预付卡、银行卡收单均需填写）
    :param acc_type1:
    :return:
    """
    if acc_type1 == "12":
        bank_acc_name = "XXX信息科技有限公司"
    else:
        bank_acc_name = ""
    return bank_acc_name


# 对手账号标识数据
def make_tran_flag_data(busi_type):
    """
    对手账号标识数据，仅需网络支付填写，其他不填
    :param busi_type:
    :return:
    """
    if busi_type == "01":
        tran_flag = random.choice(["11", "12"])
    else:
        tran_flag = ''
    return tran_flag

# 交易订单号数据
def make_trans_order_data(busi_type):
    """
    交易订单号，仅需网络支付填写
    :param busi_type:
    :return:
    """
    if busi_type == "01":
        trans_order = make_random_num(20)
    else:
        trans_order = ""

    return trans_order

# 非自然人股权可辨识度数据
def make_clear_data():
    clear = random.choice([
        "1",  # 全民集体所有制企业等结构清晰的企业
        "2",  # 公司制企业等结构相对清晰的企业
        "3",  # 公司制外资企业等结构较难识辨的企业
        "4",  # 个人独资企业、家族企业、合伙等难以尽调的企业
        "5"  # 其他风险较高股权或控制权结构（信托、代名股东等
    ])
    return clear


# 批量代付标识数据
def make_batch_pay_data(busi_type, client_tp):
    """
    批量代付标识,预付卡业务不填
    :param busi_type:
    :return:
    """
    if busi_type == "03":
        batch_pay = ""
    elif client_tp == "1":
        batch_pay = "2"
    else:
        batch_pay = random.choice(["1", "2"])
    return batch_pay


# 网络支付商户网址信息数据
def make_web_info_data(busi_type):
    """
    网络支付商户网址信息、与商户签约时登记注册网址，非网络支付业务，以及无网址的商户可不填,
    默认网络用户都填了
    :param busi_type:
    :return:
    """
    if busi_type == "01":
        web_info = "http://www.baidu.com"
    else:
        web_info = ""
    return web_info

# 地址类型数据
def make_address_tp_data():
    address_tp = random.choice([
        "11",  # 家庭地址
        "12",  # 工作地址
        "13",  # 证件地址
        "21",  # 注册地址
        "22",  # 经营地址
        "99"  # 其它地址
    ])
    return address_tp


# 支付账户表账户状态数据
def make_pact_cls_dt_data(name):
    """
    非正常数据各造一条，其他为正常数据
    "C",  # 注销
    "N",  # 正常
    "I",  # 待激活
    "U",  # 闲置
    "B"  # 冻结
    :param name:
    :return:
    """
    num = name.split("_")
    if num[-1] == "1":
        cls_dt = "C"
    elif num[-1] == "2":
        cls_dt = "I"
    elif num[-1] == "3":
        cls_dt = "U"
    elif num[-1] == "4":
        cls_dt = "B"
    else:
        cls_dt = "N"
    return cls_dt


# 个人/机构表销户日期数据
def make_cls_dt_data(name):
    """
    个人表销户日期数据,使用随机生成注册日期函数生成日期,默认当客户号尾号数字为1时，账户是销户
    :param name:
    :return:
    """
    num = name.split("_")
    if num[-1] == "1":
        cls_dt = make_register_date()
    else:
        cls_dt = ""
    return cls_dt

# 账户分类数据
def make_account_tp_data(busi_type):
    if busi_type in ["02", "03"]:
        account_tp = ""
    else:
        account_tp = random.choice(["1", "2", "3"])
    return account_tp

# 管理机构数据
def make_mer_unit_data():
    """
    需提供码表，暂无，默认1000，代表S1总部
    :return:
    """
    return "1000"
# 个人绑定银行卡数据
def make_bind_card_data(busi_type):
    """
    个人绑定银行卡/企业绑定银行账户(仅需网络支付填写)
    :param busi_type:
    :return:
    """
    if busi_type == "01":
        bind_card = random.choice(["11", "12"])
    else:
        bind_card = ""
    return bind_card

# 关联支付账户数据
def make_pay_id_data(busi_type, act_cd):
    """
    关联支付账户数据，银行卡收单业务不填，网络和预付卡业务，取支付账户表中的支付账号
    :param busi_type:
    :param act_cd:
    :return:
    """
    if busi_type == "02":
        pay_id = ""
    else:
        pay_id = act_cd
    return pay_id


# 婚姻状态数据
def make_marriage_data(ctid):
    """
    25岁以下，未婚，25岁以上，已婚、离异、丧偶、其他。
    :param ctid: 身份证号
    :return:
    """
    year_now = time.strftime("%Y", time.localtime())
    age = int(year_now) - int(ctid[6:10])
    if age < 25:
        marriage = "1"
    else:
        marriage = random.choice([
            "2",
            "3",
            "4",
            "5"
        ])
    return marriage

# 境内外标识数据
def make_bord_flag_data():
    """
    境内外标识数据,网络支付、预付卡、银行卡收单必须填写,境内、外数量比例4:1
    :return:
    """
    return random.choice(["11" if num > 1 else "12" for num in range(10)])

# 商户所在国家数据
def make_con_nation_data(bord_flag):
    """如果境内外标识为11(境内)，商户所在地选中国，为12，
    商户所在第随机选别的国家，台湾暂时放在境外，
    网络支付、预付卡、银行卡收单必须填写"""
    if bord_flag == "11":
        con_nation = "CHN"
    else:
        con_nation = random.choice([
            "ALB",  # 阿尔巴尼亚
            "DZA",  # 阿尔及利亚
            "AFG",  # 阿富汗
            "ARG",  # 阿根廷
            "ARE",  # 阿联酋
            "ABW",  # 阿鲁巴
            "OMN",  # 阿曼
            "AZE",  # 阿塞拜疆
            "EGY",  # 埃及
            "ETH",  # 埃塞俄比亚
            "IRL",  # 爱尔兰
            "EST",  # 爱沙尼亚
            "AND",  # 安道尔
            "AGO",  # 安哥拉
            "AIA",  # 安圭拉
            "ATG",  # 安提瓜和巴布达
            "AUT",  # 奥地利
            "ALA",  # 奥兰群岛
            "AUS",  # 澳大利亚
            "MAC",  # 澳门
            "BRB",  # 巴巴多斯
            "PNG",  # 巴布亚新几内亚
            "BHS",  # 巴哈马
            "PAK",  # 巴基斯坦
            "PRY",  # 巴拉圭
            "PSE",  # 巴勒斯坦
            "BHR",  # 巴林
            "PAN",  # 巴拿马
            "BRA",  # 巴西
            "BLR",  # 白俄罗斯
            "BMU",  # 百慕大
            "BGR",  # 保加利亚
            "MNP",  # 北马里亚纳群岛
            "BEN",  # 贝宁
            "BEL",  # 比利时
            "ISL",  # 冰岛
            "PRI",  # 波多黎各
            "BIH",  # 波黑
            "POL",  # 波兰
            "BOL",  # 玻利维亚
            "BLZ",  # 伯利兹
            "BWA",  # 博茨瓦纳
            "BTN",  # 不丹
            "BFA",  # 布基纳法索
            "BDI",  # 布隆迪
            "BVT",  # 布韦岛
            "PRK",  # 朝鲜
            "GNQ",  # 赤道几内亚
            "DNK",  # 丹麦
            "DEU",  # 德国
            "TLS",  # 东帝汶
            "TGO",  # 多哥
            "DOM",  # 多米尼加
            "DMA",  # 多米尼克
            "RUS",  # 俄罗斯
            "ECU",  # 厄瓜多尔
            "ERI",  # 厄立特里亚
            "FRA",  # 法国
            "FRO",  # 法罗群岛
            "PYF",  # 法属波利尼西亚
            "GUF",  # 法属圭亚那
            "ATF",  # 法属南部领地
            "MAF",  # 法属圣马丁
            "VAT",  # 梵蒂冈
            "PHL",  # 菲律宾
            "FJI",  # 斐济群岛
            "FIN",  # 芬兰
            "CPV",  # 佛得角
            "GMB",  # 冈比亚
            "COG",  # 刚果（布）
            "COD",  # 刚果（金）
            "COL",  # 哥伦比亚
            "CRI",  # 哥斯达黎加
            "GRD",  # 格林纳达
            "GRL",  # 格陵兰
            "GEO",  # 格鲁吉亚
            "GGY",  # 根西岛
            "CUB",  # 古巴
            "GLP",  # 瓜德罗普
            "GUM",  # 关岛
            "GUY",  # 圭亚那
            "KAZ",  # 哈萨克斯坦
            "HTI",  # 海地
            "KOR",  # 韩国
            "NLD",  # 荷兰
            "BES",  # 荷兰加勒比区
            "SXM",  # 荷属圣马丁
            "HMD",  # 赫德岛和麦克唐纳群岛
            "MNE",  # 黑山
            "HND",  # 洪都拉斯
            "KIR",  # 基里巴斯
            "DJI",  # 吉布提
            "KGZ",  # 吉尔吉斯斯坦
            "GIN",  # 几内亚
            "GNB",  # 几内亚比绍
            "CAN",  # 加拿大
            "GHA",  # 加纳
            "GAB",  # 加蓬
            "KHM",  # 柬埔寨
            "CZE",  # 捷克
            "ZWE",  # 津巴布韦
            "CMR",  # 喀麦隆
            "QAT",  # 卡塔尔
            "CYM",  # 开曼群岛
            "CCK",  # 科科斯群岛
            "COM",  # 科摩罗
            "CIV",  # 科特迪瓦
            "KWT",  # 科威特
            "HRV",  # 克罗地亚
            "KEN",  # 肯尼亚
            "COK",  # 库克群岛
            "CUW",  # 库拉索
            "LVA",  # 拉脱维亚
            "LSO",  # 莱索托
            "LAO",  # 老挝
            "LBN",  # 黎巴嫩
            "LTU",  # 立陶宛
            "LBR",  # 利比里亚
            "LBY",  # 利比亚
            "LIE",  # 列支敦士登
            "REU",  # 留尼汪
            "LUX",  # 卢森堡
            "RWA",  # 卢旺达
            "ROU",  # 罗马尼亚
            "MDG",  # 马达加斯加
            "IMN",  # 马恩岛
            "MDV",  # 马尔代夫
            "FLK",  # 马尔维纳斯群岛（福克兰）
            "MLT",  # 马耳他
            "MWI",  # 马拉维
            "MYS",  # 马来西亚
            "MLI",  # 马里
            "MKD",  # 马其顿
            "MHL",  # 马绍尔群岛
            "MTQ",  # 马提尼克
            "MYT",  # 马约特
            "MUS",  # 毛里求斯
            "MRT",  # 毛里塔尼亚
            "USA",  # 美国
            "UMI",  # 美国本土外小岛屿
            "ASM",  # 美属萨摩亚
            "VIR",  # 美属维尔京群岛
            "MNG",  # 蒙古国；蒙古
            "MSR",  # 蒙塞拉特岛
            "BGD",  # 孟加拉国
            "PER",  # 秘鲁
            "FSM",  # 密克罗尼西亚联邦
            "MMR",  # 缅甸
            "MDA",  # 摩尔多瓦
            "MAR",  # 摩洛哥
            "MCO",  # 摩纳哥
            "MOZ",  # 莫桑比克
            "MEX",  # 墨西哥
            "NKR",  # 纳戈尔诺-卡拉巴赫
            "NAM",  # 纳米比亚
            "ZAF",  # 南非
            "ATA",  # 南极洲
            "SGS",  # 南乔治亚岛和南桑威奇群岛
            "SSD",  # 南苏丹
            "NRU",  # 瑙鲁
            "NPL",  # 尼泊尔
            "NIC",  # 尼加拉瓜
            "NER",  # 尼日尔
            "NGA",  # 尼日利亚
            "NIU",  # 纽埃
            "NOR",  # 挪威
            "NFK",  # 诺福克岛
            "PLW",  # 帕劳
            "PCN",  # 皮特凯恩群岛
            "PRT",  # 葡萄牙
            "JPN",  # 日本
            "SWE",  # 瑞典
            "CHE",  # 瑞士
            "SLV",  # 萨尔瓦多
            "WSM",  # 萨摩亚
            "SRB",  # 塞尔维亚
            "SLE",  # 塞拉利昂
            "SEN",  # 塞内加尔
            "CYP",  # 塞浦路斯
            "SYC",  # 塞舌尔
            "SAU",  # 沙特阿拉伯
            "BLM",  # 圣巴泰勒米岛
            "CXR",  # 圣诞岛
            "STP",  # 圣多美和普林西比
            "SHN",  # 圣赫勒拿
            "KNA",  # 圣基茨和尼维斯
            "LCA",  # 圣卢西亚
            "SMR",  # 圣马力诺
            "SPM",  # 圣皮埃尔和密克隆
            "VCT",  # 圣文森特和格林纳丁斯
            "LKA",  # 斯里兰卡
            "SVK",  # 斯洛伐克
            "SVN",  # 斯洛文尼亚
            "SJM",  # 斯瓦尔巴群岛和扬马延岛
            "SWZ",  # 斯威士兰
            "SDN",  # 苏丹
            "SUR",  # 苏里南
            "SLB",  # 所罗门群岛
            "SOM",  # 索马里
            "TJK",  # 塔吉克斯坦
            "THA",  # 泰国
            "TZA",  # 坦桑尼亚
            "TON",  # 汤加
            "TCA",  # 特克斯和凯科斯群岛
            "TTO",  # 特立尼达和多巴哥
            "TUN",  # 突尼斯
            "TUV",  # 图瓦卢
            "TUR",  # 土耳其
            "TKM",  # 土库曼斯坦
            "TKL",  # 托克劳
            "WLF",  # 瓦利斯和富图纳
            "VUT",  # 瓦努阿图
            "GTM",  # 危地马拉
            "VEN",  # 委内瑞拉
            "BRN",  # 文莱
            "UGA",  # 乌干达
            "UKR",  # 乌克兰
            "URY",  # 乌拉圭
            "UZB",  # 乌兹别克斯坦
            "ESP",  # 西班牙
            "ESH",  # 西撒哈拉
            "GRC",  # 希腊
            "HKG",  # 香港
            "SGP",  # 新加坡
            "NCL",  # 新喀里多尼亚
            "NZL",  # 新西兰
            "HUN",  # 匈牙利
            "SYR",  # 叙利亚
            "JAM",  # 牙买加
            "ARM",  # 亚美尼亚
            "YEM",  # 也门
            "IRQ",  # 伊拉克
            "IRN",  # 伊朗
            "ISR",  # 以色列
            "ITA",  # 意大利
            "IND",  # 印度
            "IDN",  # 印尼
            "GBR",  # 英国
            "VGB",  # 英属维尔京群岛
            "IOT",  # 英属印度洋领地
            "JOR",  # 约旦
            "VNM",  # 越南
            "ZMB",  # 赞比亚
            "JEY",  # 泽西岛
            "TCD",  # 乍得
            "GIB",  # 直布罗陀
            "CHL",  # 智利
            "CAF",  # 中非
            "TWN"  # 中国台湾
        ])
    return con_nation


# 客户真实有效性数据
def make_reals_data():
    """
    正常为空，不正常：
    1:留存的联系地址与注册地址不一致
    2:留存联系地址不存在或者虚构
    3:留存的电话号码属于无效、空号、已停机或无法接通
    4:证件非本人、证件伪造、变造证件
    5:拒绝配合尽职调查工作
    正常数据与不正常数据比例为1:10
    :return:
    """
    return random.choice(['' if num >= 1 else str(random.randint(1, 5)) for num in range(10)])

# 结算类型数据
def make_statement_type_data(client_tp):
    """
    结算类型数据，如果是个人，为空，商户随机选择
    :param client_tp:
    :return:
    """
    if client_tp == "1":
        statement_type = ""
    else:
        statement_type = random.choice(["0", "1"])
    return statement_type


# 生成个人表
def make_stan_persion(num):
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
    busi_reg_no = "person_new2_{}".format(num)
    ctnm = make_name_data()
    cten = word_to_pinyin(ctnm)
    client_tp = random.choice(["1", "2"])
    busi_type = make_busi_type_data()
    account_tp = make_account_tp_data(busi_type)
    if client_tp == "2":
        smid = random.randint(1000, 9999)  # 该字段值待确定
        smid = str(smid)
    else:
        smid = ""
    citp = make_citp_data()
    citp_ori = citp  # 该值暂定
    citp_nt = "有效证件"
    ctid = make_IDCard()
    ctid_edt = make_Card_valid_date(ctid)
    sex = make_sex(ctid)
    country = choice_contry()
    nation = str(random.randint(1, 57))
    birthday = ctid[6:14]
    education = str(random.randint(1, 7))
    ctvc = random.choice(["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H"])
    picm = "300000"
    ficm = "500000"
    marriage = make_marriage_data(ctid)
    ceml = make_email_data()
    rgdt = make_register_date()
    cls_dt = make_cls_dt_data(busi_reg_no)
    remark = "这是一个备注"
    indu_code = "666666"
    stat_flag_ori = "888888"
    stat_flag = make_stat_flag_data(busi_reg_no)
    mer_prov = get_province_data(ctid[:6])
    mer_city = make_province_city_data(ctid[:6])[0]
    mer_area = make_province_city_data(ctid[:6])[-1]
    address = make_address(ctid[:6])
    tel = make_tel_num()
    mer_unit = make_mer_unit_data()
    is_line = random.choice(["0", "1"])
    certification = random.choice(["1", "2", "3"])
    cer_num = str(random.randint(0, 6))
    con_acc_name = "默认经营名称"  # 网络支付、预付卡、银行卡收单必须填写,暂为空
    bord_flag = make_bord_flag_data()
    web_info = make_web_info_data(busi_type)  # 非网络支付业务，无网址用户可不填
    con_nation = make_con_nation_data(bord_flag)
    bind_card = make_bind_card_data(busi_type)  # 仅需网络支付填写
    ip_code = make_ip_data(busi_type)  # 仅需网络支付填写
    mac_info = make_mac_info_data(busi_type)  # PC机填写MAC，移动终端填写IMEI(需网络支付，预付卡填写), 暂为空
    self_acc_no = make_self_acc_no_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    acc_type1 = make_acc_type1_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    bank_acc_name = make_bank_acc_name_data(acc_type1)
    reals = make_reals_data()
    batch_pay = make_batch_pay_data(busi_type, client_tp)
    statement_type = make_statement_type_data(client_tp)

    print(busi_reg_no, ctnm, cten, client_tp, account_tp, busi_type, smid, citp, citp_ori, citp_nt, ctid, ctid_edt, sex,
          country, nation, birthday, education, ctvc, picm, ficm, marriage, ceml, rgdt, cls_dt, remark, indu_code,
          stat_flag_ori, stat_flag, mer_prov, mer_city, mer_area, address, tel, mer_unit, is_line, certification,
          cer_num, con_acc_name, bord_flag, web_info, con_nation, bind_card, ip_code, mac_info, self_acc_no, acc_type1,
          bank_acc_name, reals, batch_pay, statement_type)
    contect_data = make_connect_data([
        busi_reg_no, ctnm, cten, client_tp, account_tp, busi_type, smid, citp, citp_ori, citp_nt, ctid, ctid_edt, sex,
        country, nation, birthday, education, ctvc, picm, ficm, marriage, ceml, rgdt, cls_dt, remark, indu_code,
        stat_flag_ori, stat_flag, mer_prov, mer_city, mer_area, address, tel, mer_unit, is_line, certification,
        cer_num, con_acc_name, bord_flag, web_info, con_nation, bind_card, ip_code, mac_info, self_acc_no, acc_type1,
        bank_acc_name, reals, batch_pay, statement_type
    ])
    return {
               "busi_reg_no": busi_reg_no,
               "ctnm": ctnm,
               "cten": cten,
               "client_tp": client_tp,
               "account_tp": account_tp,
               "busi_type": busi_type,
               "smid": smid,
               "citp": citp,
               "citp_ori": citp_ori,
               "citp_nt": citp_nt,
               "ctid": ctid,
               "ctid_edt": ctid_edt,
               "sex": sex,
               "country": country,
               "nation": nation,
               "birthday": birthday,
               "education": education,
               "ctvc": ctvc,
               "picm": picm,
               "ficm": ficm,
               "marriage": marriage,
               "ceml": ceml,
               "rgdt": rgdt,
               "cls_dt": cls_dt,
               "remark": remark,
               "indu_code": indu_code,
               "stat_flag_ori": stat_flag_ori,
               "stat_flag": stat_flag,
               "mer_prov": mer_prov,
               "mer_city": mer_city,
               "mer_area": mer_area,
               "address": address,
               "tel": tel,
               "mer_unit": mer_unit,
               "is_line": is_line,
               "certification ": certification,
               "cer_num": cer_num,
               "con_acc_name": con_acc_name,
               "bord_flag": bord_flag,
               "web_info": web_info,
               "con_nation": con_nation,
               "bind_card": bind_card,
               "ip_code": ip_code,
               "mac_info": mac_info,
               "self_acc_no": self_acc_no,
               "acc_type1": acc_type1,
               "bank_acc_name": bank_acc_name,
               "reals": reals,
               "batch_pay": batch_pay,
               "statement_type": statement_type
           }, contect_data


# 生成机构表
def make_stan_org(num):
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
    busi_reg_no = "org_new2_{}".format(num)
    ctnm = make_name_data()
    cten = word_to_pinyin(ctnm)
    client_tp = random.choice(["1", "2"])
    busi_type = make_busi_type_data()
    account_tp = make_account_tp_data(busi_type)
    if client_tp == "2":
        smid = make_random_str(20)  # 该字段值待确定
    else:
        smid = ""
    citp = random.choice(["21", "29"])
    citp_ori = citp  # 该值暂定
    ctid = make_IDCard()
    ctid_edt = make_Card_valid_date(ctid)
    if citp == "29":
        citp_nt = random.choice(["营业执照", "统一社会信用代码"])
    else:
        citp_nt = "证件类型"

    if citp_ori == "营业执照":
        id_type = "11"
    else:
        id_type = "12"

    org_no = make_random_num(9)  # 统一社会信用代码9-17位
    linkman = make_name_data()
    linktel = make_tel_num()
    linkjob = "联系人职务"
    linkmail = make_email_data()
    linkphone = make_random_num(9)
    ceml = make_email_data()
    ctvc = make_org_ctvc_data()
    crnm = make_name_data()
    crit = make_citp_data()
    crit_ori = "证件原值"
    if crit == "19":
        crit_nt = "证件类型说明"
    else:
        crit_nt = ""
    crid = make_IDCard()
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
    agency_ctid = make_IDCard()
    agency_edt = make_Card_valid_date(agency_ctid)
    remark = "备注，暂时不填"
    indu_code = "11111"  # 支付机构行业代码，暂时默认为11111
    stat_flag_ori = "11111"  # 客户状态原值，可是用支付系统码表，根据客户业务系统修改
    stat_flag = make_stat_flag_data(busi_reg_no)
    mer_prov = get_province_data(ctid[:6])
    mer_city = make_province_city_data(ctid[:6])[0]
    mer_area = make_province_city_data(ctid[:6])[-1]
    address = make_address(ctid[:6])
    tel = make_tel_num()
    mer_unit = make_mer_unit_data()
    is_line = random.choice(["0", "1"])
    certification = random.choice(["1", "2", "3"])
    cer_num = str(random.randint(0, 6))
    con_acc_name = "默认经营名称"  # 网络支付、预付卡、银行卡收单必须填写,暂为空
    bord_flag = make_bord_flag_data()  # 网络支付、预付卡、银行卡收单必须填写
    web_info = make_web_info_data(busi_type)  # 非网络支付业务，无网址用户可不填
    con_nation = make_con_nation_data(bord_flag)  # 网络支付、预付卡、银行卡收单必须填写
    majority_shareholder_ctnm = make_name_data()
    majority_shareholder_citp = make_citp_data()
    majority_shareholder_citp_ori = "控股股东或实际控制人证件类型原值"
    majority_shareholder_ctid = make_IDCard()
    majority_shareholder_edt = make_Card_valid_date(majority_shareholder_ctid)
    reg_cptl_code = "CNY"
    bind_card = make_bind_card_data(busi_type)  # 仅需网络支付填写
    ip_code = make_ip_data(busi_type)  # 仅需网络支付填写
    mac_info = make_mac_info_data(busi_type)  # PC机填写MAC，移动终端填写IMEI(需网络支付，预付卡填写), 暂为空
    self_acc_no = make_self_acc_no_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    acc_type1 = make_acc_type1_data(client_tp)  # 非商户不填，网络支付、预付卡、银行卡收单必须填写
    bank_acc_name = make_bank_acc_name_data(acc_type1)  # 当acc_type1=12时填写，银行账号对应账户名称（ 网络支付、预付卡、银行卡收单均需填写）
    reals = str(random.randint(1, 5))
    complex = make_complex_data()
    clear = make_clear_data()
    batch_pay = make_batch_pay_data(busi_type, client_tp)
    statement_type = random.choice(["0", "1"])


    print(busi_reg_no, ctnm, cten, client_tp, account_tp, busi_type, smid, citp, citp_ori, ctid, ctid_edt, citp_nt,
          id_type, org_no, linkman, linktel, linkjob, linkmail, linkphone, ceml, ctvc, crnm, crit, crit_ori, crit_nt,
          crid, crid_edt, rgdt, cls_dt, scale, country, crp_type, fud_date, reg_cptl, remark_ctvc, agency_ctnm,
          agency_citp, agency_ctid, agency_edt, remark, indu_code, stat_flag_ori, stat_flag, mer_prov, mer_city,
          mer_area, address, tel, mer_unit, is_line, certification, cer_num, con_acc_name, bord_flag, web_info,
          con_nation, majority_shareholder_ctnm, majority_shareholder_citp, majority_shareholder_citp_ori,
          majority_shareholder_ctid, majority_shareholder_edt, reg_cptl_code, bind_card, ip_code, mac_info, self_acc_no,
          acc_type1, bank_acc_name, reals, complex, clear, batch_pay, statement_type)
    contect_data = make_connect_data([
        busi_reg_no, ctnm, cten, client_tp, account_tp, busi_type, smid, citp, citp_ori, ctid, ctid_edt, citp_nt,
        id_type, org_no, linkman, linktel, linkjob, linkmail, linkphone, ceml, ctvc, crnm, crit, crit_ori, crit_nt,
        crid, crid_edt, rgdt, cls_dt, scale, country, crp_type, fud_date, reg_cptl, remark_ctvc, agency_ctnm,
        agency_citp, agency_ctid, agency_edt, remark, indu_code, stat_flag_ori, stat_flag, mer_prov, mer_city, mer_area,
        address, tel, mer_unit, is_line, certification, cer_num, con_acc_name, bord_flag, web_info, con_nation,
        majority_shareholder_ctnm, majority_shareholder_citp, majority_shareholder_citp_ori, majority_shareholder_ctid,
        majority_shareholder_edt, reg_cptl_code, bind_card, ip_code, mac_info, self_acc_no, acc_type1, bank_acc_name,
        reals, complex, clear, batch_pay, statement_type
    ])

    return {
               "busi_reg_no": busi_reg_no,
               "ctnm": ctnm,
               "cten": cten,
               "client_tp": client_tp,
               "account_tp": account_tp,
               "busi_type": busi_type,
               "smid": smid,
               "citp": citp,
               "citp_ori": citp_ori,
               "ctid": ctid,
               "ctid_edt": ctid_edt,
               "citp_nt": citp_nt,
               "id_type": id_type,
               "org_no": org_no,
               "linkman": linkman,
               "linktel": linktel,
               "linkjob": linkjob,
               "linkmail": linkmail,
               "linkphone": linkphone,
               "ceml": ceml,
               "ctvc": ctvc,
               "crnm": crnm,
               "crit": crit,
               "crit_ori": crit_ori,
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
               "stat_flag_ori": stat_flag_ori,
               "stat_flag": stat_flag,
               "mer_prov": mer_prov,
               "mer_city": mer_city,
               "mer_area": mer_area,
               "address": address,
               "tel": tel,
               "mer_unit": mer_unit,
               "is_line": is_line,
               "certification": certification,
               "cer_num": cer_num,
               "con_acc_name": con_acc_name,
               "bord_flag": bord_flag,
               "web_info": web_info,
               "con_nation": con_nation,
               "majority_shareholder_ctnm": majority_shareholder_ctnm,
               "majority_shareholder_citp": majority_shareholder_citp,
               "majority_shareholder_citp_ori": majority_shareholder_citp_ori,
               "majority_shareholder_ctid": majority_shareholder_ctid,
               "majority_shareholder_edt": majority_shareholder_edt,
               "reg_cptl_code": reg_cptl_code,
               "bind_card": bind_card,
               "ip_code": ip_code,
               "mac_info": mac_info,
               "self_acc_no": self_acc_no,
               "acc_type1": acc_type1,
               "bank_acc_name": bank_acc_name,
               "reals": reals,
               "complex": complex,
               "clear": clear,
               "batch_pay": batch_pay,
               "statement_type": statement_type
           }, contect_data

# 证件签发日期数据
def make_iss_dt_data(ctid_edt):
    """
    有效期减去10,20,长期的随机减去一定年数
    :return:
    """
    year_now = time.strftime("%Y", time.localtime())
    mouth_date = time.strftime("%m%d", time.localtime())
    if ctid_edt == "99991231":
        sign_date = str(int(year_now) - random.choice([3, 5, 10, 20, 30])) + mouth_date
    else:
        date = random.choice([10, 20])
        # age = int(year_now) - int(ctid[6:10])
        sign_date = int(ctid_edt[:4]) - date
        sign_date = str(sign_date) + ctid_edt[4:]

    return sign_date


# 客户证件表
def make_stan_cert(infos):
    """
    ctif_id:客户号
    ctif_tp:主体类型
    citp:证件类型
    citp_ori:证件类型原值
    citp_nt:证件类型说明
    ctid:证件号码
    iss_unt:证件签发机关
    address:证件地址
    ctid_edt:主体证件有效期
    iss_dt:证件签发日期
    iss_ctry:证件签发国家
    is_rp:是否主证件

    :return:
    """
    ctif_id = infos.get("busi_reg_no")  # 取值
    ctif_tp = "1"
    citp = infos.get("citp")  # 取值
    citp_ori = infos.get("citp_ori")  # 取值
    citp_nt = infos.get("citp_nt")  # 取值
    ctid = infos.get("ctid")  # 取值
    iss_unt = make_province_city_process_data(ctid[:6]) + "公安局"  # 取值户籍所在地县级公安局
    address = infos.get("address")  # 取值
    ctid_edt = infos.get("ctid_edt")  # 取值，
    iss_dt = make_iss_dt_data(ctid_edt)
    iss_ctry = infos.get("country")  # 取值，
    is_rp = "1"  # 考虑添加副证件
    print(ctif_id, ctif_tp, citp, citp_ori, citp_nt, ctid, iss_unt, address, ctid_edt, iss_dt, iss_ctry, is_rp)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, citp, citp_ori, citp_nt, ctid, iss_unt, address, ctid_edt, iss_dt, iss_ctry, is_rp
    ])
    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "citp": citp,
               "citp_ori": citp_ori,
               "citp_nt": citp_nt,
               "ctid": ctid,
               "iss_unt": iss_unt,
               "address": address,
               "ctid_edt": ctid_edt,
               "iss_dt": iss_dt,
               "iss_ctry": iss_ctry,
               "is_rp": is_rp
           }, contect_data


# 客户地址信息表
def make_stan_address(infos, ctif_tp_data):
    """
    ctif_id: 客户号
    ctif_tp: 主体类型
    address_tp: 地址类型
    address: 详细地址
    ctry: 国家代码
    county: 行政区划代码
    prvc: 省
    city: 市
    area: 区县
    postcode: 邮编
    exp_dt: 地址的失效日
    is_rp: 是否主地址
    :return:
    """
    ctif_id = infos.get("busi_reg_no")  # 取值
    ctif_tp = ctif_tp_data  # 取值
    address_tp = make_address_tp_data()
    address = infos.get("address")  #
    ctry = infos.get("country")  # 取值
    # county = make_make_province_city_process_data(infos.get("ctid")[:6])  # 已从最新接口文档中移除
    prvc = infos.get("mer_prov")  # 取值
    city = infos.get("mer_city")  # 取值
    area = infos.get("mer_area")[:6]  # 取值
    postcode = ""
    exp_dt = ""
    is_rp = "1"
    print(ctif_id, ctif_tp, address_tp, address, ctry, prvc, city, area, postcode, exp_dt, is_rp)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, address_tp, address, ctry, prvc, city, area, postcode, exp_dt, is_rp
    ])
    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "address_tp": address_tp,
               "address": address,
               "ctry": ctry,
               "prvc": prvc,
               "city": city,
               "area": area,
               "postcode": postcode,
               "exp_dt": exp_dt,
               "is_rp": is_rp
           }, contect_data


# 关系类型数据
def make_rel_tp_data():
    rel_tp = random.choice([
        "A01",  # 对公客户与法人代表
        "A02",  # 对公客户与联系人
        "A03",  # 对公客户与负责人
        "A04",  # 对公客户与董事
        "A05",  # 对公客户与股东
        "A06",  # 母公司与子公司
        "A07",  # 代理
        "A08",  # 投资与被投资
        "A09",  # 其他关联单位
        "A10",  # 企业团体
        "A11",  # 银行团体
        "A12",  # 家族企业
        "B01",  # 夫妻关系
        "B02",  # 子女
        "B03",  # 父母
        "B04",  # 其他血亲
        "B05",  # 其他姻亲
        "B06",  # 同学
        "B07",  # 朋友
        "X",  # 未说明
        "C01"  # 受益所有人
    ])
    return rel_tp


# 客户联系信息表
def make_stan_tel(infos):
    """
    ctif_id:客户号
    ctif_tp:主体类型
    tel_tp:电话类型
    tel:联系电话
    is_rp:是否主电话
    :param infos:
    :return:
    """

    ctif_id = infos.get("busi_reg_no")
    ctif_tp = "1"
    tel_tp = random.choice(["11", "12", "21", "22", "23"])
    tel = make_tel_num()
    is_rp = "1"
    print(ctif_id, ctif_tp, tel_tp, tel, is_rp)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, tel_tp, tel, is_rp
    ])
    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "tel_tp": tel_tp,
               "tel": tel,
               "is_rp": is_rp
           }, contect_data


# 关系人信息表
def make_stan_relation(infos):
    """
    客户关系
    ctif_id: 客户号
    ctif_tp: 主体类型
    rel_tp: 关系类型
    rel_layer: 关系人层级
    rel_ctif: 关系人客户号
    rel_cstp: 关系人类别
    rel_name: 关系人名称
    rcnt: 关系人国籍/国家
    citp: 关系人证件类型
    citp_ori: 关系人证件类型原
    ctid: 关系人证件号码
    citp_nt: 关系人证件类型说
    hold_per: 持股比例
    hold_amt: 持股金额
    ctid_edt: 关系人证件有效期
    rel_prov: 关系人省
    rel_city: 关系人市
    rel_area: 关系人区县
    rear: 关系人详细地址
    retl: 关系人联系电话

    :param infos:
    :return:
    """
    ctif_id = infos.get("busi_reg_no")
    ctif_tp = "1"
    rel_tp = make_rel_tp_data()
    rel_layer = random.choice(["-1", "0", "1", "2", "3", "4", "5"])
    rel_ctif = make_random_num(6)
    rel_cstp = random.choice(["1", "2"])
    rel_name = make_name_data()
    rcnt = "CHE"  # make_country_data()  默认中国
    citp = make_citp_data()
    citp_ori = "证件类型原值"
    ctid = make_IDCard()
    citp_nt = "证件类型说明"
    hold_per = ""  # 持股比例
    hold_amt = ""  # 持股金额
    ctid_edt = make_Card_valid_date(ctid)
    rel_prov = get_province_data(ctid[:6])[:10]
    rel_city = make_province_city_data(ctid[:6])[0][:10]
    rel_area = make_province_city_data(ctid[:6])[-1][:10]
    rear = make_address(ctid[:6])
    retl = make_tel_num()

    print(ctif_id, ctif_tp, rel_tp, rel_layer, rel_ctif, rel_cstp, rel_name, rcnt, citp, citp_ori, ctid, citp_nt,
          hold_per, hold_amt, ctid_edt, rel_prov, rel_city, rel_area, rear, retl)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, rel_tp, rel_layer, rel_ctif, rel_cstp, rel_name, rcnt, citp, citp_ori, ctid, citp_nt,
        hold_per, hold_amt, ctid_edt, rel_prov, rel_city, rel_area, rear, retl
    ])
    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "rel_tp": rel_tp,
               "rel_layer": rel_layer,
               "rel_ctif": rel_ctif,
               "rel_cstp": rel_cstp,
               "rel_name": rel_name,
               "rcnt": rcnt,
               "citp": citp,
               "citp_ori": citp_ori,
               "ctid": ctid,
               "citp_nt": citp_nt,
               "hold_per": hold_per,
               "hold_amt": hold_amt,
               "ctid_edt": ctid_edt,
               "rel_prov": rel_prov,
               "rel_city": rel_city,
               "rel_area": rel_area,
               "rear": rear,
               "retl": retl
           }, contect_data


# 支付账户表
def make_stan_pact(infos):
    """
    ctif_id: 客户号
    ctif_tp: 主体类型
    act_tp: 账户类型
    act_cd: 支付账户号
    act_typ: 账号类别
    act_limit: 支付账户交易限额
    is_self_acc: 是否特约商户收单结算账号
    sales_name: 预付卡办卡人
    cst_sex: 预付卡办卡人性别
    nation: 预付卡办卡人国籍
    occupation: 预付卡办卡人职业
    id_type: 预付卡办卡人证件种类
    id_type_ori: 预付卡办卡人证件种类原值
    id_no: 预付卡办卡人证件号码
    id_deadline: 预付卡办卡人证件有效期截至日
    contact: 预付卡办卡人联系方式
    address: 预付卡办卡人住所地或工作单位地址
    sales_flag: 预付卡代直销标识
    bind_mob: 绑定的手机号码
    mer_unit: 管理机构
    cls_dt: 账户状态
    rgdt: 开户日期
    cls_stat: 销户日期

    :param infos:
    :return:
    """
    if infos.get("busi_type") == "02":
        ctif_id = ""
        ctif_tp = ""
        act_tp = ""
        act_cd = ""
        act_typ = ""
        act_limit = ""
        is_self_acc = ""
        sales_name = ""
        cst_sex = ""
        nation = ""
        occupation = ""
        id_type = ""
        id_type_ori = ""
        id_no = ""
        id_deadline = ""
        contact = ""
        address = ""
        sales_flag = ""
        bind_mob = ""
        mer_unit = ""
        cls_dt = ""
        rgdt = ""
        cls_stat = ""
    else:
        ctif_id = infos.get("busi_reg_no")
        ctif_tp = "1"
        act_tp = random.choice(['11', "211", "212"])
        act_cd = make_act_cd_data(act_tp)
        act_typ = make_act_type_data(act_tp)
        act_limit = make_act_limit_data(act_tp, act_typ)
        is_self_acc = random.choice(["0", "1"])
        sales_name, cst_sex, nation, occupation, id_type, id_type_ori, id_no, id_deadline, contact, address, sales_flag \
            = make_prepaid_card_data(infos)
        bind_mob = make_bind_mob_data(infos)
        mer_unit = make_mer_unit_data()
        cls_dt = make_cls_dt_data(infos.get("busi_reg_no"))
        rgdt = make_register_date()
        if cls_dt == "C":
            cls_stat = make_register_date()
        else:
            cls_stat = ""

    print(ctif_id, ctif_tp, act_tp, act_cd, act_typ, act_limit, is_self_acc, sales_name, "性别：", cst_sex, nation,
          occupation, id_type, id_type_ori, id_no, id_deadline, contact, address, sales_flag, bind_mob, mer_unit,
          cls_dt, rgdt, cls_stat)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, act_tp, act_cd, act_typ, act_limit, is_self_acc, sales_name, cst_sex, nation, occupation,
        id_type, id_type_ori, id_no, id_deadline, contact, address, sales_flag, bind_mob, mer_unit, cls_dt, rgdt,
        cls_stat
    ])

    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "act_tp": act_tp,
               "act_cd": act_cd,
               "act_typ": act_typ,
               "act_limit": act_limit,
               "is_self_acc": is_self_acc,
               "sales_name": sales_name,
               "cst_sex": cst_sex,
               "nation": nation,
               "occupation": occupation,
               "id_type": id_type,
               "id_type_ori": id_type_ori,
               "id_no": id_no,
               "id_deadline": id_deadline,
               "contact": contact,
               "address": address,
               "sales_flag": sales_flag,
               "bind_mob": bind_mob,
               "mer_unit": mer_unit,
               "cls_dt": cls_dt,
               "rgdt": rgdt,
               "cls_stat": cls_stat
           }, contect_data


# 银行账户表
def make_stan_bact(infos, t_stan_pact):
    """
    ctif_id: 客户号
    ctif_tp: 主体类型
    act_tp: 银行账号种类
    act_flag: 银行账号种类-现场检查
    act_cd: 银行账户号
    cabm: 银行账号开户行名称
    pay_id: 关联支付账户
    is_self_acc: 是否特约商户收单结算账号
    bank_acc_name: 银行账户名称
    mer_unit: 管理机构

    :param infos:
    :return:
    """
    ctif_id = infos.get("busi_reg_no")
    ctif_tp = "1"
    act_tp = make_bank_act_tp_data(ctif_tp)
    act_flag = random.choice(["11", "12"])
    act_cd = "62" + make_random_num(17)
    cabm = make_cabm_data(infos.get("ctid")[:6])
    pay_id = make_pay_id_data(infos.get("busi_type"), t_stan_pact.get("act_cd"))
    is_self_acc = t_stan_pact.get("is_self_acc")
    bank_acc_name = ""  # 没明白是什么，暂空
    mer_unit = t_stan_pact.get("mer_unit")
    print(ctif_id, ctif_tp, act_tp, act_flag, act_cd, cabm, pay_id, is_self_acc, bank_acc_name, mer_unit)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, act_tp, act_flag, act_cd, cabm, pay_id, is_self_acc, bank_acc_name, mer_unit
    ])
    return {
               "ctif_id": ctif_id,
               "ctif_tp": ctif_tp,
               "act_tp": act_tp,
               "act_flag": act_flag,
               "act_cd": act_cd,
               "cabm": cabm,
               "pay_id": pay_id,
               "is_self_acc": is_self_acc,
               "bank_acc_name": bank_acc_name,
               "mer_unit": mer_unit
           }, contect_data

# 主体的交易账号种类数据
def make_ctat_data(busi_type):
    if busi_type == "02":
        ctat = ""
    else:
        ctat = random.choice(["01", "02"])
    return ctat

# 主体的交易账号数据
def make_ctac_data(busi_type):
    if busi_type == "02":
        ctac = ""
    else:
        ctac = make_random_num(19)
    return ctac

# 标准交易表
def make_stan_stif(infos, stan_bact, ctif_tp_num):
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
    cbat = stan_bact.get("act_tp")
    cbac = stan_bact.get("act_cd")
    cabm = stan_bact.get("cabm")

    busi_type = make_busi_type_data()

    ctat = make_ctat_data(busi_type)
    ctac = make_random_num(17)
    cpin = "默认机构名称"
    cpba = make_random_num(17)
    cpbn = make_cabm_data(make_province_code_data())
    ctip = make_ip_data(busi_type)
    tstm = make_trade_time_data()
    cttp = make_cttp_data()
    tsdr = random.choice(["01", "02"])
    crpp = "资金用途"
    crtp = "CNY"
    crat = make_trade_amount_data()
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
    mer_prov = get_province_data(province_code[:2])
    mer_area = make_province_city_data(province_code)[-1][:10]  # [:10]作用，数据库字段最大长度为10，县名超过10时，切片取前10

    province_code2 = make_province_code_data()
    pos_prov = get_province_data(province_code2[:2])
    pos_area = make_province_city_data(province_code2)[-1][:10]  # 同上

    mer_unit = make_mer_unit_data()  # 需提供支付系统代码表
    extend1 = ""
    # rate_rmb = ""   # 老接口字段
    # rate_usa = ""  # 老接口字段
    iofg = "0"  # 暂时默认境内交易
    trans_channel = make_trans_channel_data()
    ctmac = make_mac_info_data(busi_type)
    balance = "10000"
    acc_flag = make_acc_flag_data(busi_type)
    ctid_edt = infos.get("ctid_edt")
    tran_flag = make_tran_flag_data(busi_type)

    trans_order = make_trans_order_data(busi_type)
    trans_cst_type = make_trans_cst_type_data()
    crat_u = ""
    crat_c = ""
    trans_way = make_random_str(6)  # 详见交易方式代码表(目前未收到人行的接口文件，暂定6位)
    agency_ctnm = make_name_data()
    agency_citp = make_citp_data()
    agency_ctid = make_IDCard()
    agency_country = "CHN"

    print(ctif_id, ctif_tp, client_tp, smid, ctnm, citp, citp_ori, citp_nt, ctid, cbat, cbac, cabm, ctat, ctac, cpin,
          cpba, cpbn, ctip, tstm, cttp, tsdr, crpp, crtp, crat, tcif_id, tcnm, tsmi, tcit, tcit_ori, tcit_nt, tcid,
          tcat,
          tcba, tcbn, tctt, tcta, tcpn, tcpa, tpbn, tcip, tmnm, bptc, pmtc, ticd, busi_type, trans_type, pos_dev_id,
          trans_stat, bank_stat, mer_prov, mer_area, pos_prov, pos_area, mer_unit, extend1, iofg, trans_channel, ctmac,
          balance, acc_flag, ctid_edt, tran_flag, trans_order, trans_cst_type, crat_u, crat_c, trans_way, agency_ctnm,
          agency_citp, agency_ctid, agency_country)
    contect_data = make_connect_data([
        ctif_id, ctif_tp, client_tp, smid, ctnm, citp, citp_ori, citp_nt, ctid, cbat, cbac, cabm, ctat, ctac, cpin,
        cpba, cpbn, ctip, tstm, cttp, tsdr, crpp, crtp, crat, tcif_id, tcnm, tsmi, tcit, tcit_ori, tcit_nt, tcid, tcat,
        tcba, tcbn, tctt, tcta, tcpn, tcpa, tpbn, tcip, tmnm, bptc, pmtc, ticd, busi_type, trans_type, pos_dev_id,
        trans_stat, bank_stat, mer_prov, mer_area, pos_prov, pos_area, mer_unit, extend1, iofg, trans_channel, ctmac,
        balance, acc_flag, ctid_edt, tran_flag, trans_order, trans_cst_type, crat_u, crat_c, trans_way, agency_ctnm,
        agency_citp, agency_ctid, agency_country
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
               "iofg": iofg,
               "trans_channel": trans_channel,
               "ctmac": ctmac,
               "balance": balance,
               "acc_flag": acc_flag,
               "ctid_edt": ctid_edt,
               "tran_flag": tran_flag,
               "trans_order": trans_order,
               "trans_cst_type": trans_cst_type,
               "crat_u": crat_u,
               "crat_c": crat_c,
               "trans_way": trans_way,
               "agency_ctnm": agency_ctnm,
               "agency_citp": agency_citp,
               "agency_ctid": agency_ctid,
               "agency_country": agency_country
           }, contect_data


def person(num):
    print("个人")
    persion_infos, stan_person_connect = make_stan_persion(num)
    t_stan_cert, stan_cert_connect = make_stan_cert(persion_infos)
    t_stan_address, stan_address_connect = make_stan_address(persion_infos, "1")
    t_stan_tel, stan_tel_connect = make_stan_tel(persion_infos)
    t_stan_pact, stan_pact_connect = make_stan_pact(persion_infos)
    t_stan_bact, stan_bact_connect = make_stan_bact(persion_infos, t_stan_pact)
    t_stan_relation, stan_relation_connect = make_stan_relation(persion_infos)
    # 交易表数据单独写入，一个主体写入10条数据
    for num in range(10):
        t_stan_stif, stan_stif_connect = make_stan_stif(persion_infos, t_stan_bact, '1')
        # data = eval("t_stan_stif"[2:] + "_connect")
        data = stan_stif_connect
        file_name = "t_stan_stif".split("_")[-1] + "_" + file_date_time
        print(stan_stif_connect)
        write_to_csv(file_name + ".csv", data)

    print(stan_person_connect)
    print(stan_cert_connect)
    print(stan_address_connect)
    print(stan_tel_connect)
    print(stan_pact_connect)
    print(stan_bact_connect)
    # print(stan_stif_connect)
    print(stan_relation_connect)
    name = ["t_stan_person", "t_stan_cert", "t_stan_address", "t_stan_tel", "t_stan_relation", "t_stan_pact",
            "t_stan_bact"]
    for file_name in name:
        data = eval(file_name[2:] + "_connect")
        file_name = file_name.split("_")[-1] + "_" + file_date_time
        write_to_csv(file_name + ".csv", data)
        # write_to_csv(file_name + ".txt", data)


def org(num):
    print("机构")
    org_infos, stan_org_connect = make_stan_org(num)
    t_stan_cert, stan_cert_connect = make_stan_cert(org_infos)
    t_stan_address, stan_address_connect = make_stan_address(org_infos, "2")
    t_stan_tel, stan_tel_connect = make_stan_tel(org_infos)
    t_stan_pact, stan_pact_connect = make_stan_pact(org_infos)
    t_stan_bact, stan_bact_connect = make_stan_bact(org_infos, t_stan_pact)
    t_stan_relation, stan_relation_connect = make_stan_relation(org_infos)

    # 交易表数据单独写入，一个主体写入10条数据
    for num in range(10):
        t_stan_stif, stan_stif_connect = make_stan_stif(org_infos, t_stan_bact, '2')

        # data = eval("t_stan_stif"[2:] + "_connect")
        data = stan_stif_connect
        file_name = "t_stan_stif".split("_")[-1] + "_" + file_date_time
        print(stan_stif_connect)

        write_to_csv(file_name + ".csv", data)

    print(stan_org_connect)
    print(stan_cert_connect)
    print(stan_address_connect)
    print(stan_tel_connect)
    print(stan_pact_connect)
    print(stan_bact_connect)
    # print(stan_stif_connect)
    print(stan_relation_connect)
    name = ["t_stan_org", "t_stan_cert", "t_stan_address", "t_stan_tel", "t_stan_relation", "t_stan_pact",
            "t_stan_bact"]
    for file_name in name:
        data = eval(file_name[2:] + "_connect")
        file_name = file_name.split("_")[-1] + "_" + file_date_time
        write_to_csv(file_name + ".csv", data)
        # write_to_csv(file_name + ".txt", data)


# def main(num):
#     person(num)
#     org(num)

def main(begin, end):
    for num in range(begin, end):
        person(num)
        org(num)


if __name__ == "__main__":
    # pinyin = word_to_pinyin("张三")
    # print(pinyin)

    # res = make_IDCard()
    # print(res)

    # res = read_province_data()
    # print(res)

    # add = make_make_province_city_process_data("150722")
    # print(add)

    # address = make_address("230183")
    # print(address)

    # trade_data = make_trade_amount_data()
    # print(trade_data)

    # ticd = make_ticd_data()
    # print(ticd)

    # data = make_make_province_city_process_data(make_province_code_data())
    # make_province_city_data(data)[-1]

    # data2 = make_province_code_data()
    # province = get_province_data(data2[:2])
    # print(province)

    # read_excel()

    # header = "&#@".join(t_stan_tel_header)
    # write_to_csv("t_stan_tel.csv", header)
    # date = time.strftime("%Y-%m-%d", time.localtime())

    # -------------------------多线程
    from threading import Thread
    # make_trade_time_data()
    start_time = time.time()
    # threads = []
    # for count in range(10):
    #     t = Thread(target=main, args=(count*10, (count+1)*10))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()
    # -------------------------单线程
    main(0, 100)
    end_time = time.time()
    print(end_time-start_time)  # 13

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