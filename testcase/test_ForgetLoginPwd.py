#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_ForgetLoginPwdPage
from config import DAE_SuccessMessage,DAE_ErrorMessage
import time
from testcase import test_RegisterAndLogin

class ForgetLoginPwd(mytest.MyTest):
    def test_ForgetLoginPwd(self):
        forgetPwd = DAE_ForgetLoginPwdPage.ForgetLoginPwd(self)
        forgetPwd.click_ForgetLoginPwd()
        forgetPwd.type_PhoneAndCaptcha()
        time.sleep(2)
        self.assertEqual(self.dr.get_url(),)

