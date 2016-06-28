# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入smtplib和MIMEText
import smtplib
from email.mime.text import MIMEText
import conf
import time
import MySQLdb

#############
# 要发给谁，这里发给2个人
mailto_list = ["wangxianghong@looip.cn",'yvonneyang@looip.cn']
#####################
# 设置服务器，用户名、口令以及邮箱的后缀
mail_host = "smtp.sina.com"
mail_user = "hong1070"
mail_pass = "hong97850014"
mail_postfix = "sina.com"


def conndb():
    return MySQLdb.connect(host=conf.mysql_host, user=conf.mysql_user, passwd=conf.mysql_pwd, db=conf.mysql_db,
                           port=int(conf.mysql_port))


######################
def send_mail(to_list, sub, content):
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    # if send_mail(mailto_list, "老板需求审核提醒邮件", "老板需求审核提醒邮件"):
    # print "发送成功"
    # else:
    # print "发送失败"

    conn = conndb()
    cursor = conn.cursor()

    try:
        cursor.execute('set names utf8')
        selectSql = "select demand_id,title,demand_desc  from project_demand  where verify_status = 'send'  order by demand_id desc limit 0,1"

        res = cursor.execute(selectSql)

        if (True != res):
            print("没有新的纪录需要审核")
        else:
            result = cursor.fetchone();
            print(result)
            if send_mail(mailto_list, "老板需求审核提醒邮件",'\n一句话:'+result[1]+'\n 自我描述:'+ result[2]):
                print "发送成功"
            else:
                print "发送失败"
        conn.commit()
    except Exception, e:
        print e

    cursor.close()
    conn.close()
