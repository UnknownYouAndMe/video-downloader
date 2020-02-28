import os
import re
from pip._internal import main
import requests


def m3u8_downloader1(url):
    # 获取m3u8内容
    m3u8 = requests.get(url).text
    # 获取ts文件名
    pattern = re.compile(r'.+.ts')
    ts = pattern.findall(m3u8)
    # 获取ts文件路径
    ts_url = url.split('/')[:-1]
    ts_url = '/'.join(ts_url)
    time = len(ts)
    time2 = 0
    ts_folder = os.getcwd() + '\\ts\\'
    if not os.path.exists(ts_folder):
        os.makedirs(ts_folder)
    while time >= 0:
        time2 = time2 + 1
        ts_urls = ts_url + '/' + ts[time2]
        time = time - 1
        r = requests.get(ts_urls)
        with open(ts_folder + str(time2) + '.ts', 'wb') as f:
            f.write(r.content)
        print(ts_urls)
        filelist = 'file' + ' ' + '\'%d.ts\'' % time2
        with open(ts_folder + 'filelist.txt', 'w') as d:
            d.write(filelist+'\n')
        print('下载完成')


def ts_convert(savename):
    ff = 'ffmpeg -f concat -i filelist.txt -c copy '+savename+'.mp4'
    ff.run()


def m3u8_downloader2():
    return


if __name__ == '__main__':
    url = input("请输入m3u8地址：")
    m3u8_downloader1(url)
