#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FindPwdPage,DAE_FirstPage
from config import DAE_PromptMessage
import time
from testcase import test_RegisterAndLogin

class FindPwd(mytest.MyTest):

    def test_a_FindPwd(self):
        """找回密码功能测试"""
        findPwd = DAE_FindPwdPage.FindPwd(self.dr)
        findPwd.click_ForgetLoginPwd()
        findPwd.type_email('yangmengying8977@dingtalk.com')
        findPwd.type_code('123456')
        time.sleep(2)
        findPwd.type_password('test123','test123')
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.FindPwdSuccess))

    def test_a_FindPwdWithPhone(self):
        """找回密码功能测试-使用手机找回密码"""
        findPwd = DAE_FindPwdPage.FindPwd(self.dr)
        findPwd.click_ForgetLoginPwd()
        findPwd.type_email('15273258977')
        findPwd.type_code('123456')
        time.sleep(2)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.RegainCode))

    def test_a_FindPwdWithWrongFormatPhone(self):
        """找回密码功能测试-使用错误手机格式找回密码"""
        findPwd = DAE_FindPwdPage.FindPwd(self.dr)
        findPwd.click_ForgetLoginPwd()
        findPwd.type_email('152732258977')
        findPwd.type_code('123456')
        time.sleep(2)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.WrongFormat))

    def test_a_FindPwdWithWrongCode(self):
        """找回密码功能测试-输入错误验证码"""
        findPwd = DAE_FindPwdPage.FindPwd(self.dr)
        findPwd.click_ForgetLoginPwd()
        findPwd.type_email('15273258977')
        findPwd.type_code('789456')
        time.sleep(2)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.WrongCode))

    def test_a_FindPwdWithNullEmail(self):
        """找回密码功能测试-不输入邮箱号"""
        findPwd = DAE_FindPwdPage.FindPwd(self.dr)
        findPwd.click_ForgetLoginPwd()
        findPwd.type_email(None)
        time.sleep(2)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.NoneEmail))

    def test_a_FindPwdWithNullCode(self):
        """找回密码功能测试-不输入邮箱号"""
        findPwd = DAE_FindPwdPage.FindPwd(self.dr)
        findPwd.click_ForgetLoginPwd()
        findPwd.type_email('15273258977')
        findPwd.type_code(None)
        time.sleep(2)
        self.assertTrue(self.dr.get_element(DAE_PromptMessage.NoneCode))