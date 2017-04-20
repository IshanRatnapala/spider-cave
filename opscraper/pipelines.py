# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3 as sq

class OpscraperPipeline(object):

    def open_spider(self, spider):
        self.setupDBCon()
        self.setupDB()

    def close_spider(self, spider):
        self.closeDB()

    def process_item(self, item, spider):
        self.storeInDB(item)
        return item

    def setupDBCon(self):
        self.con = sq.connect('test.db')
        self.cur = self.con.cursor()

    def closeDB(self):
        self.con.close()

    def setupDB(self):
        self.dropTables()
        self.createTables()

    def dropTables(self):
        self.cur.execute("DROP TABLE IF EXISTS Country")
        self.cur.execute("DROP TABLE IF EXISTS Postcode")

    def createTables(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Country ( \
        countryCode1 VARCHAR(2) PRIMARY KEY NOT NULL, \
        countryCode2 VARCHAR(3), \
        countryName TEXT, \
        countryCapital TEXT, \
        countryArea TEXT, \
        countryPopulation TEXT, \
        continent TEXT, \
        postcodeTranslation TEXT \
        )")

        self.cur.execute("CREATE TABLE IF NOT EXISTS Postcode ( \
        countryCode1 VARCHAR(2) PRIMARY KEY NOT NULL, \
        postcode TEXT, \
        countryName TEXT, \
        address1 TEXT, \
        address2 TEXT, \
        address3 TEXT, \
        latitude TEXT, \
        longitude TEXT \
        )")

    def storeInDB(self, item):
        self.storeCountryInDB(item)
        self.storePostcodeInDB(item)

    def storeCountryInDB(self, item):
        country = [
            item['country'].get('countryCode1', ''),
            item['country'].get('countryName', ''),
            item['country'].get('countryCode2', ''),
            item['country'].get('countryCapital', ''),
            item['country'].get('countryArea', ''),
            item['country'].get('countryPopulation', ''),
            item['country'].get('continent', ''),
            item['country'].get('postcodeTranslation', '')
        ]

        self.cur.execute("INSERT INTO Country VALUES (?, ?, ?, ?, ?, ?, ?, ? )", country)
        self.con.commit()

    def storePostcodeInDB(self, item):
        postcode = [
            item['country'].get('countryCode1', ''),
            item['postcode'].get('postcode', ''),
            item['postcode'].get('areaname', ''),
            item['postcode'].get('address1', ''),
            item['postcode'].get('address2', ''),
            item['postcode'].get('address3', ''),
            item['postcode'].get('latitude', ''),
            item['postcode'].get('longitude', '')
        ]
        self.cur.execute("INSERT INTO Postcode VALUES (?, ?, ?, ?, ?, ?, ?, ? )", postcode)
        self.con.commit()

