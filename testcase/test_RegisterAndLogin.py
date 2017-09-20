#coding=utf-8


from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FirstPage,DAE_RegisterPage
from config import DAE_ErrorMessage,DAE_RegisterPage_Element
from public.common import datainfo
from config import assert_element

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
    #     self.assertEqual(u'请输入邮箱/手机号 ',self.dr.get_attribute(assert_element.PhoneOrEmailLogin_button_assert))

    def test_a_PhoneRegister(self):
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click_PhoneOrEmailLogin_button()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        register.Type_EmailOrPhone('18774389631')
        register.Type_VCode('123456')
        register.Type_LoginPassword('test123')
        register.Type_ConfirmLoginPassword('test123')
        register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.RegisterSuccess).is_displayed())

    def test_b_login_WrongPassword(self):
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click_PhoneOrEmailLogin_button()
        firstPage.LoginWithEmailOrPhone('18774389635','t123')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.AccountOrPwd_Error).is_displayed())

    def test_c_register_WrongVCode(self):
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click_RegisterButton()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        register.Type_EmailOrPhone('18774389631')
        register.Type_VCode('12345')
        register.Type_LoginPassword('test123')
        register.Type_ConfirmLoginPassword('test123')
        register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.Network_Error).is_displayed())

    def test_c_register_PhoneExist(self):
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click_RegisterButton()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        register.Type_EmailOrPhone('18774389631')
        register.Type_VCode('12345')
        register.Type_LoginPassword('test123')
        register.Type_ConfirmLoginPassword('test123')
        register.Click_CreateAccount()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.PhoneExist).is_displayed())