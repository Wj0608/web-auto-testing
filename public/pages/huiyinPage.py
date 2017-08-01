#coding=utf-8

from public.common import basepage
import time
from config import DAE_FirstPage

class HuiyinPage(basepage.Page):

    def into_huiyin_page(self):
        """打开DAE首页"""
        self.dr.open('http://www.intranet.szjys.com/')
    # def input_search_key(self,values):
    #     """输入搜索关键词"""
    #     self.dr.clear_type('id->kw',values)

    def click_ETH_button(self):
        """点击ETH按钮"""
        element=self.dr.get_element(DAE_FirstPage.ETH_button)
        self.dr.click(DAE_FirstPage.ETH_button)
        # self.dr.click('xpath->//*[@id="form1"]/div[2]/div/div[2]/div/ul/li[2]/a')
        self.dr.ut_highlighted(element)
        time.sleep(3)


    def click_XRP_button(self):
        """点击XRP按钮"""
        element=self.dr.get_element(DAE_FirstPage.XRP_button)
        self.dr.click(DAE_FirstPage.XRP_button)
        self.dr.ut_highlighted(element)
        time.sleep(3)

    def click_PhoneOrEmailLogin_button(self):
        """点击手机/邮箱登录"""
        element=self.dr.get_element(DAE_FirstPage.PhoneOrEmailLogin_button)
        self.dr.click(DAE_FirstPage.PhoneOrEmailLogin_button)
        self.dr.ut_highlighted(element)
        time.sleep(3)


    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()