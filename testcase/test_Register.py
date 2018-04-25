#coding=utf-8


from time import sleep
from public.common import mytest,datainfo
from public.common import publicfunction
from public.pages import DAE_LoginPage,DAE_RegisterPage
from config import DAE_PromptMessage,DAE_RegisterPage_Element,DAE_SuccessMessage
import time

class TestHuiyin(mytest.MyTest):
    """DAE注册登录功能测试"""

    def test_open(self):
         """打开首页"""
         huiyinpage = huiyinPage.HuiyinPage(self.dr)
         publicfunction.get_img(self.dr,'111.png')

    def test_ETH_button(self):
        """点击ETH按钮"""
        huiyinpage = huiyinPage.HuiyinPage(self.dr)
        huiyinpage.click_ETH_button()
        sleep(2)
        self.assertIn(u'1ETH=¥ ',self.dr.get_text(assert_element.ETH_button_assert))

    def test_XRP_button(self):
        """点击XRP按钮"""
        huiyinpage = huiyinPage.HuiyinPage(self.dr)
        huiyinpage.click_XRP_button()
        self.assertIn(u'1XRP=¥ ',self.dr.get_text(assert_element.XRP_button_assert))

    def test_PhoneOrEmailLogin_button(self):
        """点击手机或邮箱登录按钮"""
        firstpage = DAE_FirstPage.HuiyinPage(self.dr)
        firstpage.click_PhoneOrEmailLogin_button()
        self.assertEqual(u'请输入邮箱/手机号 ',self.dr.get_attribute(assert_element.PhoneOrEmailLogin_button_assert))

    # 手机注册
    def test_a_PhoneRegister(self):
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.type_PhoneNumber('18774389630')
        firstPage.click_Register_Button()
        register = DAE_RegisterPage.RegisterPage(self.dr)
        self.dr.element_wait(DAE_RegisterPage_Element.DAEClause_Link)
        if(register.get_PhoneNumber()== '18774389630'):
            register.Type_VCode('123456')
            register.Type_LoginAndConfirmPassword('test123','test123')
          #  register.Click_CreateAccount()
        # print(self.dr.get_element(DAE_RegisterPage_Element.RegisterSuccess).is_displayed())
        self.assertTrue(self.dr.get_element(DAE_SuccessMessage.RegisterSuccess).is_displayed())


    res = datainfo.get_xls_to_dict('testdata.xlsx','Sheet1')
