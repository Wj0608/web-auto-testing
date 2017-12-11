#coding=utf-8

from public.common import basepage
from config import DAE_PersonalCenterPageg_Element
from public.common import pyselenium
import time
from selenium.webdriver.common.action_chains import ActionChains

class PersoalCenter(basepage.Page):

    def click_PersonalCenter(self):
        action = ActionChains(self.dr)
        PC = self.dr.get_element(DAE_PersonalCenterPageg_Element.Account_Img)
        action.move_to_element(PC).perform()
        time.sleep(3)
        self.dr.element_wait(DAE_PersonalCenterPageg_Element.PersonalCenter_Button)
        # self.dr.click(DAE_PersonalCenterPageg_Element.PersonalCenter_Button)

    def switch_To_SecuritySet(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.Security_Set)

    def click_EditTradePwd(self,operation=None,NewWithdrawPwd=None,OldWithdrawPwd=None,ConfirmWithdrawPwd=None,Vcode=None):
        self.dr.click(DAE_PersonalCenterPageg_Element.Security_Set)
        if(self.dr.get_text(DAE_PersonalCenterPageg_Element.Pwd_Status)=='未设置'):
        # if(self.dr.element_exist(DAE_PersonalCenterPageg_Element.SetWithdrawPwd)):
            self.dr.click(DAE_PersonalCenterPageg_Element.SetWithdrawPwd)
            time.sleep(3)
            self.SetWithdrawPwd(NewWithdrawPwd,ConfirmWithdrawPwd,Vcode)
        else:
            if(operation == 'ForgetPwd'):
                self.dr.click(DAE_PersonalCenterPageg_Element.ForgetPassword_Link)
                self.SendVcode(Vcode)
                self.click_Submit()
                self.type_NewAndConfirmPwd(NewWithdrawPwd,ConfirmWithdrawPwd)
                self.click_Submit()
            elif(operation == 'ChagePwd'):
                self.dr.click(DAE_PersonalCenterPageg_Element.ChangePassword_Link)
                self.type_OldTradePwd(OldWithdrawPwd)
                self.type_NewAndConfirmPwd(NewWithdrawPwd,ConfirmWithdrawPwd)
                self.click_Submit()

    def type_OldTradePwd(self,OldWithdrawPwd):
        self.dr.click(DAE_PersonalCenterPageg_Element.OldTradePassword_Input)
        self.dr.type(DAE_PersonalCenterPageg_Element.OldTradePassword_Input,OldWithdrawPwd)

    def type_NewAndConfirmPwd(self,NewWithdrawPwd=None,ConfirmPwd=None):
        self.dr.click(DAE_PersonalCenterPageg_Element.NewTradePassword_Input)
        if(NewWithdrawPwd!=None):
            self.dr.type(DAE_PersonalCenterPageg_Element.NewTradePassword_Input,NewWithdrawPwd)
        time.sleep(1)
        self.dr.click(DAE_PersonalCenterPageg_Element.ConfirmNewTradePassword_Input)
        if(ConfirmPwd!=None):
            self.dr.type(DAE_PersonalCenterPageg_Element.ConfirmNewTradePassword_Input,ConfirmPwd)

    def click_Submit(self):
        submitButton = self.dr.get_element(DAE_PersonalCenterPageg_Element.Submit_Button)
        submitButton.click()

    def SendVcode(self,VCode):
        self.dr.click(DAE_PersonalCenterPageg_Element.SendVCode_Button)
        # self.dr.element_wait(DAE_PersonalCenterPageg_Element.SendVCode_Success)
        self.dr.click(DAE_PersonalCenterPageg_Element.VCode_Input)
        if(VCode!=None):
            self.dr.type(DAE_PersonalCenterPageg_Element.VCode_Input,VCode)

    def SetWithdrawPwd(self,WithdrawPwd=None,ConfirmWithdrawPwd=None,Vcode=None):
        self.dr.click(DAE_PersonalCenterPageg_Element.SetTradePassword_Input)
        if(WithdrawPwd!=None):
            self.dr.type(DAE_PersonalCenterPageg_Element.SetTradePassword_Input,WithdrawPwd)
        self.dr.click(DAE_PersonalCenterPageg_Element.ConfirmTradePassword_Input)
        if(ConfirmWithdrawPwd!=None):
            self.dr.type(DAE_PersonalCenterPageg_Element.ConfirmTradePassword_Input,ConfirmWithdrawPwd)
        self.SendVcode(Vcode)
        self.click_Submit()
        time.sleep(5)