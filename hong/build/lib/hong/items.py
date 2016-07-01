# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class HongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = Field()
    link = Field()
    desc = Field()


class ShixianItem(scrapy.Item):
    uid = Field()
    nick = Field()
    company = Field()
    title = Field()
    workYear = Field()
    city = Field()
    kind = Field()
    techExp = Field()
    proExp = Field()
    daySalary = Field()
    partTime = Field()
    expLocation = Field()

class ProginnItem(scrapy.Item):
    uid = Field()
    nick = Field()
    company = Field()
    title = Field()
    workYear = Field()
    city = Field()
    kind = Field()
    techExp = Field()
    proExp = Field()
    daySalary = Field()
    partTime = Field()
    expLocation = Field()
    skill = Field()
    experience = Field()
class SxsoftItem(scrapy.Item):
    uid = Field()
    nick = Field()
    company = Field()
    title = Field()
    workYear = Field()
    city = Field()
    kind = Field()
    techExp = Field()
    proExp = Field()
    daySalary = Field()
    partTime = Field()
    expLocation = Field()
    skill = Field()
    experience = Field()

class ZbjItem(scrapy.Item):
    url = Field()
    company = Field()
    service = Field()
    location = Field()
    mobile = Field()
    tel = Field()
    detail = Field()
    isCompany = Field()
