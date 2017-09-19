#coding=utf-8

from public.common import basepage
from config import DAE_PersonalCenterPageg_Element
from public.common import pyselenium

class DAE_PersoalCenter(basepage.Page):

    def click_EditTradePwd(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.EditTradePassword_Link)

    def click_ChangeTradePwd(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.ChangePassword_Link)

    def click_ForgetTradePwd(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.ForgetPassword_Link)

    def type_OldTradePwd(self,OldTradePwd):
        self.dr.type(DAE_PersonalCenterPageg_Element.OldTradePassword_Input,OldTradePwd)

    def type_NewTradePWd(self,NewTradePwd):
        self.dr.type(DAE_PersonalCenterPageg_Element.NewTradePassword_Input,NewTradePwd)

    def type_ConfirmTradePwd(self,ConfirmTradePwd):
        self.dr.type(DAE_PersonalCenterPageg_Element.ConfirmTradePassword_Input,ConfirmTradePwd)

    def click_Submit(self):
        self.dr.click(DAE_PersonalCenterPageg_Element.Submit_Button)