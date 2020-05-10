import urllib3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

"""
 ting56下载.
"""

pm = urllib3.PoolManager(num_pools=10)


def request(url, name):
    """
    请求url，返回html
    :param url:
    :return:
    """
    browser = webdriver.Chrome()
    # 延迟30s
    browser.implicitly_wait(30)
    browser.get(url)
    # 根据元素id获取元素
    audio = browser.find_element_by_id('jp_audio_0')
    # 获取元素的属性信息
    src = audio.get_attribute('src')
    # 可能会为空
    if src is not None and len(src) > 10:
        resp = pm.request('GET', src)
        with open('E:\music\\' + str(name) + '.mp3', 'wb') as f:
            f.write(resp.data)
            print(str(name) + ',下载成功.')


for i in range(3):
    url = "http://www.xxx.com/video/1031-0-" + str(i) + ".html"
    request(url, i + 1)
