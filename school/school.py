import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import ddddocr
from faker import Factory
import requests
import urllib3
from pyquery import PyQuery as pq

class Browser():
    # 初始化操作
    def __init__(self,url):
        service = Service('chromedriver.exe')
        option = Options()
        option.add_argument('--disable-infobars')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        option.add_argument(f'user-agent={user_agent}')
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(service=service,options=option)
        self.driver.get(url)
        self.code = ''
        self.ocr = ddddocr.DdddOcr()
        self.cookie = ''
        self.data = ''
    # 模拟登录
    def login(self):
        username = self.driver.find_element(By.CSS_SELECTOR,'#userAccount')
        username.send_keys('输入自己的账号')
        password = self.driver.find_element(By.CSS_SELECTOR,'#userPassword')
        password.send_keys('输入自己的密码')
        code = self.driver.find_element(By.CSS_SELECTOR,'#RANDOMCODE')
        code.send_keys(self.code)
        loginbtn = self.driver.find_element(By.CSS_SELECTOR,'.login_btn')
        loginbtn.click()
        time.sleep(2)
        for i in self.driver.get_cookies():
            self.cookie += f"{i['name']}={i['value']};"
        self.driver.save_screenshot('ok.png')
    # 保存验证码图片
    def savecode(self):
        self.driver.save_screenshot('preCode.jpg')
        with Image.open('preCode.jpg')as img:
            area = (1124,490,1240,545)
            resimg = img.crop(area)
            resimg.save('code.jpg')
    # 获得验证码
    def getcode(self):
        with open('code.jpg','rb')as f:
            imgdata = f.read()
        self.code = self.ocr.classification(imgdata)
        print(self.code)
    # 获取课程信息
    def getclass(self):
        time.sleep(2)
        url = 'https://jw.gdsty.edu.cn/jsxsd/framework/main_index_loadkb.jsp'
        data = {
            'rq':time.strftime("%Y-%m-%d",time.localtime()),
            'sjmsValue':'97AEEC590D96F04DE053110AA8C0F71A'
        }
        headers = {
                "accept": "text/html, */*; q=0.01",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "connection": "keep-alive",
                "content-length": "56",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cookie": self.cookie,
                "host": "jw.gdsty.edu.cn",
                "origin": "https://jw.gdsty.edu.cn",
                "referer": "https://jw.gdsty.edu.cn/jsxsd/framework/xsMain_new.jsp?t1=1",
                "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": Factory.create().user_agent(),
                "x-requested-with": "XMLHttpReque"
        }
        self.data = requests.post(url=url,data=data,headers=headers,verify=False).text
    # 进行数据解析
    def savedata(self):
        doc = pq(self.data)
        parsedata = doc('#Form1')

        with open('data.html','w',encoding='utf-8')as f:
            f.write(f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="UTF-8">
                  <title>Title</title>
                </head>
                <body>
                {parsedata}
                </body>
                </html>
                ''')
    def main(self):
        self.savecode()
        self.getcode()
        self.login()
        self.getclass()
        self.savedata()
if __name__ == '__main__':
    urllib3.disable_warnings()
    url = 'https://jw.gdsty.edu.cn/'
    browser = Browser(url)
    browser.main()
