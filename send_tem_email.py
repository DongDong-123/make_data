import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import xlwt
import time
import random
import xlrd
from xlutils.copy import copy
import time


# 添加图片
def add_img(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())  # 创建邮件图片对象
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


def send_mail(sub):
    # 定义目的地邮箱
    mailto_list = [
        # '1074373992@qq.com',
        'zisehaiyang05@sina.com',
        'operation@agilecentury.com'
    ]

    me = 'liudongyang@agilecentury.com'
    mail_host = 'smtp.mxhichina.com'
    # 邮件服务器登陆信息
    mail_user = 'liudongyang@agilecentury.com'
    mail_pass = 'Jrsj2019'

    msg = MIMEMultipart()  # 文本内容消息
    html = """
    <style class="fox_global_style"> div.fox_html_content { line-height: 1.5;} /* 一些默认样式 */ blockquote { margin-Top: 0px; margin-Bottom: 0px; margin-Left: 0.5em } ol, ul { margin-Top: 0px; margin-Bottom: 0px; list-style-position: inside; } p { margin-Top: 0px; margin-Bottom: 0px } </style> <div><span id="_FoxCURSOR"></span><br></div> <div><br></div><hr id="FMSigSeperator" style="width: 210px; height: 1px;" color="#b5c4df" size="1" align="left"> <div><span id="_FoxFROMNAME"><div style="MARGIN: 10px; FONT-FAMILY: verdana; FONT-SIZE: 10pt"><div style="font-family: 'Microsoft YaHei UI'; font-size: 14px; line-height: 21px;"><font face="Microsoft YaHei UI, sans-serif">刘冬洋</font><span style="color: rgb(0, 0, 0); font-family: verdana; font-size: 13.3333px; background-color: rgba(0, 0, 0, 0);">&nbsp;</span></div><div style="font-size: 10pt;"><p class="MsoNormal" style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 宋体; line-height: 15.75pt;"><span lang="EN-US" style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">===================================<o:p></o:p></span></p><p class="MsoNormal" style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 宋体; line-height: 15.75pt;"><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">北京捷软世纪信息技术有限公司<span lang="EN-US"><o:p></o:p></span></span></p><p class="MsoNormal" style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 宋体; line-height: 15.75pt;"><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">通讯地址：北京市海淀区上地信息路</span><span lang="EN-US" style="font-size: 10.5pt;">1</span><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">号</span><span lang="EN-US" style="font-size: 10.5pt;">A</span><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">栋</span><span lang="EN-US" style="font-size: 10.5pt;">201</span><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">室（<span lang="EN-US">100085</span>）<span lang="EN-US"><o:p></o:p></span></span></p><p class="MsoNormal" style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 宋体; line-height: 15.75pt;"><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif;">手机：<span lang="EN-US">16619923387<o:p></o:p></span></span></p><p class="MsoNormal" style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 宋体; line-height: 15.75pt;"><span style="font-size: 10.5pt; font-family: 'Microsoft YaHei UI', sans-serif; background-image: initial; background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: initial; background-repeat: initial;">网址：<span lang="EN-US"><a href="http://www.agilecentury.com/" style="text-decoration: none !important; color: rgb(149, 79, 114);">www.agilecentury.com</a></span></span></p></div></div></span></div>
    """

    mimetext = MIMEText(html, "html", 'utf-8')

    # 添加附加信息
    msg.attach(mimetext)
    # msg.attach(add_img('img/bytes_io.png','io'))
    # msg.attach(add_img('img/myisam_key_hit.png','key_hit'))
    # msg.attach(add_img('img/os_mem.png','mem'))
    # msg.attach(add_img('img/os_swap.png','swap'))

    # 添加文件对象
    filename = u'捷软世纪员工测温登记表.xls'
    attach1 = MIMEApplication(open(filename, 'rb').read())
    # attach1['Content-Type'] = 'application/octect-stream'
    attach1.add_header("Content-Disposition", 'attachment', filename=('gbk', '', filename))
    # attach1["Content-Disposition"]= 'attachment'

    msg.attach(attach1)

    # content 发送邮件的内容
    # msg = MIMEText(content)
    msg['Subject'] = sub  # 邮件标题
    msg['From'] = me  # 从哪发
    msg['To'] = ';'.join(mailto_list)  # 发到哪

    # 连接邮件服务器
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)
        s.connect(mail_host)  # 连接邮件服务器

        # 邮件调试信息
        # s.set_debuglevel(1)

        # 登陆操作
        s.login(mail_user, mail_pass)

        # 发送邮件
        s.sendmail(me, mailto_list, msg.as_string())

        # 断开连接
        s.close()

        print('邮件发送成功')

    except Exception as e:
        print(e)
        print('发送失败')

# 写excel
def write_excel():
    time2 = time.strftime("%Y-%m-%d {}:{}".format('18', random.choice(['10', '12', '14', '17'])), time.localtime())
    time1 = time.strftime("%Y-%m-%d {}:{}".format('09', random.choice(['11', '12', '15', '18'])), time.localtime())
    temp1 = random.choice(['36.7', '36.8', '36.5'])
    temp2 = random.choice(['36.7', '36.8', '36.5'])
    value = [[1, '刘冬洋', '未离京', time1, temp1, '否', '否', '否'], [2, '刘冬洋', '未离京', time2, temp2, '否', '否', '否']]
    workbook = xlrd.open_workbook(u'捷软世纪员工测温登记表.xls', formatting_info=True)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    old_data = worksheet.ncols
    print(old_data)
    # 添加边框
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    styleS = xlwt.XFStyle()
    styleS.borders = borders
    # 居中
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    styleS.alignment = alignment
    # 创建新对象，写入数据
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)

    for i in range(0, 2):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + 2, j, value[i][j], styleS)
    # 覆盖保存旧文件
    new_workbook.save(u'捷软世纪员工测温登记表.xls')


if __name__ == '__main__':
    write_excel()
    time.sleep(0.5)
    send_mail('体温测量')
