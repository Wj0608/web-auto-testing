# coding=utf-8

from public.common import mytest
from config import DAE_RegisterPage_Element
from public.pages import DAE_RegisterPage
import time


class Test_Register(mytest.MyTest):

    # def test_Register1(self):
    #      """打开首页"""
    #      huiyinpage = huiyinPage.HuiyinPage(self.dr)
    #      publicfunction.get_img(self.dr,'111.png')
    #
    #     """注册成功"""
    #     firstPage = DAE_RegisterPage.RegisterPage(self.dr)
    #     firstPage.Register1('51456','51456@qq.com','123456')
    #     firstPage.Register2('123456','123456')
    #     time.sleep(2)
    #     self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.Sign_up).is_displayed())
    #
    # def test_XRP_button(self):
    #     """点击XRP按钮"""
    #     huiyinpage = huiyinPage.HuiyinPage(self.dr)
    #     huiyinpage.click_XRP_button()
    #     self.assertIn(u'1XRP=¥ ',self.dr.get_text(assert_element.XRP_button_assert))
    #
    # # 手机注册
    def test_Register2(self):
        """注册昵称/邮箱已存在"""
    #     firstPage.type_PhoneNumber('18774389630')
        self.assertTrue(True)
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('51456','51456@qq.com','123456')
    #     if(register.get_PhoneNumber()== '18774389630'):
    #         register.Type_VCode('123456')
    #         register.Type_LoginAndConfirmPassword('test123','test123')
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.existed_nickname).is_displayed())
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.registered_email).is_displayed())

    def test_Register3(self):
        """注册验证码错误"""
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('123888','12390@qq.com','111111')
        time.sleep(1)
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.invalid_code).is_displayed())

    def test_Register4(self):
        """注册邮箱为空"""
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('nihaom','','')
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.please_email).is_displayed())

    def test_Register5(self):
        """注册昵称/邮箱输入特殊字符"""
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('%$#@','1234r','')
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.includes_invalid).is_displayed())
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.please_correct_email).is_displayed())

    def test_Register6(self):
        """注册邮箱验证码为空"""
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('112233','112233@qq.com','')
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.please_code).is_displayed())

    def test_Register7(self):
        """注册step2密码为空"""
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('123888','12390@qq.com','123456')
        firstPage.Register2('','123456')
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.please_password).is_displayed())

    def test_Register8(self):
        """注册step2密码不一致"""
        firstPage = DAE_RegisterPage.RegisterPage(self.dr)
        firstPage.Register1('123888','12390@qq.com','123456')
        firstPage.Register2('111111','123456')
        self.assertTrue(self.dr.get_element(DAE_RegisterPage_Element.mismatch_password).is_displayed())