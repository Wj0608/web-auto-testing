#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FirstPage
from public.common import datainfo
from config import assert_element

class TestHuiyin(mytest.MyTest):
    """汇银首页测试"""

    # def test_open(self):
    #      """打开首页"""
    #      huiyinpage = huiyinPage.HuiyinPage(self.dr)
    #      publicfunction.get_img(self.dr,'111.png')
    #
    # def test_ETH_button(self):
    #     """点击ETH按钮"""
    #     huiyinpage = huiyinPage.HuiyinPage(self.dr)
    #     huiyinpage.click_ETH_button()
    #     sleep(2)
    #     self.assertIn(u'1ETH=¥ ',self.dr.get_text(assert_element.ETH_button_assert))
    #
    # def test_XRP_button(self):
    #     """点击XRP按钮"""
    #     huiyinpage = huiyinPage.HuiyinPage(self.dr)
    #     huiyinpage.click_XRP_button()
    #     self.assertIn(u'1XRP=¥ ',self.dr.get_text(assert_element.XRP_button_assert))
    #
    # def test_PhoneOrEmailLogin_button(self):
    #     """点击手机或邮箱登录按钮"""
    #     firstpage = DAE_FirstPage.HuiyinPage(self.dr)
    #     firstpage.click_PhoneOrEmailLogin_button()
    #     self.assertEqual(u'请输入邮箱/手机号 ',self.dr.get_attribute(assert_element.PhoneOrEmailLogin_button_assert))

    def login(self):
        huiyinpage = DAE_FirstPage.HuiyinPage(self.dr)
        huiyinpage.click_PhoneOrEmailLogin_button()
        huiyinpage.LoginWithEmailOrPhone('15273258977','test123')
        # self.assertIn(u'24小时交易量',self.dr.get_text(assert_element.VolumeOfBussiness))
        self.assertIn(u'24小时交易量',huiyinpage)

    def register(self):
        register = DAE_FirstPage.HuiyinPage(self.dr)
