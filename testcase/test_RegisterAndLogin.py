#coding=utf-8
from time import sleep
from public.common import mytest,datainfo
from public.common import publicfunction
from public.pages import DAE_FirstPage,DAE_RegisterPage
from config import DAE_ErrorMessage,DAE_RegisterPage_Element,DAE_SuccessMessage,DAE_ForgetLoginPwdPage_Element
import time
class TestHuiyin(mytest.MyTest):
    """DAE注册登录功能测试"""

    # def test_mouse_over(self):
    #     """鼠标悬浮测试"""
    #     firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
    #     firstPage.move()
    #     time.sleep(3)
    #     self.assertTrue(self.dr.get_element(DAE_ForgetLoginPwdPage_Element.downloadApp).is_displayed())
    def test_click(self):
        """登录测试"""
        firstPage = DAE_FirstPage.DAEFirstPage(self.dr)
        firstPage.click()
        firstPage.username('8888@qq.com','123456')
        firstPage.click_user()
        time.sleep(3)
