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
    return resp.data.decode()


def parse(content):
    """
    解析html
    :param content:
    :return:
    """
    # 音乐列表
    musics = []
    bs = BeautifulSoup(content, 'lxml')
    uls = bs.find('div', attrs={'class': 'chang'}).find('ul')
    for li in uls.find_all('li'):
        a = li.find('a')
        # 歌曲名称
        name = a.string
        script = li.find('script')
        scriptText = script.string[18:]
        # mp3文件地址
        musicUrlStr = scriptText[:len(scriptText) - 3].split('href')[1]
        # 截取到真实的url
        href = musicUrlStr[3:len(musicUrlStr) - 8]
        # 封装为字典
        music = {'name': name, 'href': href}
        musics.append(music)
    return musics


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
url = "http://www.333ttt.com/up/top16.html"
download(parse(request(url)))
