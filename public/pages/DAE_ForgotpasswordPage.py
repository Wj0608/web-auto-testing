from config import Forgot_password
from public.common import basepage
from public.common import publicfunction
import time
class DAEForgotpasswordPage(basepage.Page):
    def Forgot_password_step1(self,Username,Vcode):
        self.dr.click(Forgot_password.click_Forgot_password)
        self.dr.type(Forgot_password.send_username,Username)
        time.sleep(3)
        self.dr.click(Forgot_password.click_vcode)
        self.dr.type(Forgot_password.send_vcode,Vcode)
        self.dr.click(Forgot_password.click_next)
    def Forgot_password_step2(self,new_password,confirm_new_password):
        self.dr.type(Forgot_password.send_new_password,new_password)
        self.dr.type(Forgot_password.send_confirm_new_password,confirm_new_password)
        self.dr.click(Forgot_password.click_reset)
        time.sleep(2)
