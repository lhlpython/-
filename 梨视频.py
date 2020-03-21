import requests
import re
from lxml import etree
from urllib.request import urlretrieve
import os


def download():

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 '
        '/537.36'

    }
    html = requests.get(
        'https://www.pearvideo.com/category_9', headers=header).text
    req = '<a href="(.*?)" class="vervideo-lilink actplay">'
    video_id = re.findall(req, html)

    video_url = []
    starturl = 'https://www.pearvideo.com/'
    for i in video_id:
        newurl = starturl + i
        video_url.append(newurl)

    for playurl in video_url:
        html = requests.get(playurl).text
        req = 'ldUrl="",srcUrl="(.*?)",vdoUrl=srcUrl'
        req = re.compile(req)
        purl = re.findall(req, html)

        req = ' <h1 class="video-tt">(.*?)</h1>'
        pname = re.findall(req, html)
        print('正在下载。。。%s' % pname[0])
        path = 'video'

        if path not in os.listdir():
            os.mkdir(path)

        urlretrieve(purl[0], path + '/%s.mp4' % pname[0])


download()
