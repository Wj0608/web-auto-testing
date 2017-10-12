#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# PersonalCenter_Button
PersonalCenter_Button = 'css->a[href=/user-center/account]'

# Account_Img
Account_Img= 'css->div[class^=userInfo_]'

# Security_Set
Security_Set = 'link_text->安全设置'

# Pwd_Status
Pwd_Status = 'css->div[class^=status_]'

# KYC_Tab
KYC_Tab = 'link_text->身份验证'

# TradePassword_Tab
TradePassword_Tab = 'link_text->交易密码'

# KYC_Link
KYC_Link = 'link_text->获取更多权限'

# ChangePassword_Link
ChangePassword_Link = 'link_text->修改提币密码'

# ForgetPassword_Link
ForgetPassword_Link = 'link_text->忘记提币密码'

# SetTradePassword_Input
SetTradePassword_Input = 'name->trade_password'

# OldTradePassword_Input
OldTradePassword_Input = 'name->old_trade_password'

# NewTradePassword_Input
NewTradePassword_Input = 'name->new_trade_password'

# ConfirmTradePassword_Input
ConfirmTradePassword_Input = 'name->confirm_trade_password'

# ConfirmNewTradePassword_Input
ConfirmNewTradePassword_Input = 'name->confirm_new_trade_password'

# Submit_Button
Submit_Button = 'tag_name->button'

# SendVCode_Button
SendVCode_Button = 'link_text->发送验证码'

# SendVCode_Success
SendVCode_Success = 'css->div[class^=fieldInput_]>div:nth-child(2)>a'

# VCode_Input
VCode_Input = 'name->vcode'

# NextStep_Button
NextStep_Button = 'tag_name->button'

# SetWithdrawPwd
SetWithdrawPwd = 'link_text->设置提币密码'