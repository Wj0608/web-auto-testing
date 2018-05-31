# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from public.common import pyselenium
import unittest, time, re

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = ""
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sport_International(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[9]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div/div/ul/li/div/input').send_keys("中国"+Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_China(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[8]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div/div/ul/li/div/input').send_keys("上海"+Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_FIFA(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[7]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div/div/ul/li/div/input').send_keys("德国"+Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_Euro(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[6]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_serie(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[5]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_bundesliga(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[4]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_ligue(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[3]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_leagueone(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[2]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[2]').click()  # NBA
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[6]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[6]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

    def test_sport_laliga(self):
        driver = self.driver
        driver.get("http://demo-crm.intranet.etcgame.com/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("cmsadmin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_name("password").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"新建预测").click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()  # my xpath
        driver.find_element_by_xpath("//li[3]").click()  # 让分，博彩，
        driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()  # 具体项目
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div/div').click()  # 预测球类
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()  # 篮球
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div[2]/div/div/div/div').click()  # 选择比赛
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/ul/li[1]').click()  # 西班牙
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/span[2]/div/input').click()  # 上线时间-日期
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[2]/span/input').click()  # 上线时间-时间
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[1]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[2]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[2]/div[3]/ul/li[11]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[1]/span[2]/div/input').click()
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[5]/div[2]/span/input').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[1]/ul/li[24]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[2]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div/div[2]/div[3]/ul/li[60]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[6]/div/div/div/div/div').click()
        driver.find_element_by_xpath('/html/body/div[10]/div/div/div/ul/li[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]/div[7]/div/div/input').send_keys(1000)
        driver.find_element_by_xpath('//*[@id="item_name_zh_0"]').send_keys("选项一")
        driver.find_element_by_xpath('//*[@id="item_name_zh_1"]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[5]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath("//input[@type='file']").send_keys("C:\\Users\\Public\\wangjie\\pic\\china.jpg")  # pic
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_en_0"])[2]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_en_1"])[2]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ja_0"])[3]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ja_1"])[3]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ko_0"])[4]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ko_1"])[4]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/textarea').send_keys("文本描述")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[5]').click()
        driver.find_element_by_xpath('(//*[@id="item_name_ru_0"])[5]').send_keys("选项一")
        driver.find_element_by_xpath('(//*[@id="item_name_ru_1"])[5]').send_keys("选项二")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[5]/textarea').send_keys("文本描述")
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div/input').send_keys('C:\\Users\Public\wangjie\pic\china')
        #  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div').send_keys('C:\\Users\Public\wangjie\pic\china')

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