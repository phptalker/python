#coding=utf-8
#!/usr/bin/python
#filename: conf.py
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import datetime

#####################
# 设置服务器，用户名、口令以及邮箱的后缀
mail_host = "smtp.exmail.qq.com"
mail_user = "geeksoho@looip.cn"
mail_pass = "112233Asdf"
mail_postfix = "looip.cn"

######################
def send_mail(to_list, sub, content):
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, 'html', 'utf-8')
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


d = datetime.datetime.now()

def day_get(d):

   oneday = datetime.timedelta(days = 1 )

   day = d - oneday

   date_from = datetime.datetime(day.year, day.month, day.day, 0 , 0 , 0 ).strftime("%Y-%m-%d")

   #date_to = datetime.datetime(day.year, day.month, day.day, 23 , 59 , 59 )

   return  str (date_from)

def week_get(d):

   dayscount = datetime.timedelta(days = d.isoweekday())

   dayto = d - dayscount

   sixdays = datetime.timedelta(days = 6 )

   dayfrom = dayto - sixdays

   date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0 , 0 , 0 ).strftime("%Y-%m-%d")

   date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23 , 59 , 59 ).strftime("%Y-%m-%d")

   return [ str (date_from), str (date_to)]

def month_get(d):

   dayscount = datetime.timedelta(days = d.day)

   dayto = d - dayscount

   date_from = datetime.datetime(dayto.year, dayto.month, 1 , 0 , 0 , 0 ).strftime("%Y-%m-%d")

   date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23 , 59 , 59 ).strftime("%Y-%m-%d")

   return [ str (date_from), str (date_to)]

#day_get(d)