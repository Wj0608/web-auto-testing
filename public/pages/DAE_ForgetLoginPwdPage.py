#coding=utf-8

from public.common import basepage
from config import DAE_FirstPage_Element
from public.common import pyselenium

class ForgetLoginPwd(basepage.Page):
    def type_PhoneOrEmail(self):
        self.dr.type()