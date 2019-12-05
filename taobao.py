# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from selenium import webdriver
from os import path
chrome_driver = r'D:\newproject\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
# driver = webdriver.Chrome()


def login(url):
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://login.taobao.com/member/login.jhtml")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在30秒内完成扫码")
        time.sleep(30)
        browser.get(url)
    time.sleep(3)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= buytime:
            try:
                # 点击抢购
                if browser.find_element_by_id("J_LinkBuy"):
                    print("点吖！！！")
                    browser.find_element_by_id("J_LinkBuy").click()
                    time.sleep(0.09)
                    while now >= buytime:
                        try:
                            print("买吖！！！")
                            browser.find_element_by_class_name('go-btn').click()
                            browser.find_element_by_link_text('提交订单').click()
                        except:
                            time.sleep(0.02)
            except:
                time.sleep(0.08)
        print(now)
        time.sleep(0.05)


if __name__ == "__main__":
    times = input("请输入抢购时间：时间格式：2018-11-06 10:08:00.000000")
    # 时间格式："2018-09-06 11:20:00.000000"
    url = input("请输入抢购地址")
    login(url)
    buy(times)
