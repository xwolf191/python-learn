# _*_ coding:utf-8 _*_

import urllib3
from bs4 import BeautifulSoup

pm = urllib3.PoolManager(num_pools=10)

def request(url):
    """
    请求url，返回html
    :param url:
    :return:
    """
    # 响应内容
    resp = pm.request('GET', url)
    return resp.data.decode('utf8', errors='ignore')


def parse(content):
    """
    解析html
    :param content:
    :return:
    """
    # 音乐列表
    musics = []
    bs = BeautifulSoup(content, 'lxml')
    uls = bs.find('var media =')
    print(uls)


def download(musicList):
    """
    下载mp3
    :return:
    """
    for music in musicList:
        name = music['name']
        href = music['href']
        resp = pm.request('GET', href)
        # 将mp3文件下载到指定目录
        with open('E:\music\\'+name+'.mp3', 'wb') as f:
              f.write(resp.data)
        print(name+',下载成功.')
    print('OK,全部下载完成.')


# 入口
url = "http://www.ting56.com/video/1031-0-2.html"
#print(request(url))
