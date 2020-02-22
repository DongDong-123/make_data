import sys
from collections import Counter

# 读取文件
def read_txt(file):
    with open(file, 'r', encoding="utf-8")as f:
        file_contant = f.readlines()
    return file_contant


# 对比
def compare(file_name):
    if isinstance(file_name, str):
        contant = read_txt(file_name)
    elif isinstance(file_name, list):
        contant = []
        for txt in file_name:
            if txt[-4:] != ".txt":
                raise TypeError("文件格式不是TXT文件！")
            else:
                contant.extend(read_txt(txt))
    else:
        raise TypeError("类型错误！")
    line_list = []
    # print(contant)
    for line in contant:
        line = line.splitlines(keepends=False)[0]
        line = line.strip()
        if line:
            line_list.append(line)
    # print(line_list)
    print("文件总数:", len(line_list))

    line_set = set(line_list)
    if len(line_list) == len(line_set):
        print("没有重复")
    else:
        print("有重复文件！")
        line_list_2 = list(line_set)
        for line2 in line_list_2:
            line_list.remove(line2)

        print("重复文件{}个：".format(len(line_list)), line_list)
        # count = Counter(line_list)
        # print("未重复文件：", )


# txt = open("temp.txt", 'r')
# print(txt)


if __name__ == "__main__":
    parm = sys.argv[1:]
    print("上线文件", u'{}'.format(parm))
    if parm:
        compare(parm)
    else:
        raise FileNotFoundError("没有文件！")

