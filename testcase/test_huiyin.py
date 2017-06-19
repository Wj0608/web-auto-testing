#coding=utf-8

from time import sleep
from public.common import mytest
from public.common import publicfunction
from public.pages import huiyinPage
from public.common import datainfo


class TestHuiyin(mytest.MyTest):
    """汇银首页测试"""

    def test_open(self):
        """打开首页"""
        huiyinpage = huiyinPage.HuiyinPage(self.dr)

        huiyinpage.into_huiyin_page()
        publicfunction.get_img(self.dr,'111.png')
        huiyinpage.click_shouye_button()




        sleep(2)
        print(huiyinpage.return_title())

        self.assertIn(u'汇银',huiyinpage.return_title())
