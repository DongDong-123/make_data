import requests
import json


def get_names():
    """
    万人奥运名单
    :return:
    """
    url = "https://www.cnrunners.com/tlist/getList.do"
    data = {
        "pageSize": 50,
        "pageNumber": 600,
        "qType": "男",
        "gType": 0
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        # "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "Connection": "keep-alive",
        # "Content-Length": "49",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID=D6A999B78FE336CF16A552D7D059EBB6; UM_distinctid=16f421a7ff23e6-0bd0b332140afb-7711a3e-144000-16f421a7ff3331; CNZZDATA1276378882=1188976902-1577359975-%7C1577359975",
        "Host": "www.cnrunners.com",
        "Origin": "https://www.cnrunners.com",
        "Referer": "https://www.cnrunners.com/runners/pages/projects/runnerList.jsp",
        # "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Site": "same-origin",
        # "X-Requested-With": "XMLHttpRequest"
    }
    data = json.dumps(data)

    res = requests.post(url, data, headers=header)
    print(res.text)



get_names()