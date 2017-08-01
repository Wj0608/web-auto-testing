#coding=utf-8

from public.common import basepage

class HuiyinPage(basepage.Page):

    def into_huiyin_page(self):
        """打开汇银首页"""
        self.dr.open('http://www.huiyin.com')
    # def input_search_key(self,values):
    #     """输入搜索关键词"""
    #     self.dr.clear_type('id->kw',values)

    def click_shouye_button(self):
        """点击搜索按钮"""
        self.dr.click('xpath->//*[@id="form1"]/div[2]/div/div[2]/div/ul/li[2]/a')


    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()