#coding=utf-8

from public.common import basepage
from config import DAE_PersonalCenterPage_Element
from public.common import pyselenium
import time

class PersoalCenter(basepage.Page):
    def __init__(self,dr):
        self.dr = dr
        self.dr.click(DAE_PersonalCenterPage_Element.PersonalCenter_Tab)

    def Switch_AccountInfo(self):
        self.dr.click(DAE_PersonalCenterPage_Element.Account_Tab)

    def Switch_SecuritySetting(self):
        self.dr.click(DAE_PersonalCenterPage_Element.SecuritySetting_Tab)

    def Switch_SecurityPolicy(self):
        self.dr.click(DAE_PersonalCenterPage_Element.SecurityPolicy_Tab)

    def change_nicknaem(self,nickname=''):
        # 修改昵称
        self.dr.click(DAE_PersonalCenterPage_Element.ChangeNickname_Button)
        self.dr.type(DAE_PersonalCenterPage_Element.nickname_Input,nickname)

    def Change_Email(self,Email='',TradePwd='',Vcode='',clicksendcode=True):
        # 修改邮箱
        element = self.dr.get_element(DAE_PersonalCenterPage_Element.ChangeEmail_Button)
        self.dr.click(DAE_PersonalCenterPage_Element.ChangeEmail_Button)
        self.dr.type(DAE_PersonalCenterPage_Element.NewEmail_Input,Email)
        self.Send_Vcode(Vcode,clicksendcode)
        self.Type_TradePwd(TradePwd)

    def Type_TradePwd(self,TradePwd=''):
        # 输入交易密码
        self.dr.type(DAE_PersonalCenterPage_Element.TradePwd_Input,TradePwd)

    def Send_Vcode(self,Vcode='',clicksendcode=True):
        # 发送并输入验证码
        if clicksendcode:
            self.dr.click(DAE_PersonalCenterPage_Element.SendCode_Button)
            self.dr.element_exist(DAE_PersonalCenterPage_Element.SendSuccess).ispdisplay()
        self.dr.type(DAE_PersonalCenterPage_Element.Vcode_Input,Vcode)

    def ChangeLoginPwd(self,OldPwd='',NewPwd= '',ConfirmPwd='',Vcode='',clicksendcode=True):
        # 修改登录密码
        self.dr.click(DAE_PersonalCenterPage_Element.ChangeLoginPwd_Button)
        self.dr.type(DAE_PersonalCenterPage_Element.OldPwd_Input,OldPwd)
        self.dr.type(DAE_PersonalCenterPage_Element.NewPwd_Input,NewPwd)
        self.dr.type(DAE_PersonalCenterPage_Element.ConfirmPwd_Input,ConfirmPwd)
        self.Send_Vcode(Vcode,clicksendcode)

    def ForgetTradePwd_Step1(self,Vcode='',clicksendcode=True):
        # 忘记交易密码第一步
        self.dr.click(DAE_PersonalCenterPage_Element.ForgetCurrencyPwd_Button)
        self.Send_Vcode(Vcode,clicksendcode)
        self.dr.click(DAE_PersonalCenterPage_Element.ConfirmChange)

    def ForgetTradePwd_Step2(self,NewTradePwd='',ConfirmTradePwd=''):
        # 忘记交易密码第二步
        self.dr.type(DAE_PersonalCenterPage_Element.NewTradePwd_Input,NewTradePwd)
        self.dr.type(DAE_PersonalCenterPage_Element.ConfirmTradePwd_Input,ConfirmTradePwd)

    def ChangeTradePwd(self,OldTradePwd='',NewTradePwd='',ConfirmTradePwd=''):
        # 修改交易密码
        self.dr.click(DAE_PersonalCenterPage_Element.ChangeCurrencyPwd_Button)
        self.dr.type(DAE_PersonalCenterPage_Element.OldTradePwd_Input,OldTradePwd)
        self.dr.type(DAE_PersonalCenterPage_Element.NewTradePwd_Input,NewTradePwd)
        self.dr.type(DAE_PersonalCenterPage_Element.ConfirmTradePwd_Input,ConfirmTradePwd)

    def click_CancelButton(self):
        self.dr.click(DAE_PersonalCenterPage_Element.Cancel_Button)

    def click_ConfirmButton(self):
        self.dr.click(DAE_PersonalCenterPage_Element.ConfirmChange)

    # def click_PersonalCenter(self):
    #     time.sleep(5)
    #     self.dr.move_to_element(DAE_PersonalCenterPage_Element.Account_Img)
    #     time.sleep(3)
    #     self.dr.element_wait(DAE_PersonalCenterPage_Element.PersonalCenter_Button)
    #     PC = self.dr.get_element(DAE_PersonalCenterPage_Element.PersonalCenter_Button)
    #     self.dr.ut_highlighted(PC)
    #     self.dr.move_to_element(DAE_PersonalCenterPage_Element.PersonalCenter_Button)
    #     self.dr.click(DAE_PersonalCenterPage_Element.PersonalCenter_Button)
    #
    # def switch_To_SecuritySet(self):
    #     self.dr.click(DAE_PersonalCenterPage_Element.Security_Set)
    #
    # def click_EditTradePwd(self,operation=None,NewWithdrawPwd=None,OldWithdrawPwd=None,ConfirmWithdrawPwd=None,Vcode=None):
    #     self.dr.click(DAE_PersonalCenterPage_Element.Security_Set)
    #     if(self.dr.get_text(DAE_PersonalCenterPage_Element.Pwd_Status)=='未设置'):
    #     # if(self.dr.element_exist(DAE_PersonalCenterPageg_Element.SetWithdrawPwd)):
    #         self.dr.click(DAE_PersonalCenterPage_Element.SetWithdrawPwd)
    #         time.sleep(3)
    #         self.SetWithdrawPwd(NewWithdrawPwd,ConfirmWithdrawPwd,Vcode)
    #     else:
    #         if(operation == 'ForgetPwd'):
    #             self.dr.click(DAE_PersonalCenterPage_Element.ForgetPassword_Link)
    #             self.SendVcode(Vcode)
    #             self.click_Submit()
    #             self.type_NewAndConfirmPwd(NewWithdrawPwd,ConfirmWithdrawPwd)
    #             self.click_Submit()
    #         elif(operation == 'ChagePwd'):
    #             self.dr.click(DAE_PersonalCenterPage_Element.ChangePassword_Link)
    #             self.type_OldTradePwd(OldWithdrawPwd)
    #             self.type_NewAndConfirmPwd(NewWithdrawPwd,ConfirmWithdrawPwd)
    #             self.click_Submit()
    #
    # def type_OldTradePwd(self,OldWithdrawPwd):
    #     self.dr.click(DAE_PersonalCenterPage_Element.OldTradePassword_Input)
    #     self.dr.type(DAE_PersonalCenterPage_Element.OldTradePassword_Input,OldWithdrawPwd)
    #
    # def type_NewAndConfirmPwd(self,NewWithdrawPwd=None,ConfirmPwd=None):
    #     self.dr.click(DAE_PersonalCenterPage_Element.NewTradePassword_Input)
    #     if(NewWithdrawPwd!=None):
    #         self.dr.type(DAE_PersonalCenterPage_Element.NewTradePassword_Input,NewWithdrawPwd)
    #     time.sleep(1)
    #     self.dr.click(DAE_PersonalCenterPage_Element.ConfirmNewTradePassword_Input)
    #     if(ConfirmPwd!=None):
    #         self.dr.type(DAE_PersonalCenterPage_Element.ConfirmNewTradePassword_Input,ConfirmPwd)
    #
    # def click_Submit(self):
    #     submitButton = self.dr.get_element(DAE_PersonalCenterPage_Element.Submit_Button)
    #     submitButton.click()
    #
    # def SendVcode(self,VCode):
    #     self.dr.click(DAE_PersonalCenterPage_Element.SendVCode_Button)
    #     # self.dr.element_wait(DAE_PersonalCenterPageg_Element.SendVCode_Success)
    #     self.dr.click(DAE_PersonalCenterPage_Element.VCode_Input)
    #     if(VCode!=None):
    #         self.dr.type(DAE_PersonalCenterPage_Element.VCode_Input,VCode)
    #
    # def SetWithdrawPwd(self,WithdrawPwd=None,ConfirmWithdrawPwd=None,Vcode=None):
    #     self.dr.click(DAE_PersonalCenterPage_Element.SetTradePassword_Input)
    #     if(WithdrawPwd!=None):
    #         self.dr.type(DAE_PersonalCenterPage_Element.SetTradePassword_Input,WithdrawPwd)
    #     self.dr.click(DAE_PersonalCenterPage_Element.ConfirmTradePassword_Input)
    #     if(ConfirmWithdrawPwd!=None):
    #         self.dr.type(DAE_PersonalCenterPage_Element.ConfirmTradePassword_Input,ConfirmWithdrawPwd)
    #     self.SendVcode(Vcode)
    #     self.click_Submit()
    #     time.sleep(5)