#coding=utf-8

import os
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from public.common.readconfig import ReadConfig


#################################Login Page################################################

# AccountOrPwd_Error
AccountOrPwd_Error = 'xpath->//span[contains(text(),"邮箱或密码错误")]'

# EmailsNullI
EmailsNullI =  'xpath->//span[contains(text(),请输入邮箱)]'

# PasswordlsNullI
PasswordlsNullI =  'xpath->//*[contains(text(),请输入登录密码)]'

# Network_Error
Network_Error = 'xpath->//*[contains(text(),网络错误)]'

###################################
# NicknameExist
NicknameExist = 'xpath->//div[contains(text(),昵称已存在)]'

# ChangeSuccess
ChangeSuccess = 'xpath->//span[contains(text(),修改成功)]'



# DifferentPwd_Error
DifferentPwd_Error = 'xpath->//*[contains(text(),两次输入密码不一致)]'

# WrongPhoneNumber_Error
WrongPhoneNumber_Error = 'xpath->//*[contains(text(),请输入正确的手机号)]'

# OldWithdrawPwd_Error
OldWithdrawPwd_Error = 'xpath->//*[contains(text(),原提币密码不正确)]'

# NotInputNewWithdrawPwd_Error
NotInputNewWithdrawPwd_Error = 'xpath->//*[contains(text(),请输新提币密码)]'

# CannotInputMyselfAddress_Error
CannotInputMyselfAddress_Error = 'xpath->//*[contains(text(),不能提到自己的充值地址)]'

# WrongTradePwd_Error
WrongTradePwd_Error = 'xpath->//*[contains(text(),交易密码错误)]'

# InputAddress_Remind
InputAddress_Remind = 'xpath->//*[contains(text(),请输入提现地址)]'

# InputPwd_Remind
InputPwd_Remind = 'xpath->//*[contains(text(),请输入提币密码)]'

# InputAmount_Remind
InputAmount_Remind = 'xpath->//*[contains(text(),请输入提现金额)]'

# InValidAddress_Remind
InValidAddress_Remind = 'xpath->//*[contains(text(),无效的提现地址)]'