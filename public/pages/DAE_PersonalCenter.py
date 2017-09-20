#coding=utf-8

from public.common import basepage
from config import DAE_PersonalCenterPageg_Element
from public.common import pyselenium

class PersoalCenter(basepage.Page):

    def click_PersonalCenter(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.PersonalCenter_Button)

    def click_SetAndEditTradePwd(self):
        if(self.dr.element_exist(DAE_PersonalCenterPageg_Element.SetWithdrawPwd)):
            self.dr.click(DAE_PersonalCenterPageg_Element.SetWithdrawPwd)
        else:
            self.dr.click(DAE_PersonalCenterPageg_Element.EditTradePassword_Link)

    def click_ChangeTradePwd(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.ChangePassword_Link)

    def type_OldTradePwd(self,OldTradePwd):
        self.dr.type(DAE_PersonalCenterPageg_Element.OldTradePassword_Input,OldTradePwd)

    def type_NewTradePWd(self,NewTradePwd):
        self.dr.type(DAE_PersonalCenterPageg_Element.NewTradePassword_Input,NewTradePwd)

    def type_ConfirmTradePwd(self,ConfirmTradePwd):
        self.dr.type(DAE_PersonalCenterPageg_Element.ConfirmTradePassword_Input,ConfirmTradePwd)

    def click_Submit(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.Submit_Button)

    def click_ForgetTradePwd(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.ForgetPassword_Link)

    def SendVcode(self,VCode):
        self.dr.click(DAE_PersonalCenterPageg_Element.SendVCode_Button)
        self.dr.element_wait(DAE_PersonalCenterPageg_Element.SendVCode_Success)
        self.dr.type(DAE_PersonalCenterPageg_Element.VCode_Input,VCode)

