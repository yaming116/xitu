# _*_ coding: utf-8 _*_

import requests
import json
import time
import MySQLdb
from multiprocessing.dummy import Pool as ThreadPool
import sys
import base64

reload(sys)

sys.setdefaultencoding('utf-8')

urls = []

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'X-LC-Id': '自行解决',
    'Content-Type': 'application/json',
    'User-Agent': 'AVOS Cloud iOS-v3.3.1 SDK',
    'X-LC-Sign': '自行解决'
}

time1 = time.time()
for i in range(1, 125):
    if i == 1:
	   url = 'https://api.leancloud.cn/1.1/classes/Entry?include=user&limit=100&order=createdAt'
	   urls.append(url)
    else:
	   url = 'https://api.leancloud.cn/1.1/classes/Entry?include=user&limit=100&order=createdAt'+ '&skip=' + str((i -1) * 100)
	   urls.append(url)

# s = requests.Session()

proxies = {
        'http': '120.198.231.87:84',
        #'https': 'http://219.133.31.120:8888',
}

def getsource(url):
    time.sleep(1)
    jscontent = requests.get(url, headers=head,  verify=False).content.decode('utf-8')
    time2 = time.time()
    jsDict = json.loads(jscontent)
    jsResult = jsDict.get('results')
    if len(jsResult) > 0:
        for entry in jsResult:
            objectId = entry.get('objectId')
            title = entry.get('title')
            author = entry.get('author')
            content = entry.get('content')
            tagsTitleArray = entry.get('tagsTitleArray')
            category = entry.get('category')
            hotIndex = entry.get('hotIndex')
            updatedAt = entry.get('updatedAt')
            viewsCount = entry.get('viewsCount')
            collectionCount = entry.get('collectionCount')
            hot = entry.get('hot')
            original = entry.get('original')
            createdAt = entry.get('createdAt')
            _type = entry.get('type')
            english = entry.get('english')
            rankIndex = entry.get('rankIndex')
            url = entry.get('url')
            gfw = entry.get('gfw')
            commentsCount = entry.get('commentsCount')
            subscribersCount = entry.get('subscribersCount')
            userId = entry.get('user').get('objectId')
            originalUrl = entry.get('originalUrl')
            photoUrl = entry.get('screenshot', '')
            if photoUrl != '':
                    photoUrl = photoUrl.get('url')
            

            print("Succeed: " + objectId + "\t" + str(time2 - time1))

            try:
                conn = MySQLdb.connect(host='localhost', user='root', passwd='_', port=3306, charset='utf8')
                cur = conn.cursor()
                # cur.execute('create database if not exists python')
                conn.select_db('gold')
                cur.execute(
                    'INSERT INTO article VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, '
                    '%s,%s,%s)',
                    [objectId, title, author, content, str(tagsTitleArray), category, hotIndex,
                     updatedAt, viewsCount, collectionCount, hot, original, createdAt,
                     _type, english, rankIndex, url, gfw, commentsCount, subscribersCount, userId, 
                     originalUrl, photoUrl])
                cur.close()
                conn.commit()
                conn.close()
            except MySQLdb.Error, e:
                print  "Mysql Error %d: %s" % (e.args[0], e.args[1])

    else:
        print ("Error: " + url)

pool = ThreadPool(10)
try:
    results = pool.map(getsource, urls)
except Exception, e:
    print ('ConnectionError')
    print (e)
    time.sleep(300)
    results = pool.map(getsource, urls)

pool.close()
pool.join()
