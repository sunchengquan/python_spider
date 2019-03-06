#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/11/17:16'

import re
import os
import time
import requests
import threading
import multiprocessing
from bs4 import BeautifulSoup
from proxypool.utils import get_page
from mongo_queue import MongoQueue
from proxypool.db_mongo import MongoClient



def url_to_mongoqueue(url):
    """
    把URL写入MongoDB的队列了
    """
    crawl_queue = MongoQueue('crawl_queue')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    all_a = soup.find('div', class_='all').find_all('a')
    for a in all_a:
        title = a.get_text()
        url = a['href']
        print(title)
        print(url)
        crawl_queue.push(url, title)


class Mzitu_crawler():
    current_dir = 'E:\sunchengquan\PycharmProjects\mzitu' #os.path.dirname(__file__)
    crawl_queue = MongoQueue('crawl_queue')
    img_queue = MongoQueue('img_queue')
    max_threads = 16
    sleep_time = 1
    def url_open(self, url,headers={}):
        """使用代理IP打开链接"""

        response = ""
        while response == "":
            try:
                print("代理ip:", self.proxy)
                response = get_page(url, proxies=self.proxy, timeout=30, options=headers)
                return response
            except:
                self.proxy = MongoClient().random()
                continue

    def pageurl_crawler(self,lock):
        while 1:
            try:
                url = self.crawl_queue.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            else:
                img_urls = {}
                title = self.crawl_queue.pop_title(url)
                title= re.sub('[？，。；：、,.;:?!！·]', '', title)
                self.mkdir(title)
                response =requests.get(url)
                web_title = BeautifulSoup(response.text, 'lxml').find('title').get_text()
                if '妹子图' in web_title:
                    max_span = BeautifulSoup(response.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
                    lock.acquire()
                    path = self.current_dir +'\\'+ title
                    for page in range(1, int(max_span) + 1):
                        page_url = url + '/' + str(page)
                        img_url = BeautifulSoup(requests.get(page_url).text, 'lxml').find('div', class_='main-image').find('img')['src']
                        img_urls[img_url] = page_url
                        self.save(img_url,page_url,path)
                    self.crawl_queue.complete(url)
                    self.img_queue.push_imgurl(title, img_urls)
                    lock.release()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join(self.current_dir, path))
        if not isExists:
            print('建了一个名字叫做', path, '的文件夹')
            os.makedirs(os.path.join(self.current_dir, path))
            return True
        else:
            print('名字叫做', path, '的文件夹已经存在了')
            return False

    def save(self, img_url,page_url ,path):
        name = img_url[-9:-4]
        print('开始保存：', img_url)
        header = {'Referer':page_url}
        img = self.url_open(img_url,headers=header)
        content = img.content
        time.sleep(0.5)
        f = open(path +'\\'+name + '.jpg', 'wb')
        f.write(content)
        f.close()

    def thread_crawler(self):
        threads = []
        while threads or self.crawl_queue:
            """
            这儿crawl_queue用上了，就是我们__bool__函数的作用，为真则代表我们MongoDB队列里面还有数据
            threads 或者 crawl_queue为真都代表我们还没下载完成，程序就会继续执行
            """
            for thread in threads:
                if not thread.is_alive():  ##is_alive是判断是否为空,不是空则在队列中删掉
                    threads.remove(thread)
            while len(threads) < self.max_threads :  ##线程池中的线程少于max_threads
                lock = threading.Lock()
                thread = threading.Thread(target=self.pageurl_crawler,args=(lock,))  ##创建线程
                thread.setDaemon(True)  ##设置守护线程
                thread.start()  ##启动线程
                threads.append(thread)  ##添加进线程队列
            time.sleep(self.sleep_time)


def process_crawler():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print('将会启动进程数为：', num_cpus)
    for i in range(num_cpus):
        p = multiprocessing.Process(target=Mzitu_crawler().thread_crawler()) ##创建进程
        p.start() ##启动进程
        process.append(p) ##添加进进程队列
    for p in process:
        p.join() ##等待进程队列里面的进程结束



if __name__ == "__main__":
    # url_to_mongoqueue('http://www.mzitu.com/all')
    process_crawler()