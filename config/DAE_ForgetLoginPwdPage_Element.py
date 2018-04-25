#coding=utf-8

import os
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from public.common.readconfig import ReadConfig

# Email_Input
Email_Input = 'name->username'

# SendCode_Button
SendCode_Button = 'tag_name->button'

# VCode_Input
VCode_Input = 'name->vcode'

# NextStep_Button
NextStep_Button = 'css->button[type=submit]'

# SendVCode_Button
SendVCode_Button = 'link_text->发送验证码'

# Password_Input
Password_Input = 'name->new_password'

# PasswordConfirm_Input
PasswordConfirm_Input = 'name->confirm_new_password'

# Login_Link
Login_Link = 'css->a[href=\'/login\']'

# SendVCodeSuccess
SendVCodeSuccess = 'xpath->//*[contains(text(),发送成功)'