# encoding=utf-8
import urllib3

pm = urllib3.PoolManager(num_pools=10)


def download(url, name):
    resp = pm.request('GET', url)
    # 将mp3文件下载到指定目录
    with open('E:\music\\明朝那些事\\第四部\\' + name + '.mp3', 'wb') as f:
        f.write(resp.data)
    print(name + ',下载成功.')


for i in range(1, 31):
    t = str(i).rjust(3, '0')
    url = 'http://mp3-d.ting89.com:9090/'+'%E5%88%98%E7%BA%AA%E5%90%8C_%E6%98%8E%E6%9C%9D%E9%82%A3%E4%BA%9B%E4%BA%8B%E5%84%BF4/'+t+'.mp3'
    download(url, t)
