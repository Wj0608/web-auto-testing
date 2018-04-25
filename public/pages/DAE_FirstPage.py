#coding=utf-8

from public.common import basepage
from config import DAE_FirstPageElement,DAE_LoginPageElement,globalparam
from public.common import pyselenium
import time
import urllib.request

class DAELogin(basepage.Page):

    def click_HeaderLogin_button(self):
        # 点击头部登录
        self.dr.click(DAE_FirstPageElement.Login_Button)

    def click_HeaderRegisterButton(self):
        # 点击头部注册
        self.dr.click(DAE_FirstPageElement.Register_Button)

    def click_InstantRegister(self):
        # 点击立即注册
        self.dr.click(DAE_FirstPageElement.InstantRegister_Button)

    def type_Email(self,email):
        # 输入邮箱号
        self.dr.type_and_enter(DAE_LoginPageElement.Email_Input,email)
        return email

    def type_Code(self,code):
        self.dr.click(DAE_LoginPageElement.Button)
        self.dr.type_and_enter(DAE_LoginPageElement.Email_Input)

    def type_password(self,password):
        # 输入密码
        self.dr.click(DAE_LoginPageElement.Password_Input)
        self.dr.type(DAE_LoginPageElement.Password_Input,password)

    def type_ImageCode(self,email):
        # 输入图形验证码
        elements = self.dr.get_elements(DAE_LoginPageElement.ImageCode)
        string = []
        for element in elements:
            text = element.text
            string.append(text)
        self.dr.type(DAE_LoginPageElement.ImageCode_Input,string)
        time.sleep(5)
        req = urllib.request.Request(globalparam.Interface_address + 'secStrategy/getUserLoginSecStrategy?username=%s'% email)
        req.add_header('authorization','Basic  YnJvd3Nlcjo=')
        req.add_header('content-type','application/json')
        res_data = urllib.request.urlopen(req)
        res = res_data.read().decode('utf-8')
        if res == 'true':
            self.email_Verification()
        else:
            register_Button = self.dr.get_element(DAE_LoginPageElement.Button)
            register_Button.click()

    def email_Verification(self):
        # 输入邮箱验证码
        sendCode_Button = self.dr.get_elements(DAE_LoginPageElement.Button)[0]
        sendCode_Button.click()
        self.dr.type(DAE_LoginPageElement.emailCode_Input,'123456')
        time.sleep(3)
        register_Button = self.dr.get_elements(DAE_LoginPageElement.Button)[1]
        register_Button.click()

    def click_ForgetPassword_link(self):
        # 点击忘记密码
        self.dr.click(DAE_LoginPageElement.ForgetPassword_Link)

    def click_FreeRegister_link(self):
        # 点击免费注册
        self.dr.click(DAE_LoginPageElement.FreeRegister_Link)

    def return_title(self):
        # 返回该页面的title
        return self.dr.get_title()