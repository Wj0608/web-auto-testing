#coding=utf-8

from public.common import basepage,APIUtil
from config import DAE_LoginPage_Element
from public.common import pyselenium
import time

class DAEFirstPage(basepage.Page):
    def __init__(self, driver):
        self.dr = driver
        self.dr.click(DAE_LoginPage_Element.HeaderLogin_Button)
        self.Email = ''
        self.Password = ''

    def Login(self,email,password):
        """登录"""
        self.Email = email
        self.Password = password
        self.dr.click(DAE_LoginPage_Element.Email_Input)
        self.dr.type(DAE_LoginPage_Element.Email_Input,self.Email)
        self.dr.click(DAE_LoginPage_Element.Password_Input)
        self.dr.type(DAE_LoginPage_Element.Password_Input,self.Password)

    def click_SigninButton(self,smsCode=''):
        """点击登录按钮"""
        #获取登录token
        url_token ="/uaa/oauth/token"
        para_token = {"grant_type":"password","password":self.Password,"scope":"ui","source":"standard","username":self.Email}
        header_token = {'Content-Type':'application/x-www-form-urlencoded', 'authorization':'Basic YnJvd3Nlcjo=',"origin":"https://pre-www.dae.org"}
        response = APIUtil.post_kv(url_token, para_token, header_token)
        self.dr.click(DAE_LoginPage_Element.SignIn_Button)
        #用户开启二次验证
        Code = APIUtil.ResponseCode(response)
        if APIUtil.ResponseCode(response)== 403:
            mfa_token = APIUtil.json_to_python(response)['mfa_token']
            #获取二次验证方式
            url_challenge = "/uaa/mfa/challenge"
            para_challenge = {'challenge_type':'otp|oob','mfa_token':mfa_token}
            header_challenge = {'Content-Type':'application/json',"origin":"https://pre-www.dae.org"}
            response_challenge = APIUtil.post_json(url_challenge, para_challenge, header_challenge)
            #用户开启了短信验证码
            if str(APIUtil.json_to_python(response_challenge)['challenge_types'])== '[\'oob\']':
                self.dr.click(DAE_LoginPage_Element.Send_VCode)
                time.sleep(2)
                self.dr.type(DAE_LoginPage_Element.SMSCode_Input,smsCode)
                self.dr.click(DAE_LoginPage_Element.Submit_Button)
            # 用户开启了谷歌验证码
            # if str(APIUtil.json_to_python(response_challenge)['challenge_types'])== '[\'otp\']':


    # def click_Register_Button(self):
    #     button = self.dr.get_element(DAE_FirstPage_Element.Submit_Button)
    #     button.click()
    #
    # def click_ForgetPassword_link(self):
    #     """点击忘记密码"""
    #     self.dr.click(DAE_FirstPage_Element.ForgetPwd_Link)
    #
    # def click_LoginImmediately(self):
    #     self.dr.click(DAE_FirstPage_Element.Login_Link)
    #
    # def Login(self,EmailOrPhone,Pwd):
    #     """登录"""
    #     time.sleep(2)
    #     self.dr.element_wait(DAE_FirstPage_Element.LoginUsername_Input)
    #     self.dr.click(DAE_FirstPage_Element.LoginUsername_Input)
    #     self.dr.type(DAE_FirstPage_Element.LoginUsername_Input,EmailOrPhone)
    #     self.dr.click(DAE_FirstPage_Element.LoginPwd_Input)
    #     self.dr.type(DAE_FirstPage_Element.LoginPwd_Input,Pwd)
    #     Submit_Button = self.dr.get_element(DAE_FirstPage_Element.Submit_Button)
    #     Submit_Button.click()

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()