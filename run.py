# -*- coding: utf-8 -*-

import time
import unittest
import HTMLTestRunner
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from config import globalparam

# reload(sys)
# sys.setdefaultencoding('utf8')
# from public.common import sendmail

def run():
    test_dir = './testcase'
<<<<<<< HEAD
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_RegisterAndLogin.py')
=======
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test_ForgetWithdrawPwd.py')
>>>>>>> e7dd5b8b3e31cc98edf5a32567d356d3c0539ff5

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    #reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u'UI自动化测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()

if __name__=='__main__':
    run()