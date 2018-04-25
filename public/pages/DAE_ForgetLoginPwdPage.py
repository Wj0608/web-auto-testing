#coding=utf-8

from public.common import basepage
from config import DAE_FirstPage_Element,DAE_ForgetLoginPwdPage_Element
from public.common import pyselenium

class ForgetLoginPwd(basepage.Page):

    def type_PhoneAndCaptcha(self,Email=None,Vcode='',Pwd='',ConfirmPwd=''):
        self.dr.type(DAE_ForgetLoginPwdPage_Element.Email_Input,Email)
        self.dr.click(DAE_ForgetLoginPwdPage_Element.SendCode_Button)
        self.dr.type(DAE_ForgetLoginPwdPage_Element.VCode_Input,Vcode)
        self.click_NextStep()
        self.dr.click(DAE_ForgetLoginPwdPage_Element.Password_Input)
        self.dr.type(DAE_ForgetLoginPwdPage_Element.Password_Input,Pwd)
        self.dr.click(DAE_ForgetLoginPwdPage_Element.PasswordConfirm_Input)
        self.dr.type(DAE_ForgetLoginPwdPage_Element.PasswordConfirm_Input,ConfirmPwd)

    def click_NextStep(self):
        self.dr.click(DAE_ForgetLoginPwdPage_Element.NextStep_Button)

    def Type_VCode(self,VCode):
        self.dr.click(DAE_ForgetLoginPwdPage_Element.SendVCode_Button)
        self.dr.element_wait(DAE_ForgetLoginPwdPage_Element.SendVCodeSuccess)
        self.dr.type(DAE_ForgetLoginPwdPage_Element.VCode_Input,VCode)
