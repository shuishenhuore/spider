import os.path
import easygui as gui
from tqdm import tqdm
import requests

class Xiaojiejie(object):
    def __init__(self,url):
        self.url = url
        self.imgUrl = ''
        self.name = ''
        self.imgnum = 1
    def askimg(self):
        try:
            # self.imgnum = eval(input("你需要下载几张图片："))
            self.imgnum = eval(gui.enterbox(msg='你需要下载几张图片：',title='xiaojiejie'))
        except Exception as e:
            print(f"刁民看你输的啥")
            self.askimg()

    def getdata(self):

        res = requests.get(self.url).json()['data']
        self.name = res.split('/')[-1]
        self.imgUrl = res.strip()
    def download(self):
        res = requests.get(self.imgUrl)
        if not os.path.exists('xiaojiejie'):
            os.mkdir('xiaojiejie')
        with open(f'./xiaojiejie/{self.name}','wb')as f:
            f.write(res.content)
    def run(self):
        self.askimg()
        for i in tqdm(iterable=range(self.imgnum),desc='下载中'):
            self.getdata()
            self.download()

def asktype():
    enter = gui.buttonbox(msg='请选择你喜欢的类型',choices=['heisi','meinv','jk','baisi'])
    if enter == 'heisi':
        return 'https://v2.xxapi.cn/api/heisi'
    elif enter == 'meinv':
        return 'https://v2.xxapi.cn/api/meinvpic'
    elif enter =='jk':
        return 'https://v2.xxapi.cn/api/jk'
    elif enter == 'baisi':
        return 'https://v2.xxapi.cn/api/baisi'


if __name__ == '__main__':
    url = asktype()
    xiaojiejie = Xiaojiejie(url=url)
    xiaojiejie.run()
