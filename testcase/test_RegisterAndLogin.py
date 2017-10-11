#coding=utf-8


from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FirstPage,DAE_RegisterPage
from config import DAE_ErrorMessage,DAE_RegisterPage_Element,DAE_SuccessMessage
from public.common import datainfo
import time

class TestHuiyin(mytest.MyTest):
    """DAE注册登录功能测试"""

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
    #     self.assertEqual(u'请输入邮箱/手机号 ',self.dr.get_attribute(ass ert_element.PhoneOrEmailLogin_button_assert))

    # # 手机注册
    # def test_a_PhoneRegister(self):
    #     firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
    #     firstPage.type_PhoneNumber('18774389630')
    #     firstPage.click_Register_Button()
    #     register = DAE_RegisterPage.RegisterPage(self.dr)
    #     self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
    #     if(register.get_PhoneNumber()== '18774389630'):
    #         register.Type_VCode('123456')
    #         register.Type_LoginAndConfirmPassword('test123','test123')
    #       #  register.Click_CreateAccount()
    #     # print(self.dr.get_element(DAE_RegisterPage_Element.RegisterSuccess).is_displayed())
    #     self.assertTrue(self.dr.get_element(DAE_SuccessMessage.RegisterSuccess).is_displayed())
    #

    def test_a_login(self):
        """登录功能测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click_HeaderLogin_button()
        firstPage.Login('18774389631','test123')
        time.sleep(5)
        self.assertEqual(self.dr.get_url(),'http://pre-www.szjys.com/wallet')

    def test_b_login_WrongPassword(self):
        """登录密码错误功能测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click_LoginImmediately()
        firstPage.Login('18774389635','t123')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.AccountOrPwd_Error).is_displayed())

    def test_c_register_WrongVCode(self):
        """注册验证码错误功能测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.type_PhoneNumber('18774389630')
        firstPage.click_Register_Button()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
        if(register.get_PhoneNumber()== '18774389630'):
            register.Type_VCode('12345')
            register.Type_LoginAndConfirmPassword('test123','test123')
            register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.Network_Error).is_displayed())

    def test_c_register_PhoneExist(self):
        """注册手机号已存在功能测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.type_PhoneNumber('18774389631')
        firstPage.click_Register_Button()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
        if(register.get_PhoneNumber()== '18774389631'):
            register.Type_VCode('123456')
            register.Type_LoginAndConfirmPassword('test123','test123')
            register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.PhoneExist).is_displayed())

    def test_c_register_DifferentPWD(self):
        """注册确认密码不同功能测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.type_PhoneNumber('18774389630')
        firstPage.click_Register_Button()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
        if(register.get_PhoneNumber()== '18774389630'):
            register.Type_VCode('123456')
            register.Type_LoginAndConfirmPassword('test123','123test')
            register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.DifferentPwd_Error).is_displayed())

    def test_c_register_WrongPhoneNumber(self):
        """注册手机号格式错误功能测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.type_PhoneNumber('18774389630djafhgj')
        firstPage.click_Register_Button()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
        if(register.get_PhoneNumber()== '18774389630djafhgj'):
            register.Type_VCode('123456')
            register.Type_LoginAndConfirmPassword('test123','test123')
            register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.WrongPhoneNumber_Error).is_displayed())

