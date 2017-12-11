#coding=utf-8

import os
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from public.common.readconfig import ReadConfig

# EmailOrPhone_Input
EmailOrPhone_Input = 'name->username'

# PictureVCode_Input
PictureVCode_Input = 'name->captcha'

# NextStep_Button
NextStep_Button = 'tag_name->button'

# SendVCode_Button
SendVCode_Button = 'link_text->发送验证码'

# VCode_Input
VCode_Input = 'name->vcode'

# SendSuccess
SendSuccess = ''

# LoginPwd_Input
LoginPwd_Input = 'name->new_password'

# ConfirmLoginPwd
ConfirmLoginPwd ='name->confirm_new_password'

# SendVCodeSuccess
SendVCodeSuccess = 'css->xpath->//*[contains(text(),发送成功，请查收)'