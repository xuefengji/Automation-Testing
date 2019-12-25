from selenium import webdriver
from demos.base.find_element import FindElement
import time
class ActionMethod():
    def __init__(self):
        pass

    #打开浏览器
    def open_browser(self,key):
        if key == 'chrome':
            self.driver = webdriver.Chrome()
        elif key == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    #输入url
    def send_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_element(self,key):
        element = FindElement(self.driver)
        return element.get_value(key)
    #输入元素
    def send_value(self,value,key):
        self.get_element(key).send_keys(value)

    #element点击
    def element_click(self,key):
        self.get_element(key).click()
    #等待
    def sleep_time(self,sec):
        time.sleep(sec)

    #关闭浏览器
    def driver_close(self):
        self.driver.close()