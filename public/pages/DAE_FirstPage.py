#coding=utf-8

from public.common import basepage
from config import DAE_FirstPage_Element
from public.common import pyselenium

class DAEFirstPage(basepage.Page):

    def click_HeaderLogin_button(self):
        """点击手机或者邮箱登录"""
        self.dr.click(DAE_FirstPage_Element.HeaderLogin_Button)

    def click_HeaderRegisterButton(self):
        self.dr.click(DAE_FirstPage_Element.HeaderRegister_Button)

    def type_PhoneNumber(self,PhoneNumber):
        """输入手机号"""
        self.dr.click(DAE_FirstPage_Element.LoginUsername_Input)
        self.dr.type(DAE_FirstPage_Element.LoginUsername_Input,PhoneNumber)

    def click_Register_Button(self):
        button = self.dr.get_element(DAE_FirstPage_Element.Submit_Button)
        button.click()

    def click_ForgetPassword_link(self):
        """点击忘记密码"""
        self.dr.click(DAE_FirstPage_Element.ForgetPwd_Link)

    def click_LoginImmediately(self):
        self.dr.click(DAE_FirstPage_Element.Login_Link)

    def Login(self,EmailOrPhone,Pwd):
        """登录"""
        self.dr.element_wait(DAE_FirstPage_Element.LoginUsername_Input)
        self.dr.click(DAE_FirstPage_Element.LoginUsername_Input)
        self.dr.type(DAE_FirstPage_Element.LoginUsername_Input,EmailOrPhone)
        self.dr.click(DAE_FirstPage_Element.LoginPwd_Input)
        self.dr.type(DAE_FirstPage_Element.LoginPwd_Input,Pwd)
        Submit_Button = self.dr.get_element(DAE_FirstPage_Element.Submit_Button)
        Submit_Button.click()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()