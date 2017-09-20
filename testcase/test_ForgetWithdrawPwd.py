#coding=utf-8


from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_PersonalCenter
from config import DAE_SuccessMessage,DAE_ErrorMessage

from testcase import test_RegisterAndLogin

class TestWithdrawPwd(mytest.MyTest):

    # 修改提现密码
    def test_a_ChangeWithdrawPwd(self):
        test_RegisterAndLogin.TestHuiyin.test_a_login(self)
        personalPage = DAE_PersonalCenter.PersoalCenter(self.dr)
        personalPage.click_PersonalCenter()
        personalPage.click_SetAndEditTradePwd()
        personalPage.click_ChangeTradePwd()
        personalPage.type_OldTradePwd('123456')
        personalPage.type_NewTradePWd('123456')
        personalPage.type_ConfirmTradePwd('123456')
        personalPage.click_Submit()
        self.assertTrue(self.dr.get_element(DAE_SuccessMessage.ChangePwdSuccess).is_displayed())

    # 忘记提币密码
    def test_b_ForgetWithdrawPwd(self):
        test_RegisterAndLogin.TestHuiyin.test_a_login(self)
        persoanlPage = DAE_PersonalCenter.PersoalCenter(self.dr)
        persoanlPage.click_SetAndEditTradePwd()
        persoanlPage.click_ForgetTradePwd()
        persoanlPage.SendVcode('123456')
        persoanlPage.click_Submit()
        persoanlPage.type_NewTradePWd('123456')
        persoanlPage.type_ConfirmTradePwd('123456')
        persoanlPage.click_Submit()
        self.assertEqual(self.dr.get_url(),'http://pre-www.szjys.com/user-center/transaction-password')

    # 修改提现密码-原密码错误
    def test_a_ChangeWithdrawPwdWrongOldPwd(self):
        test_RegisterAndLogin.TestHuiyin.test_a_login(self)
        personalPage = DAE_PersonalCenter.PersoalCenter(self.dr)
        personalPage.click_PersonalCenter()
        personalPage.click_SetAndEditTradePwd()
        personalPage.click_ChangeTradePwd()
        personalPage.type_OldTradePwd('7894561')
        personalPage.type_NewTradePWd('123456')
        personalPage.type_ConfirmTradePwd('123456')
        personalPage.click_Submit()
        self.assertTrue(self.dr.get_element(DAE_ErrorMessage.OldWithdrawPwd_Error).is_displayed())

    # 修改提现密码-确认密码与新密码不同
    def test_a_DifferentConfirmPwd(self):
       test_RegisterAndLogin.TestHuiyin.test_a_login(self)
       personalPage = DAE_PersonalCenter.PersoalCenter(self.dr)
       personalPage.click_PersonalCenter()
       personalPage.click_SetAndEditTradePwd()
       personalPage.click_ChangeTradePwd()
       personalPage.type_OldTradePwd('7894561')
       personalPage.type_NewTradePWd('123456')
       personalPage.type_ConfirmTradePwd('123456')
       personalPage.click_Submit()
       self.assertTrue(self.dr.get_element(DAE_ErrorMessage.DifferentPwd_Error).is_displayed())

    # # 修改提现密码-不输入新密码
    # def test_a_NotInputPwd(self):

