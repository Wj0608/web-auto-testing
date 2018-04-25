#coding=utf-8

import sys
import time
import unittest.result
from unittest.case import TestCase
from public.common import pyselenium,publicfunction
from config import globalparam
from public.common.log import Log

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.open(globalparam.address)
        self.dr.js("var q=document.documentElement.scrollTop=10000")
        self.dr.get_element("link_text->中文").click()
        self.dr.max_window()

    def tearDown(self):
        # error = unittest.result.TestResult()
        # if error.buffer:
        #     if error._mirrorOutput:
        for method, error in self._outcome.errors:
            if error:
                test_method_name = self._testMethodName
                publicfunction.get_img(self.dr,test_method_name+".png")
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')