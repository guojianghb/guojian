import os
from selenium import webdriver
import datetime
import time
from selenium import webdriver
from os import path
chrome_driver = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Scripts\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
# browser.get("https://www.taobao.com")
# browser.find_element_by_link_text("亲，请登录").click()
# browser.get("https://cart.taobao.com/cart.htm")
# browser.find_element_by_id("J_SelectAll1").click()

def login():
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print(f"扫码登录")
        time.sleep(15)
def picking(method):
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print(f"找不到！！")
            else:
                print(f"手动勾选")
                time.sleep(5)
def buy(times):
    while True:
        now = datetime.datetime.now.strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"下单成功")
                        break
                except:
                    pass
                while True:
                    try:
                        if browser.find_element_by_link_text("提交订单"):
                            browser.find_element_by_link_text("提交订单").click()
                            print(f"提交成功，请付款")
                    except:
                        print(f"再次尝试")
                        time.sleep(1)
if __name__ == "__main__":
    times = input("请输入抢购时间：时间格式：2018-11-06 10:08:00.000000")
    # 时间格式："2018-09-06 11:20:00.000000"
    url = 1
    login(url)
    buy(times)
