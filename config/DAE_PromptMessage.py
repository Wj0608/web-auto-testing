import os
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from public.common.readconfig import ReadConfig

# nickNameExist
nickNameExist = 'xpath->//*[contains(text(),昵称已被占用)]'

# nicknameFormatWrong
nicknameFormatWrong = 'xpath->//*[contains(text(),4-20个字符)]'

# nicknameIncludeillegalChars
nicknameIncludeillegalChars = 'xpath->//*[contains(text(),昵称包含非法字符)]'

# openSecurityLoginStrategy
openSecurityLoginStrategy = 'xpath->//*[contains(text(),此账号已开启登录安全策略)]'

# emailIncludeillegalChars
emailIncludeillegalChars = 'xpath->//*[contains(text(),邮箱格式错误)]'

# wrongEmail
wrongEmail = 'xpath->//*[contains(text(),邮箱错误)]'

# setLoginPwd
setLoginPwd = 'xpath->//*[contains(text(),设置登录密码)]'

# WrongCode
WrongCode = 'xpath->//*[contains(text(),验证码错误)]'

# NotSamePwd
NotSamePwd = 'xpath->//*[contains(text(),密码不一致)]'

# LoginPwdLong
LoginPwdLong = 'xpath->//*[contains(text(),6-32位字符)]'

# PleaseInputPwd
PleaseInputPwd = 'xpath->//*[contains(text(),请输入密码)]'

# PleaseConfirmPwd
PleaseConfirmPwd = 'xpath->//*[contains(text(),请确认密码)]'

# LoginWrong
LoginWrong = 'xpath->//*[contains(text(),密码或验证码错误)]'

# FindPwdSuccess
FindPwdSuccess = 'xpath->//*[contains(text(),您的密码重置成功)]'

# RegainCode
RegainCode = 'xpath->//*[contains(text(),请重新获取验证码)]'

# WrongFormat
WrongFormat = 'xpath->//*[contains(text(),格式错误)]'

# NoneEmail
NoneEmail = 'xpath->//*[contains(text(),请输入邮箱地址)]'

# NoneCode
NoneCode = 'xpath->//*[contains(text(),请输入验证码)]'