# coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FirstPage, DAE_RegisterPage
from config import DAE_PromptMessage
from public.common import datainfo
import time
import unittest


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

    def test_b_register(self):
        """注册功能测试"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('yangaaa')
        registerPage.Type_Email('12345678901@qq.com')
        registerPage.Type_VCode('123456')
        registerPage.click_NextStep()
        registerPage.setPassword('test123', 'test123')
        registerPage.Type_ImageCode()
        registerPage.click_register()
        time.sleep(5)
        self.assertTrue(self.dr.get_url(), 'http://pre-www.dae.org/login')

    def test_b_registerWithExistedEmail(self):
        """注册功能测试--邮箱已存在"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('yang123')
        registerPage.Type_Email('yangmengying8977@dingtalk.com')
        registerPage.Type_VCode('123456')
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.wrongEmail).is_displayed())

    def test_b_registerWithExistedNickname(self):
        """注册功能测试--昵称已存在"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('yang')
        registerPage.Type_Email('')
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.nickNameExist).is_displayed())

    def test_b_registerWithShortNickname(self):
        """注册功能测试--昵称长度过短"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('1一y')
        registerPage.Type_Email('')
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.nicknameFormatWrong).is_displayed())

    def test_b_registerWithNicknameIncludeIllegalChars(self):
        """注册功能测试--昵称包含特殊字符"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('1@!')
        registerPage.Type_Email('')
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.nicknameIncludeillegalChars).is_displayed())

    def test_b_emailIncludeIllegalChars(self):
        """注册功能测试--邮箱账号包含特殊字符"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('yangyangyang')
        registerPage.Type_Email('123rjfkd！@#￥f,d')
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.emailIncludeillegalChars).is_displayed())

    def test_b_registerWithWrongVCode(self):
        """注册功能测试--邮箱验证码错误"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('yangaaa')
        registerPage.Type_Email('1234567890@qq.com')
        registerPage.Type_VCode('789456')
        registerPage.click_NextStep()
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.WrongCode).is_displayed())

    def test_b_registerSetPwdNotSame(self):
        """注册功能测试"""
        firstPage = DAE_FirstPage.DAELogin(self.dr)
        firstPage.click_HeaderRegisterButton()
        registerPage = DAE_RegisterPage.RegisterPage(self.dr)
        registerPage.Type_nickName('yangaaa')
        registerPage.Type_Email('1234567890@qq.com')
        registerPage.Type_VCode('123456')
        registerPage.click_NextStep()
        registerPage.setPassword('123', '456789')
        time.sleep(5)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.NotSamePwd).is_displayed())