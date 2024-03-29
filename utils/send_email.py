# -*- coding: utf-8 -*-
# @ProjectName：Python_InterfaceAutoTest
# @Author: dudu.zhang
# @File: send_email.py
# @Time: 2019-08-18 15:23

import smtplib
from email.mime.text import MIMEText

class SendEmail:

    global send_user
    global email_host
    global password
    send_user = "13501331103@163.com"
    email_host = "smtp.163.com"
    password = 'zhang511520'

    def send_mail(self,user_list,sub,content):
        user = '13501331103'+'<'+send_user+'>'
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)

        user_list = ['807306906@qq.com']
        sub = '接口自动化测试报告'
        content = "此次一共运行接口个数为%s个,通过个数为%s个,失败个数为%s个,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    send = SendEmail()
    # user_list = ['807306906@qq.com']
    # sub = '这个是测试邮件'
    # content = "这个是我们的第一封测试邮件"

    send.send_main([1,2,3,4],[2,3,4,5,6,7])

