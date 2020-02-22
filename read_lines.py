import os
path = os.getcwd()
new_path = os.path.join(path, "4.0")
# fname = 'D:\\data\\4.0\\person_2020-01-10.csv'
# per_12701_1999
file2 = 'person_2020-01-08.csv'
fname = os.path.join(new_path, file2)
# per_6269_999
# with open(fname, 'rb') as f:  # 打开文件
# # 在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始,只能seek(offset,0)
#     first_line = f.readline()  # 取第一行
#     offset = -500  # 设置偏移量
#
#     n = 0
#
#     while True:
#         n += 1
#         # if n > 100:
#         #     break
#         """
#         file.seek(off, whence=0)：从文件中移动off个操作标记（文件指针），正往结束方向移动，负往开始方向移动。
#         如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
#         """
#         f.seek(offset, 2)  # seek(offset, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
#         lines = f.readlines()  # 读取文件指针范围内所有行
#         if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
#             last_line = lines[-2]  # 取最后一行
#             break
#         # 如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
#         # 所以off翻倍重新运行，直到readlines不止一行
#         offset *= 2
#     print('文件' + fname + '第一行为：' + first_line.decode())
#     print('文件' + fname + '最后一行为：' + last_line.decode())
#


with open(fname, 'rb') as f:  # 打开文件
    for i in range(5):

        line = f.readline()
        print('文件' + fname + '第一行为：' + line.decode() + "\n")

# per_2310_0
# per_10936_0