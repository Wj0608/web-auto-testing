# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from config.globalparam import script_path
import unittest, time, re, os

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_entertainment(self):
        driver = self.driver
        driver.get("http://testing-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[1]").click()  # 让分，博彩，竞猜
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[2]').click()  # 具体项目
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[1]/div/input').send_keys("2018-06-02")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]').click()  # click anywhere
        #  driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[1]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("娱乐竞猜")
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/input').send_keys("娱乐竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input').send_keys("娱乐竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[1]/div/div/input').send_keys("娱乐竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[1]/div/div/input').send_keys("娱乐竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]').click()

    def test_politics(self):
        driver = self.driver
        driver.get("http://testing-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[1]").click()  # 让分，博彩，竞猜
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[3]').click()  # 具体项目
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[1]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("时政竞猜")
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/input').send_keys("时政竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input').send_keys("时政竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[1]/div/div/input').send_keys("时政竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[1]/div/div/input').send_keys("时政竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]').click()

    def test_finance(self):
        driver = self.driver
        driver.get("http://testing-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[1]").click()  # 让分，博彩，竞猜
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[4]').click()  # 具体项目
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[1]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("金融竞猜")
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/input').send_keys("金融竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input').send_keys("金融竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[1]/div/div/input').send_keys("金融竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[1]/div/div/input').send_keys("金融竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]').click()

    def test_esport(self):
        driver = self.driver
        driver.get("http://testing-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[1]").click()  # 让分，博彩，竞猜
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[2]').click()  # 具体项目
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[1]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("电竞竞猜")
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/input').send_keys("电竞竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input').send_keys("电竞竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[1]/div/div/input').send_keys("电竞竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[1]/div/div/input').send_keys("电竞竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]').click()

    def test_sport(self):
        driver = self.driver
        driver.get("http://testing-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[1]").click()  # 让分，博彩，竞猜
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[1]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[2]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[3]/ul/li[10]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[8]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("体育竞猜")
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[1]/div/div/input').send_keys("体育竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input').send_keys("体育竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[1]/div/div/input').send_keys("体育竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[1]/div/div/input').send_keys("体育竞猜")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div').click()
        os.system(script_path)
        while (driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/p').text != '已成功上传图片，如果预览失效因为图片地址为海外IP，您依旧可以重新选择图片上传并且替换'):
            time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]').click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

