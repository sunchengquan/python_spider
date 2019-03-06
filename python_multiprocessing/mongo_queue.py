#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/11/15:44'

import sys
import traceback
from datetime import datetime, timedelta
from pymongo import MongoClient, errors


MONGODB_CONFIG = {
    'host': '188.131.173.150',
    'port': 27017,
    'db': 'test',
    'collection':'crawl_queue',
    'username': 'sunchengquan',
    'password': 'scq123456'
}


class MongoQueue():

    OUTSTANDING = 1  ##初始状态
    PROCESSING = 2  ##正在下载状态
    COMPLETE = 3  ##下载完成状态

    def __init__(self,collection, timeout=600):
        """
        初始mongodb连接
        :param collection:表名
        :param timeout:
        """
        try:
            self.conn = MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db']]
            self.username = MONGODB_CONFIG['username']
            self.password = MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True

            self.collection = self.db[collection]
            self.timeout = timeout
        except Exception:
            print(traceback.format_exc())
            print('Connect Statics Database Fail.')
            sys.exit(1)

    def __bool__(self):
        """
        这个函数，我的理解是如果下面的表达为真，则整个类为真
        至于有什么用，后面我会注明的（如果我的理解有误，请指点出来谢谢，我也是Python新手）
        $ne的意思是不匹配
        """
        record = self.collection.find_one(
            {'status': {'$ne': self.COMPLETE}}
        )
        return True if record else False

    def push(self, url, title):
        """
        添加新的URL进队列
        :param url:地址
        :param title:主题
        :return:none
        """
        try:
            self.collection.insert({'_id': url, 'status': self.OUTSTANDING, '主题': title})
            print(url, '插入队列成功')
        except errors.DuplicateKeyError:
            ##报错则代表已经存在于队列之中了
            print(url, '已经存在于队列中了')
            pass

    def push_imgurl(self, title, url):
        try:
            self.collection.insert({'_id': title, 'statue': self.OUTSTANDING, 'url': url})
            print('图片地址插入成功')
        except errors.DuplicateKeyError:
            print('地址已经存在了')
            pass

    def pop_title(self, url):
        record = self.collection.find_one({'_id': url})
        return record['主题']

    def pop(self):
        """
        这个函数会查询队列中的所有状态为OUTSTANDING的值，
        更改状态，（query后面是查询）（update后面是更新）
        并返回_id（就是我们的ＵＲＬ），MongDB好使吧，^_^
        如果没有OUTSTANDING的值则调用repair()函数重置所有超时的状态为OUTSTANDING，
        $set是设置的意思，和MySQL的set语法一个意思
        """
        record = self.collection.find_and_modify(
            query={'status': self.OUTSTANDING},
            update={'$set': {'status': self.PROCESSING, 'timestamp': datetime.now()}}
        )
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError

    def peek(self):
        """
        取出状态为 OUTSTANDING的文档并返回_id(URL)
        """
        record = self.collection.find_one({'status': self.OUTSTANDING})
        if record:
            return record['_id']

    def repair(self):
        """
        重置状态
        $lt “<”
        $lte “<=”
        $ne “!=”

        """
        record = self.collection.find_and_modify(
            query={
                'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                'status': {'$ne': self.COMPLETE}
            },
            update={'$set': {'status': self.OUTSTANDING}}
        )
        if record:
            print('重置URL状态', record['_id'])



    def complete(self, url):
        """
        更新已成功爬去的的URL的状态为：COMPLETE
        """
        self.collection.update({'_id': url}, {'$set': {'status': self.COMPLETE}})
    def clear(self):
        """
        这个函数只有第一次才调用、后续不要调用、因为这是删库啊！
        """
        self.collection.drop()

if __name__ == "__main__":
    MongoQueue('crawl').push('https://cuiqingcai.com', '博客')