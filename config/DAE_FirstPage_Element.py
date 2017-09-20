#coding=utf-8

import os
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from public.common.readconfig import ReadConfig

# DigitalWallet_Text
DigitalWallet_Text = 'xpath->//*[contains(text(),最可靠的数字钱包)]'

# HeaderLogin_Button
HeaderLogin_Button = 'link_text->登录'

# HeaderRegister_Button
HeaderRegister_Button = 'link_text->注册'

# # BTC_Button
# BTC_Button='css->div[class^="markets_"]>span:nth-child(1)'
#
# # ETH_Button
# ETH_Button='css->div[class^="markets_"]>span:nth-child(2)'
#
# # ETC_Button
# ETC_Button='css->div[class^="markets_"]>span:nth-child(3)'
#
# # PhoneOrEmailLogin_Button
# PhoneOrEmailLogin_Button='link_text->使用邮箱/手机登录'
#

# LoginUsername_Input
LoginUsername_Input='name->username'

# LoginPassword_Input
LoginPassword_Input='name->password'

# ForgetPassword_Link
ForgetPassword_Link='link_text->忘记密码？'

# Register_Link
Register_Link='link_text->立即注册'

# Login_Button
Login_Button = 'tag_name->button'
