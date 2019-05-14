# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class TarkariPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        print('here')
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='tarkari'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS t_list""")
        self.curr.execute("""create table t_list(name text, unit text, maximum text, minimum text, average text COLLATE utf8_unicode_ci NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        print('here')
        for index, elem in enumerate(item['name']):
            self.curr.execute("""insert into t_list(name,unit,minimum,maximum,average) values (%s,%s,%s,%s,%s)""", (
                item['name'][index],
                item['unit'][index],
                item['minimum'][index],
                item['maximum'][index],
                item['average'][index],
            ))
        self.conn.commit()

