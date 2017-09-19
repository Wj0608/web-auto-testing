#coding=utf-8

from public.common import basepage
from config import DAE_FirstPage_Element
from public.common import pyselenium

class DAEFirstPage(basepage.Page):

    # def click_ETH_button(self):
    #     """点击ETH按钮"""
    #     self.dr.click(DAE_FirstPage_Element.ETH_Button)
    #
    # def click_BTC_button(self):
    #     """点击BTC按钮"""
    #     self.dr.click(DAE_FirstPage_Element.BTC_Button)

    def click_PhoneOrEmailLogin_button(self):
        """点击手机或者邮箱登录"""
        self.dr.click(DAE_FirstPage_Element.HeaderLogin_Button)

    def click_ForgetPassword_link(self):
        """点击忘记密码"""
        self.dr.click(DAE_FirstPage_Element.ForgetPassword_Link)

    def LoginWithEmailOrPhone(self,EmailOrPhone,Pwd):
        """登录"""
        self.dr.type(DAE_FirstPage_Element.LoginUsername_Input,EmailOrPhone)
        self.dr.type(DAE_FirstPage_Element.LoginPassword_Input,Pwd)
        Submit_Button = self.dr.get_element(DAE_FirstPage_Element.Login_Button)
        Submit_Button.click()

    def click_RegisterButton(self):
        self.dr.click(DAE_FirstPage_Element.HeaderRegister_Button)

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()