#coding=utf-8

from public.common import basepage
from config import DAE_RegisterPage_Element
import time

class RegisterPage(basepage.Page):

    def Type_EmailOrPhone(self,EmailOrPhone):
        self.dr.type(DAE_RegisterPage_Element.EmailOrPhone_Input,EmailOrPhone)

    def Type_VCode(self,VCode):
        self.dr.click(DAE_RegisterPage_Element.SendVCode_Button)
        self.dr.element_wait(DAE_RegisterPage_Element.SendVCode_Button_Success)
        self.dr.type(DAE_RegisterPage_Element.VCode_Input,VCode)

    def Type_LoginAndConfirmPassword(self,Pwd,ConfirmPwd):
        self.dr.type(DAE_RegisterPage_Element.VCode_Input,Pwd)
        time.sleep(1)
        self.dr.type(DAE_RegisterPage_Element.ConfirmPassword_Input,ConfirmPwd)

    def Click_CreateAccount(self):
        self.dr.click(DAE_RegisterPage_Element.CreateAccount_Button)

    def Click_DAEClauseLink(self):
        self.dr.click(DAE_RegisterPage_Element.DAEClause_Link)

    def Login(self):
        self.dr.click(DAE_RegisterPage_Element.Login_link)

    def WeChatLogin(self):
        self.dr.click(DAE_RegisterPage_Element.WeChatLogin_button)