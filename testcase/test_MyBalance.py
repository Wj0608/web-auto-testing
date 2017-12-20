#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_MyBalancePage
from config import DAE_SuccessMessage,DAE_ErrorMessage,DAE_MyBalancePage_Element
import time
from testcase import test_Register


class TestMyBalance(mytest.MyTest):
    """资产充值提现功能测试"""

    def BTCDeposite(self):
        test_Register.TestHuiyin.test_a_login(self)
        time.sleep(3)
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_BTC_Deposite()
        self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)

    def ETHDeposite(self):
        test_Register.TestHuiyin.test_a_login(self)
        time.sleep(3)
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_ETH_Deposite()
        self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)

    def ETCDeposite(self):
        test_Register.TestHuiyin.test_a_login(self)
        time.sleep(3)
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_ETC_Deposite()
        self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)

    # def test_BTCDeposite(self):
    #     """BTC充值功能测试"""
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     time.sleep(3)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_BTC_Deposite()
    #     self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)
    #     self.assertTrue(self.dr.get_element(DAE_MyBalancePage_Element.CopyAddress_Link).is_displayed())

    # def test_ETHDeposite(self):
    #     """ETH充值功能测试"""
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_ETH_Deposite()
    #     self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)
    #     self.assertTrue(self.dr.get_element(DAE_MyBalancePage_Element.CopyAddress_Link).is_displayed())
    #
    # def test_ETCDeposite(self):
    #     """ETC充值功能测试"""
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_ETC_Deposite()
    #     self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)
    #     self.assertTrue(self.dr.get_element(DAE_MyBalancePage_Element.CopyAddress_Link).is_displayed())

    def test_BTC_CopyPasteAddress(self):
        """提BTC到自己的地址功能测试"""
        # self.test_BTCDeposite()
        self.BTCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('Paste',1,'123456')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())

    def test_ETH_CopyPasteAddress(self):
        """提ETH到自己的地址功能测试"""
        # self.test_ETHDeposite()
        self.ETHDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('Paste',1,'123456')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())

    def test_ETC_CopyPasteAddress(self):
        """提ETC到自己的地址功能测试"""
        # self.test_ETCDeposite()
        self.ETCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('Paste',1,'123456')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())

    def test_BTC_WithdrawWrongPwd(self):
        """提BTC密码错误功能测试"""
        # self.test_BTCDeposite()
        self.BTCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('Paste',1,'456789')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.WrongTradePwd_Error).is_displayed())

    def test_BTC_NullAddress(self):
        """提BTC不输入地址功能测试"""
        # self.test_BTCDeposite()
        self.BTCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite(None,1,'123456')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.InputAddress_Remind).is_displayed())

    def test_BTC_NullPwd(self):
        """提BTC不输入密码功能测试"""
        # self.test_BTCDeposite()
        self.BTCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('fjdhgdfj46178564783vnmcbjkda',1,None)
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.InputPwd_Remind).is_displayed())

    def test_BTC_NullAmount(self):
        """提BTC不输入金额功能测试"""
        # self.test_BTCDeposite()
        self.BTCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('fjdhgdfj46178564783vnmcbjkda',None,'123456')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.InputAmount_Remind).is_displayed())

    def test_BTC_InValidAddress(self):
        """提BTC输入无效地址功能测试"""
        # self.test_BTCDeposite()
        self.BTCDeposite()
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_CopyAddress()
        time.sleep(2)
        myBalancePage.deposite_switch_withdraw()
        myBalancePage.Deposite('12345484562315430032',1,'123456')
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.InValidAddress_Remind).is_displayed())