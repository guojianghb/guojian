import time
import datetime
from selenium import webdriver
chrome_driver = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Scripts\chromedriver.exe'
# browser = webdriver.Chrome(executable_path=chrome_driver)

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
times = input("请输入抢购时间：时间格式：2018-11-06 10:08:00.000000")
# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(now)
print(times)
# def login():
#     browser.get("https://www.taobao.com")
#     time.sleep(3)
#     if browser.find_element_by_link_text("亲，请登录"):
#         browser.find_element_by_link_text("亲，请登录").click()
#         print(f"扫码登录")
#         time.sleep(15)
# login()
def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:
            while True:
                try:
                    print(f"下单成功")
                except:
                    pass
                while True:
                    try:
                        print(f"提交成功，请付款")
                    except:
                        print(f"再次尝试")
                        time.sleep(1)
buy(times)