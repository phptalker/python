# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
from datetime import datetime
from hashlib import md5
import logging
import time
from items import ShixianItem
from items import ProginnItem


class HongPipeline(object):
    def process_item(self, item, spider):
        return item


# class DmozPipeline(object):
#     def __init__(self):
#         self.file = open('items.jl', 'wb')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         return item


class ShixianPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # return
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # d.addBoth(lambda _: item)
        return d
        # return item

    def _do_upinsert(self, conn, item, spider):
        # print linkmd5id
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        conn.execute("""
                select 1 from shixian where uid = %s
        """, (item['uid'],))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update shixian set nick = %s, company = %s, title = %s, workYear = %s, city = %s
                 , kind = %s, techExp = %s, proExp = %s, daySalary = %s , partTime = %s , expLocation = %s , update_time = %s
                 where uid = %s
            """, ( item['nick'], item['company'], item['title'], item['workYear'], item['city'], item['kind'],
                item['techExp'], item['proExp'], item['daySalary'], item['partTime'], item['expLocation'], now ,item['uid'] ))
            # print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into shixian(
                    `uid`,
                    `nick`,
                    `company`,
                    `title`,
                    `workYear`,
                    `city`,
                    `kind`,
                    `techExp`,
                    `proExp`,
                    `daySalary`,
                    `partTime`,
                    `expLocation`,
                    `create_time`
                )
                values(%s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s,%s )
            """, (item['uid'], item['nick'], item['company'], item['title'], item['workYear'], item['city'], item['kind'],
                item['techExp'], item['proExp'], item['daySalary'], item['partTime'], item['expLocation'], now))

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['link']).hexdigest()

    # 异常处理
    def _handle_error(self, failure, item, spider):
        logging.log(logging.ERROR,failure)

class ProginnPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # return
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # d.addBoth(lambda _: item)
        return d
        # return item

    def _do_upinsert(self, conn, item, spider):
        print item
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        conn.execute("""
                select 1 from proginn where uid = %s
        """, (item['uid'],))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update proginn set nick = %s, company = %s, title = %s, workYear = %s, city = %s
                 , kind = %s, techExp = %s, proExp = %s, daySalary = %s , partTime = %s , expLocation = %s, skill = %s ,experience=%s , update_time = %s
                 where uid = %s
            """, ( item['nick'], item['company'], item['title'], item['workYear'], item['city'], item['kind'],
                item['techExp'], item['proExp'], item['daySalary'], item['partTime'], item['expLocation'], item['skill'], item['experience'], now ,item['uid'] ))
            # print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into proginn(
                    `uid`,
                    `nick`,
                    `company`,
                    `title`,
                    `workYear`,
                    `city`,
                    `kind`,
                    `techExp`,
                    `proExp`,
                    `daySalary`,
                    `partTime`,
                    `expLocation`,
                    `skill`,
                    `experience`,
                    `create_time`
                )
                values(%s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s,%s ,%s,%s)
            """, (item['uid'], item['nick'], item['company'], item['title'], item['workYear'], item['city'], item['kind'],
                item['techExp'], item['proExp'], item['daySalary'], item['partTime'], item['expLocation'],item['skill'],item['experience'], now))

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['link']).hexdigest()

    # 异常处理
    def _handle_error(self, failure, item, spider):
        logging.log(logging.ERROR,failure)


class SxsoftPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # return
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # d.addBoth(lambda _: item)
        return d
        # return item

    def _do_upinsert(self, conn, item, spider):
        # print item
        if(item['nick']==''):
            return
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        conn.execute("""
                select 1 from sxsoft where uid = %s
        """, (item['uid'],))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update sxsoft set nick = %s, company = %s, title = %s, workYear = %s, city = %s
                 , kind = %s, techExp = %s, proExp = %s, daySalary = %s , partTime = %s , expLocation = %s, skill = %s ,experience=%s , update_time = %s
                 where uid = %s
            """, ( item['nick'], item['company'], item['title'], item['workYear'], item['city'], item['kind'],
                item['techExp'], item['proExp'], item['daySalary'], item['partTime'], item['expLocation'], item['skill'], item['experience'], now ,item['uid'] ))
            # print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into sxsoft(
                    `uid`,
                    `nick`,
                    `company`,
                    `title`,
                    `workYear`,
                    `city`,
                    `kind`,
                    `techExp`,
                    `proExp`,
                    `daySalary`,
                    `partTime`,
                    `expLocation`,
                    `skill`,
                    `experience`,
                    `create_time`
                )
                values(%s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s,%s ,%s,%s)
            """, (item['uid'], item['nick'], item['company'], item['title'], item['workYear'], item['city'], item['kind'],
                item['techExp'], item['proExp'], item['daySalary'], item['partTime'], item['expLocation'],item['skill'],item['experience'], now))

    # 获取url的md5编码
    def _get_linkmd5id(self, item):
        # url进行md5处理，为避免重复采集设计
        return md5(item['link']).hexdigest()

    # 异常处理
    def _handle_error(self, failure, item, spider):
        logging.log(logging.ERROR,failure)



class ZbjPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # return
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # d.addBoth(lambda _: item)
        return d
        # return item

    def _do_upinsert(self, conn, item, spider):
        print item
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        conn.execute("""
                select 1 from zbj where url = %s
        """, (item['url'],))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                update zbj set  company = %s, service = %s, location = %s, tel = %s
                 , detail = %s, update_time = %s,isCompany=%s,mobile=%s
                 where url = %s
            """, (  item['company'], item['service'], item['location'], item['tel'], item['detail'], now , item['isCompany'] , item['mobile']  ,item['url'] ))
            # print """
            #    update cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (item['title'], item['desc'], item['link'], item['listUrl'], now, linkmd5id)
        else:
            conn.execute("""
                insert into zbj(
                    `url`,
                    `company`,
                    `service`,
                    `location`,
                    `tel`,
                    `isCompany`,
                    `mobile`,
                    `detail`,
                    `create_time`
                )
                values(%s, %s, %s, %s, %s , %s, %s)
            """, (item['url'], item['company'], item['service'], item['location'], item['tel'], item['isCompany'], item['mobile'], item['detail'], now))

    # 异常处理
    def _handle_error(self, failure, item, spider):
        logging.log(logging.ERROR,failure)
