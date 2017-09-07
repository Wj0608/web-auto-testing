#coding=utf-8

from public.common import basepage
from config import DAE_FirstPage
from public.common import pyselenium

class HuiyinPage(basepage.Page):

    def click_ETH_button(self):
        """点击ETH按钮"""
        self.dr.click(DAE_FirstPage.ETH_Button)

    def click_BTC_button(self):
        """点击BTC按钮"""
        self.dr.click(DAE_FirstPage.BTC_Button)

    def click_PhoneOrEmailLogin_button(self):
        """点击手机或者邮箱登录"""
        self.dr.click(DAE_FirstPage.PhoneOrEmailLogin_Button)

    def click_ForgetPassword_link(self):
        """点击忘记密码"""
        self.dr.click(DAE_FirstPage.ForgetPassword_Link)

    def LoginWithEmailOrPhone(self,EmailOrPhone,Pwd):
        """登录"""
        self.dr.type(DAE_FirstPage.LoginUsername_Input,EmailOrPhone)
        self.dr.type(DAE_FirstPage.LoginPassword_Input,Pwd)
        Submit_Button = self.dr.get_element(DAE_FirstPage.Login_Button)
        Submit_Button.click()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()