#coding=utf-8

from time import sleep
from public.common import mytest,datainfo
from public.common import publicfunction
from public.pages import DAE_LoginPage,DAE_RegisterPage
from config import DAE_PromptMessage,DAE_RegisterPage_Element,DAE_SuccessMessage
import time

class TestLogin(mytest.MyTest):

    def test_a_login(self):
        """登录功能测试"""
        firstPage = DAE_LoginPage.DAEFirstPage(self.dr)
        firstPage.Login("yangmengying8977@dingtalk.com","123456")
        firstPage.click_SigninButton('123456')
        time.sleep(3)
        # firstPage.Login(list(dict[1].values())[0],list(dict[1].values())[1])
        # firstPage.Login(dict.keys(0),dict.values(0))
        # time.sleep(5)
        URL = self.dr.get_url()
        # self.assertEqual(self.dr.get_url(),'https://pre-www.dae.org/trade/XUC_BTC')

    def test_b_login_WrongPassword(self):
        """登录密码错误功能测试"""
        firstPage = DAE_LoginPage.DAEFirstPage(self.dr)
        firstPage.Login("yangmengying8977@dingtalk.com","test123")
        firstPage.click_SigninButton()
        time.sleep(2)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.AccountOrPwd_Error).is_displayed())

    def test_c_nullemail(self):
        """账号输入为空"""
        firstPage = DAE_LoginPage.DAEFirstPage(self.dr)
        firstPage.Login("","")
        firstPage.click_SigninButton()
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.EmailsNullI).is_displayed())

    # def test_c_register_WrongVCode(self):
    #     """注册验证码错误功能测试"""
    #     firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
    #     firstPage.type_PhoneNumber('18774389630')
    #     firstPage.click_Register_Button()
    #     register = DAE_RegisterPage.RegisterPage(self.dr)
    #     self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
    #     if(register.get_PhoneNumber()== '18774389630'):
    #         register.Type_VCode('12345')
    #         register.Type_LoginAndConfirmPassword('test123','test123')
    #         register.Click_CreateAccount()
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.Network_Error).is_displayed())
    #
    # def test_c_register_PhoneExist(self):
    #     """注册手机号已存在功能测试"""
    #     firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
    #     firstPage.type_PhoneNumber('18774389631')
    #     firstPage.click_Register_Button()
    #     register = DAE_RegisterPage.RegisterPage(self.dr)
    #     self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
    #     if(register.get_PhoneNumber()== '18774389631'):
    #         register.Type_VCode('123456')
    #         register.Type_LoginAndConfirmPassword('test123','test123')
    #         register.Click_CreateAccount()
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.PhoneExist).is_displayed())
    #
    # def test_c_register_DifferentPWD(self):
    #     """注册确认密码不同功能测试"""
    #     firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
    #     firstPage.type_PhoneNumber('18774389630')
    #     firstPage.click_Register_Button()
    #     register = DAE_RegisterPage.RegisterPage(self.dr)
    #     self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
    #     if(register.get_PhoneNumber()== '18774389630'):
    #         register.Type_VCode('123456')
    #         register.Type_LoginAndConfirmPassword('test123','123test')
    #         register.Click_CreateAccount()
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.DifferentPwd_Error).is_displayed())
    #
    # def test_c_register_WrongPhoneNumber(self):
    #     """注册手机号格式错误功能测试"""
    #     firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
    #     firstPage.type_PhoneNumber('18774389630djafhgj')
    #     firstPage.click_Register_Button()
    #     register = DAE_RegisterPage.RegisterPage(self.dr)
    #     self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
    #     if(register.get_PhoneNumber()== '18774389630djafhgj'):
    #         register.Type_VCode('123456')
    #         register.Type_LoginAndConfirmPassword('test123','test123')
    #         register.Click_CreateAccount()
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.WrongPhoneNumber_Error).is_displayed())