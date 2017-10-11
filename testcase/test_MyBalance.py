#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_MyBalancePage
from config import DAE_SuccessMessage,DAE_ErrorMessage,DAE_MyBalancePage_Element
import time
from testcase import test_RegisterAndLogin

class TestMyBalance(mytest.MyTest):

    def test_BTCDeposite(self):
        test_RegisterAndLogin.TestHuiyin.test_a_login(self)
        myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
        myBalancePage.click_BTC_Deposite()
        self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)
        self.assertEqual(self.dr.get_text((DAE_MyBalancePage_Element.Deposite_Address)),'充值地址：')
    #
    # def test_ETHDeposite(self):
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_ETH_Deposite()
    #     self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)
    #     self.assertEqual(self.dr.get_text((DAE_MyBalancePage_Element.Deposite_Address)),'充值地址：')
    #
    # def test_ETCDeposite(self):
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_ETC_Deposite()
    #     self.dr.element_wait(DAE_MyBalancePage_Element.Deposite_Address)
    #     self.assertEqual(self.dr.get_text((DAE_MyBalancePage_Element.Deposite_Address)),'充值地址：')
    #
    # def test_BTCCurrencyDeposite(self):
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_BTC_Withdraw()
    #     myBalancePage.Deposite('mwCULfHpkYvPZiV6Tc5TUmLPDs7o9RSb8X',1,'123456')
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())
    #
    # def test_ETHCurrencyDeposite(self):
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_ETH_Withdraw()
    #     myBalancePage.Deposite('0x6575ee991fc8b7fa5350588d44ba7476c7bd6fcc',1,'123456')
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())
    #
    # def test_ETCCurrencyDeposite(self):
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_ETC_Withdraw()
    #     myBalancePage.Deposite('0x9ba1092e90052acb8d7b28ea13c113bdaf122702',1,'123456')
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())
    #
    # def test_CopyPasteAddress(self):
    #     test_RegisterAndLogin.TestHuiyin.test_a_login(self)
    #     myBalancePage = DAE_MyBalancePage.MyBalance(self.dr)
    #     myBalancePage.click_CopyAddress()
    #     myBalancePage.deposite_switch_withdraw()
    #     myBalancePage.Deposite('Paste',1,'123456')
    #     self.assertTrue(self.dr.get_element(DAE_ErrorMessage.CannotInputMyselfAddress_Error).is_displayed())
