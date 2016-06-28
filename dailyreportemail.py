 # -*- coding: utf-8 -*-import confimport MySQLdbimport datetimeimport tracebackimport util############## 要发给谁，这里发给2个人mailto_list =   ["gaokani@looip.cn","wangxianghong@looip.cn","sunjun@looip.cn","sunming@looip.cn","niuyijing@looip.cn","shihao@looip.cn","zhangyansha@looip.cn","hanmj@looip.cn","max@looip.cn","zhangxibin@looip.cn","jinxin@looip.cn","shixq@looip.cn","robert@looip.cn","gongzl@looip.cn","lihuaqing@looip.cn","wendywang@looip.cn"]#mailto_list =   ["wangxianghong@looip.cn"]def conndb():    return MySQLdb.connect(host=conf.mysql_host, user=conf.mysql_user, passwd=conf.mysql_pwd, db=conf.mysql_db,                           port=int(conf.mysql_port))def checkData():    conn = conndb()    cursor = conn.cursor()    try:        cursor.execute('set names utf8')        today = datetime.date.today()        yesterday =  today - datetime.timedelta(days=1)        yesterday = yesterday.strftime("%Y-%m-%d")        #yesterday = "2016-03-15"        regTotalSql = "select count(user_id) from user limit 0,1" ;        applySingleSql = "select count(*) from programmer_profile limit 0,1" ;        orderSingleSql = "select count(*) from ec_order where type='geek' limit 0,1" ;        orderMountSingleSql = "select sum(amount) from ec_order where type='geek' and status in ('paid','done','refund') limit 0,1" ;        applyTeamSql = "select count(*) from team_apply limit 0,1" ;        orderTeamSql = "select count(*) from ec_order where type='team' limit 0,1" ;        orderMountTeamSql = "select sum(amount) from ec_order where type='team' and status in ('paid','done','refund') limit 0,1" ;        lastDaySql = "select userNum,single_apply_time,single_order_time,single_payment_mount,team_apply_time,team_order_time,team_payment_mount from daily_report where date = %s";        cursor.execute(regTotalSql);        regTotalData = cursor.fetchone();        cursor.execute(applySingleSql);        applySingleData = cursor.fetchone();        cursor.execute(orderSingleSql);        orderSingleData = cursor.fetchone();        cursor.execute(orderMountSingleSql);        orderMountSingleData = cursor.fetchone();        cursor.execute(applyTeamSql);        applyTeamData = cursor.fetchone();        cursor.execute(orderTeamSql);        orderTeamData = cursor.fetchone();        cursor.execute(orderMountTeamSql);        orderMountTeamData = cursor.fetchone();        cursor.execute(lastDaySql,yesterday);        lastDayData = cursor.fetchone();        emailContent = yesterday +"日极客邦平台数据报告如下：\n"        emailContent += "&nbsp</br>"        emailContent += '<table border ="1" ><th colspan ="2" >&nbsp;</th><th>截止到昨日总数</th><th>昨日新增</th>';        if(regTotalData != None):            emailContent += "<tr><td colspan ='2'>注册总数</td><td> %d " % regTotalData[0] +"</td><td>%d " % ( 0 if (lastDayData[0] ==None) else lastDayData[0]) +"</td></tr>"        if(lastDayData != None):            emailContent += "<tr><td rowspan='3' >极客</td><td>申请数</td><td>%d " % applySingleData[0] +"</td><td>%d " % ( 0 if (lastDayData[1] ==None) else lastDayData[1]) +"</td></tr>"            emailContent += "<tr><td>订单数(邀约发起数)</td><td>%d " % orderSingleData[0] +"</td><td>%d " % ( 0 if (lastDayData[2] ==None) else lastDayData[2]) +"</td></tr>"            emailContent += "<tr><td>托管金额</td><td>%s " % orderMountSingleData[0] +"</td><td>%s " % ( 0 if (lastDayData[3] ==None) else lastDayData[3]) +"</td></tr>"            emailContent += "<tr><td rowspan='3' >团队</td><td>申请数</td><td>%d " % applyTeamData[0] +"</td><td>%d " % ( 0 if (lastDayData[4] ==None) else lastDayData[4]) +"</td></tr>"            emailContent += "<tr><td>订单数</td><td>%d " % orderTeamData[0] +"</td><td>%d " % ( 0 if (lastDayData[5] ==None) else lastDayData[5]) +"</td></tr>"            emailContent += "<tr><td>托管金额</td><td>%s " % orderMountTeamData[0] +"</td><td>%s " % ( 0 if (lastDayData[6] ==None) else lastDayData[6]) +"</td></tr>"            emailContent +='</table>'            emailContent += "&nbsp</br>"            emailContent += "每日记录详情可登录运营后台 http://system.looip.cn/mcc 查看数据统计栏目"            util.send_mail(mailto_list , '[极客邦SOHO] 数据报告-日报'+yesterday ,emailContent )        conn.commit()    except Exception, e:        #send_mail(mailto_list , '[极客邦SOHO] 数据库更新日报'+yesterday.strftime("%Y-%m-%d") ,'监测程序出错 %s' % cursor._last_executed + e.message )        print e        print traceback.format_exc()    cursor.close()    conn.close()#checkData()util.send_mail(mailto_list , '[极客邦SOHO] 数据报告-日报' ,"内容" )