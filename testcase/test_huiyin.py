#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import huiyinPage
from public.common import datainfo
from config import Assert_Element



class TestHuiyin(mytest.MyTest):
    """汇银首页测试"""

    # def test_open(self):
    #     """打开首页"""
    #     huiyinpage = huiyinPage.HuiyinPage(self.dr)
    #     huiyinpage.into_huiyin_page()
    #     publicfunction.get_img(self.dr,'111.png')

    def test_ETH_button(self):
        """点击ETH按钮"""
        huiyinpage = huiyinPage.HuiyinPage(self.dr)
        huiyinpage.click_ETH_button()
        sleep(2)
        self.assertIn(u'1ETH=¥ ',self.dr.get_text(Assert_Element.ETH_button_assert))

    def test_XRP_button(self):
        """点击XRP按钮"""
        huiyinpage = huiyinPage.HuiyinPage(self.dr)
        huiyinpage.click_XRP_button()
        self.assertIn(u'1XRP=¥ ',self.dr.get_text(Assert_Element.XRP_button_assert))

    def test_PhoneOrEmailLogin_button(self):
        """点击手机或邮箱登录按钮"""
        huiyinpage = huiyinPage.HuiyinPage(self.dr)
        huiyinpage.click_PhoneOrEmailLogin_button()
        self.assertEqual(u'请输入邮箱/手机号 ',self.driver.get_attribute(Assert_Element.PhoneOrEmailLogin_button_assert))