#coding=utf-8

from public.common import basepage
from config import DAE_FirstPageElement,DAE_LoginPageElement,DAE_FindPwdPageElement
from public.common import pyselenium

class FindPwd(basepage.Page):

    def click_ForgetLoginPwd(self):
        self.dr.click(DAE_FirstPageElement.Login_Button)
        self.dr.click(DAE_LoginPageElement.ForgetPassword_Link)

    # def type_PhoneAndCaptcha(self,Phone=None,Captcha=None,Vcode=None,Pwd=None,ConfirmPwd=None):
    #     self.dr.type(DAE_ForgetLoginPwdPage_Element.EmailOrPhone_Input,Phone)
    #     self.dr.type(DAE_ForgetLoginPwdPage_Element.PictureVCode_Input,Captcha)
    #     self.click_NextStep()
    #     self.Type_VCode(Vcode)
    #     self.click_NextStep()
    #     self.dr.click(DAE_ForgetLoginPwdPage_Element.LoginPwd_Input)
    #     self.dr.type(DAE_ForgetLoginPwdPage_Element.LoginPwd_Input,Pwd)
    #     self.dr.click(DAE_ForgetLoginPwdPage_Element.ConfirmLoginPwd)
    #     self.dr.type(DAE_ForgetLoginPwdPage_Element.ConfirmLoginPwd,ConfirmPwd)
    #
    # def click_NextStep(self):
    #     self.dr.click(DAE_ForgetLoginPwdPage_Element.NextStep_Button)
    #
    # def Type_VCode(self,VCode):
    #     self.dr.click(DAE_ForgetLoginPwdPage_Element.SendVCode_Button)
    #     self.dr.element_wait(DAE_ForgetLoginPwdPage_Element.SendVCodeSuccess)
    #     self.dr.type(DAE_ForgetLoginPwdPage_Element.VCode_Input,VCode)

    def type_email(self,email):
        self.dr.click(DAE_FindPwdPageElement.email_Input)
        if(email != None):
            self.dr.type(DAE_FindPwdPageElement.email_Input,email)

    def type_code(self,code):
        sendCode_Button = self.dr.get_elements(DAE_FindPwdPageElement.Button)[0]
        sendCode_Button.click()
        if(code != None):
            self.dr.type(DAE_FindPwdPageElement.vcode_Input,code)
        nextstep_Button = self.dr.get_elements(DAE_FindPwdPageElement.Button)[1]
        nextstep_Button.click()

    def type_password(self,password,confirmPassword):
        self.dr.click(DAE_FindPwdPageElement.password_Input)
        if(password != None):
            self.dr.type(DAE_FindPwdPageElement.password_Input,password)
        self.dr.type(DAE_FindPwdPageElement.passwordConfirm_Input)
        if(confirmPassword != None):
            self.dr.type(DAE_FindPwdPageElement.passwordConfirm_Input,confirmPassword)
        nextStep_Button = self.dr.get_element(DAE_FindPwdPageElement.Button)
        nextStep_Button.click()