 # -*- coding: utf-8 -*-
import conf
import time
import MySQLdb

def conndb():
    return MySQLdb.connect(host = conf.mysql_host, user = conf.mysql_user, passwd = conf.mysql_pwd, db = conf.mysql_db, port = int(conf.mysql_port))

def addOrUpdateProject(name,source,keyword,description,projectDetail,price,searchkey,projectId,publishtime,detailUrl,status = 0):
    conn = conndb()
    cursor = conn.cursor()

    try:
        cursor.execute('set names utf8')
        selectSql  = "select id from projects where source = '%s' and projectId = %s limit 0,1"

        res = cursor.execute(selectSql,(source,projectId))

        if(True != res):
            sql = "insert into projects(name,source,keyword,description,projectDetail,price,searchkey,projectId,intime,publishtime,detailUrl,status) " \
                  " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s)"

            currtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            param = (name,source,keyword,description,projectDetail,price,searchkey,projectId , currtime,publishtime,detailUrl,status)
            n = cursor.execute(sql,param)
            print("新增记录成功: %s" % cursor.lastrowid)
        else:
            data = cursor.fetchone()
            sql = "update projects set name =%s,keyword =%s,description =%s,projectDetail =%s" \
                  ",price =%s ,searchkey =%s,publishtime =%s ,detailUrl = %s  ,status = %s ,lastupdatetime = %s" \
                  " where source = %s and projectId = %s "
            currtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            param =  (name,keyword,description,projectDetail,price,searchkey , publishtime,detailUrl ,status ,currtime, source,projectId)

            n = cursor.execute(sql,param)
            print("更新记录成功,ID: %s" % data[0])

        conn.commit()
    except Exception, e:
        print e

    cursor.close()
    conn.close()


def addOrUpdateCostomer(robot_page,company_name,robot_key,contact,contact_title,tel,mobile,fax,address,post_code,website ):
    conn = conndb()
    cursor = conn.cursor()

    try:
        cursor.execute('set names utf8')
        selectSql  = "select id from costomer where robot_page = %s and company_name = %s limit 0,1"

        res = cursor.execute(selectSql,(robot_page,company_name))

        if(True != res):
            sql = "insert into costomer(robot_page,company_name,robot_key,contact,contact_title,tel,mobile,fax,address,post_code,website,create_time) " \
                  " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            currtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            param = (robot_page,company_name,robot_key,contact,contact_title,tel,mobile,fax,address,post_code,website,currtime)
            n = cursor.execute(sql,param)
            print("新增记录成功: %s" % cursor.lastrowid)
        else:
            data = cursor.fetchone()
            sql = "update costomer set contact =%s,contact_title =%s,tel =%s,mobile =%s" \
                  ",fax =%s ,address =%s,post_code =%s ,website = %s,update_time = %s " \
                  " where robot_page = %s and company_name = %s "
            currtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            param =  (contact,contact_title,tel,mobile,fax,address,post_code,website,currtime,robot_page,company_name)

            n = cursor.execute(sql,param)
            print("更新记录成功,ID: %s" % data[0])

        conn.commit()
    except Exception, e:
        print e

    cursor.close()
    conn.close()
