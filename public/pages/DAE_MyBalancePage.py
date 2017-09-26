#coding=utf-8

from public.common import basepage
from config import DAE_MyBalancePage_Element
from public.common import pyselenium
import time

class MyBalance(basepage.Page):
    def click_BTCDepositeButton(self):
        self.dr.click(DAE_MyBalancePage_Element.BTCDeposite_Link)

    def click_ETHDepositeButton(self):
        self.dr.click(DAE_MyBalancePage_Element.ETHDeposite_Link)

    def click_ETCDepositeButton(self):
        self.dr.click(DAE_MyBalancePage_Element.ETCDeposite_Link)

    def click_WithdrawButton(self,Currency,Address,Amount,Pwd):
        if(Currency=='BTC'):
            self.dr.click(DAE_MyBalancePage_Element.BTCBalance)
        elif(Currency=='ETH'):
            self.dr.click(DAE_MyBalancePage_Element.ETHBalance)
        elif(Currency=='ETC'):
            self.dr.click(DAE_MyBalancePage_Element.ETCBalance)
        self.dr.click(DAE_MyBalancePage_Element.Withdraw_Button)
        self.dr.click(DAE_MyBalancePage_Element.Address_Input)
        self.type_DepositeAddress(Address,Amount,Pwd)

    def type_DepositeAddress(self,Address,Amount,Pwd):
        self.dr.click(DAE_MyBalancePage_Element.Address_Input)
        self.dr.type(DAE_MyBalancePage_Element.Address_Input,Address)
        self.dr.click(DAE_MyBalancePage_Element.Amount_Input)
        self.dr.type(DAE_MyBalancePage_Element.Amount_Input,Amount)
        self.dr.click(DAE_MyBalancePage_Element.Password_Input)
        self.dr.type(DAE_MyBalancePage_Element.Password_Input,Pwd)
        self.click_SubmitButton()

    def copy_PastAddress(self):
        self.dr.click(DAE_MyBalancePage_Element.BTCBalance)
        self.dr.click(DAE_MyBalancePage_Element.CopyAddress_Link)
        self.dr.element_wait(DAE_MyBalancePage_Element.Copy_Success)
        self.dr.click(DAE_MyBalancePage_Element.Withdraw_Button)
        self.dr.paste(DAE_MyBalancePage_Element.Address_Input)
        self.dr.click(DAE_MyBalancePage_Element.Amount_Input)

    # def type_WithdrawAmount(self,Amount):
    #     self.dr.type(DAE_MyBalancePage_Element.Amount_Input,Amount)
    #
    # def type_WithdrawPwd(self,Pwd):
    #     self.dr.type(DAE_MyBalancePage_Element.Password_Input,Pwd)

    def click_SubmitButton(self):
        submit_Button = self.dr.get_element(DAE_MyBalancePage_Element.Submit_Button)
        submit_Button.click()