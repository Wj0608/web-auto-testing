#coding=utf-8


from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import DAE_FirstPage,DAE_RegisterPage
from config import DAE_FirstPage_Element,DAE_RegisterPage_Element,DAE_ForgetLoginPwdPage_Element
from public.common import datainfo
from config import assert_element

class TestLoginPwd(mytest.MyTest):
    def type_PhoneOrEmail(self,PhoneOrEmail):
        self.dr.type(DAE_ForgetLoginPwdPage_Element.EmailOrPhone_Input,PhoneOrEmail)