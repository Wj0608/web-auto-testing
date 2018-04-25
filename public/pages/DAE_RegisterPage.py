#coding=utf-8

from public.common import basepage
from config import DAE_RegisterPage_Element,DAE_SuccessMessage
import time

class RegisterPage(basepage.Page):

    def get_PhoneNumber(self):
        # self.dr.get_attribute(DAE_RegisterPage_Element.Phone_Input,"value")
        phone = self.dr.get_attribute(DAE_RegisterPage_Element.Phone_Input,"value")
        return phone

    def Type_EmailOrPhone(self,EmailOrPhone):
        self.dr.type(DAE_RegisterPage_Element.Phone_Input,EmailOrPhone)

    def Type_VCode(self,VCode):
        self.dr.click(DAE_RegisterPage_Element.SendVCode_Button)
        self.dr.element_wait(DAE_SuccessMessage.SendVCodeSuccess)
        self.dr.type(DAE_RegisterPage_Element.VCode_Input,VCode)

    def Type_LoginAndConfirmPassword(self,Pwd,ConfirmPwd):
        self.dr.type(DAE_RegisterPage_Element.VCode_Input,Pwd)
        time.sleep(1)
        self.dr.type(DAE_RegisterPage_Element.ConfirmPwd_Input,ConfirmPwd)

    def Click_CreateAccount(self):
        submit = self.dr.get_element(DAE_RegisterPage_Element.CreateAccount_Button)
        submit.click()

    def Click_DAEClauseLink(self):
        self.dr.click(DAE_RegisterPage_Element.DAEClause_Link)

    def Login(self):
        self.dr.click(DAE_RegisterPage_Element.Login_Link)

    # def WeChatLogin(self):
    #     self.dr.click(DAE_RegisterPage_Element.WeChatLogin_button)