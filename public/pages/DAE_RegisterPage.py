#coding=utf-8

from public.common import basepage
from config import DAE_FirstPageElement,DAE_RegisterPageElement
import time

class RegisterPage(basepage.Page):
    def Type_nickName(self,nickName):
        self.dr.type_and_enter(DAE_RegisterPageElement.nickName_Input,nickName)

    def Type_Email(self,Eamil):
        self.dr.type_and_enter(DAE_RegisterPageElement.email_Input,Eamil)

    def Type_VCode(self,VCode):
        Button = self.dr.get_elements(DAE_RegisterPageElement.sendCode_Button)[0]
        Button.click()
        #self.dr.element_wait(DAE_RegisterPageElement.SendVCodeSuccess)
        self.dr.type(DAE_RegisterPageElement.vCode_Input,VCode)

    def click_NextStep(self):
        nextStep = self.dr.get_elements(DAE_RegisterPageElement.sendCode_Button)[1]
        nextStep.click()

    def setPassword(self,password,passwordConfirm):
        self.dr.click(DAE_RegisterPageElement.password_Input)
        self.dr.type(DAE_RegisterPageElement.password_Input,password)
        self.dr.click(DAE_RegisterPageElement.passwordConfirm_Input)
        self.dr.type(DAE_RegisterPageElement.passwordConfirm_Input,passwordConfirm)

    def Type_ImageCode(self):
        elements = self.dr.get_elements(DAE_RegisterPageElement.ImageCode)
        string = []
        for element in elements:
            text = element.text
            string.append(text)
        self.dr.type(DAE_RegisterPageElement.imageCode_Input,string)

    def click_register(self):
        Button = self.dr.get_element(DAE_RegisterPageElement.sendCode_Button)
        Button.click()