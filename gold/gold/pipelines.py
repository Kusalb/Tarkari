# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class GoldPipeline(object):
    def process_item(self, item, spider):
        return item

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
        self.curr.execute("""DROP TABLE IF EXISTS g_list""")
        self.curr.execute("""create table g_list(product text, weight text, price text, datee text)""")


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        for index, elem in enumerate(item['product']):
            print(item['datee'])
            self.curr.execute("""insert into g_list(product,weight,price,datee) values (%s,%s,%s,%s)""", (
                item['product'][index],
                item['weight'][index],
                item['price'][index],
                item['datee'],
            ))
        self.conn.commit()

