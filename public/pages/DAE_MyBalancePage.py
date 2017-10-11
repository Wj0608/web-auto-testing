#coding=utf-8

from public.common import basepage
from config import DAE_MyBalancePage_Element
from public.common import pyselenium
import time
from selenium.webdriver.common.keys import Keys

class MyBalance(basepage.Page):
    def click_BTC_Withdraw(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_BTC_Withdraw)

    def click_BTC_Deposite(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_BTC_Deposite)

    def click_ETH_Withdraw(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_ETH_Withdraw)

    def click_ETH_Deposite(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_ETH_Deposite)

    def click_ETC_Withdraw(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_ETC_Withdraw)

    def click_ETC_Deposite(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_ETC_Deposite)

    def withdraw_switch_deposite(self):
        self.dr.click(DAE_MyBalancePage_Element.TabBar_Deposite)

    def deposite_switch_withdraw(self):
        self.dr.click(DAE_MyBalancePage_Element.TabBar_Withdraw)

    def click_SideBarBTC(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_BTC_Deposite)

    def click_SideBarETH(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_ETH_Deposite)

    def click_SideBarETC(self):
        self.dr.click(DAE_MyBalancePage_Element.MyBalance_ETC_Deposite)

    # def click_WithdrawButton(self,Currency,Address,Amount,Pwd):
    #     if(Currency=='BTC'):
    #         self.dr.click(DAE_MyBalancePage_Element.SideBar_BTC)
    #     elif(Currency=='ETH'):
    #         self.dr.click(DAE_MyBalancePage_Element.SideBar_ETH)
    #     elif(Currency=='ETC'):
    #         self.dr.click(DAE_MyBalancePage_Element.SideBar_ETC)
    #     self.dr.click(DAE_MyBalancePage_Element.Withdraw_Button)
    #     self.dr.click(DAE_MyBalancePage_Element.Address_Input)
    #     self.type_DepositeAddress(Address,Amount,Pwd)

    def Deposite(self,Address,Amount,Pwd):
        self.dr.click(DAE_MyBalancePage_Element.Address_Input)
        if(Address=='Paste'):
            address_Input = self.dr.get_element(DAE_MyBalancePage_Element.Address_Input)
            address_Input.send_Keys(Keys.CONTROL,'v')
        self.dr.type(DAE_MyBalancePage_Element.Address_Input,Address)
        self.dr.click(DAE_MyBalancePage_Element.Amount_Input)
        self.dr.type(DAE_MyBalancePage_Element.Amount_Input,Amount)
        self.dr.click(DAE_MyBalancePage_Element.Password_Input)
        self.dr.type(DAE_MyBalancePage_Element.Password_Input,Pwd)
        self.click_SubmitButton()

    def click_CopyAddress(self):
        self.dr.click(DAE_MyBalancePage_Element.CopyAddress_Link)
        self.dr.element_wait(DAE_MyBalancePage_Element.Copy_Success)

    # def type_WithdrawAmount(self,Amount):
    #     self.dr.type(DAE_MyBalancePage_Element.Amount_Input,Amount)
    #
    # def type_WithdrawPwd(self,Pwd):
    #     self.dr.type(DAE_MyBalancePage_Element.Password_Input,Pwd)

    def click_SubmitButton(self):
        submit_Button = self.dr.get_element(DAE_MyBalancePage_Element.Submit_Button)
        submit_Button.click()