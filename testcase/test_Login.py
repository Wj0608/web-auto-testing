#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FirstPage
from config import DAE_PromptMessage,globalparam
from public.common import datainfo
import time
from testcase import test_Register

class TestLogin(mytest.MyTest):

    def test_a_NewUserLogin(self):
        """新注册用户登录功能测试"""
        test_Register.TestHuiyin.test_b_register(self)
        time.sleep(5)
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        email = 'yangmengying8977@dingtalk.com'
        firstPage.type_Email(email)
        firstPage.type_password('test123')
        firstPage.type_ImageCode(email)
        time.sleep(5)
        self.assertEqual(self.dr.get_url(),globalparam.environment_address + 'setmoneypw')

    def test_a_LoginWithPhone(self):
        """老用户登录功能测试-使用手机登录"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderLogin_button()
        email = '15273258977'
        firstPage.type_Email(email)
        firstPage.type_password('test123')
        firstPage.type_ImageCode(email)
        time.sleep(5)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.LoginWrong).is_displayed())

    def test_a_Login(self):
        """开启了邮箱安全策略的用户登录功能测试"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderLogin_button()
        email = 'yangmengying8977@dingtalk.com'
        firstPage.type_Email(email)
        firstPage.type_password('test123')
        firstPage.type_ImageCode(email)
        time.sleep(5)
        self.assertEqual(self.dr.get_url(),globalparam.environment_address + 'wallet')