#coding=utf-8

from public.common import mytest
from config import Forgot_password
from public.pages import DAE_ForgotpasswordPage
import time
class Test_Forgot_password(mytest.MyTest):
    def test_Forgot_password1(self):
        """忘记密码通过"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('1234@qq.com','123456')
        firstPage.Forgot_password_step2('12345678','12345678')
        self.assertTrue(self.dr.get_element(Forgot_password.Reset_successfully).is_displayed())
    def test_Forgot_password2(self):
        """忘记密码账号不存在"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('11111@qq.com',"123456")
        self.assertTrue(self.dr.get_element(Forgot_password.click_next).is_displayed())
    def test_Forgot_password3(self):
        """忘记密码验证码错误"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('1234@qq.com',"111111")
        self.assertTrue(self.dr.get_element(Forgot_password.invalid_validation_code).is_displayed())
    def test_Forgot_password4(self):
        """忘记密码验证码为空"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('1234@qq.com',"")
        time.sleep(2)
        self.assertTrue(self.dr.get_element(Forgot_password.please_code).is_displayed())
    def test_Forgot_password5(self):
        """忘记密码step2两次密码不一致"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('1234@qq.com','123456')
        firstPage.Forgot_password_step2('123456','1234567')
        self.assertTrue(self.dr.get_element(Forgot_password.password_mismatch).is_displayed())
    def test_Forgot_password6(self):
        """忘记密码step2设置密码为空"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('1234@qq.com','123456')
        firstPage.Forgot_password_step2("","")
        self.assertTrue(self.dr.get_element(Forgot_password.please_login_password).is_displayed())
    def test_Forgot_password7(self):
        """忘记密码step2设置密码不足6位提示"""
        firstPage = DAE_ForgotpasswordPage.DAEForgotpasswordPage(self.dr)
        firstPage.Forgot_password_step1('1234@qq.com','123456')
        firstPage.Forgot_password_step2("12","")
        self.assertTrue(self.dr.get_element(Forgot_password.password_characters).is_displayed())###################################