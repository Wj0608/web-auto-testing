#coding=utf-8

from public.common import basepage
from config import DAE_RegisterPage_Element,DAE_SuccessMessage
import time
from public.common import publicfunction

class RegisterPage(basepage.Page):
        def Register1(self,Nickname,Email,Scode):
            self.dr.click(DAE_RegisterPage_Element.click_sign_up)
            self.dr.type(DAE_RegisterPage_Element.NickName_Input,Nickname)
            self.dr.type(DAE_RegisterPage_Element.Email_Input,Email)
            self.dr.click(DAE_RegisterPage_Element.click_Code_Button)
            self.dr.type(DAE_RegisterPage_Element.VCode_Input,Scode)
            self.dr.click(DAE_RegisterPage_Element.Submit_Button)

        def Register2(self,passwors,Confirm_password):
            self.dr.type(DAE_RegisterPage_Element.Password_Input,passwors)
            self.dr.type(DAE_RegisterPage_Element.PasswordConfirm_Input,Confirm_password)
            self.dr.click(DAE_RegisterPage_Element.Register_Button)
            #publicfunction.get_img(self.dr, 'mismatch password')

