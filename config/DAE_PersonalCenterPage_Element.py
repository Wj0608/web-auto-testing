
import os
from public.common.readconfig import ReadConfig


# PersonalCenter_Tab
PersonalCenter_Tab = 'link_text->个人中心'

# MyBalance_Tab
MyBalance_Tab = 'css->a[href=\'/wallet\']'

# Trade_Tab
Trade_Tab = 'css->a[href=\'/trade/XUC_BTC\']'

# Account_Tab
Account_Tab = 'css->a[href=\'/user-center/account\']'

# SecuritySetting_Tab
SecuritySetting_Tab = 'css->a[href=\'/user-center/security-setting\']'

# SecurityPolicy_Tab
SecurityPolicy_Tab = 'css->a[href=\'/user-center/security-policy\']'

# ChangeNickname_Button
ChangeNickname_Button ='xpath->//button[contains(text(),修改昵称)]'

# nickname_Input
nickname_Input = 'name->nickname'

# ConfirmChange
ConfirmChange = 'css->button[type=submit]'

# Cancel_Button
Cancel_Button = 'css->button[type=button]'

# ChangeEmail_Button
ChangeEmail_Button ='xpath->//*[text()="修改邮箱"]'

# NewEmail_Input
NewEmail_Input = 'name->email'

# Vcode_Input
Vcode_Input = 'name->vcode'

# SendCode_Button
SendCode_Button = 'xpath->//*[text()=\'发送验证码\')]'

# SendSuccess
SendSuccess = 'xpath->//span[contains(text(),"发送成功，请查收")]'

# TradePwd_Input
TradePwd_Input = 'name->trade_password'

# ChangeLoginPwd_Button
ChangeLoginPwd_Button = 'xpath->button[contains(text(),修改登录密码)]'

# OldPwd_Input
OldPwd_Input = 'name->old_password'

# NewPwd_Input
NewPwd_Input = 'name->new_password'

# ConfirmPwd_Input
ConfirmPwd_Input = 'name->confirm_password'

# ForgetCurrencyPwd_Button
ForgetCurrencyPwd_Button = 'xpath->button[contains(text(),忘记资金密码)]'

# ChangeSuccess
ChangeSuccess = 'xpath->button[contains(text(),修改成功)]'

# ChangeCurrencyPwd_Button
ChangeCurrencyPwd_Button = 'xpath->button[contains(text(),修改资金密码)]'

# OldTradePwd_Input
OldTradePwd_Input = 'name->old_trade_password'

# NewTradePwd_Input
NewTradePwd_Input = 'name->new_trade_password'


# ConfirmTradePwd_Input
ConfirmTradePwd_Input = 'name->confirm_new_trade_password'

# XUCAddress
XUCAddress = 'css->div[.^=address_]>span:nth-child(1)'

# BTCAddress
BTCAddress = 'css->div[.^=address_]>span:nth-child(2)'

# ETHAddress
ETHAddress = 'css->div[.^=address_]>span:nth-child(3)'

# LTCAddress
LTCAddress = 'css->div[.^=address_]>span:nth-child(4)'

# ETCAddress
ETCAddress = 'css->div[.^=address_]>span:nth-child(5)'

# AddressManager_Button
AddressManager_Button = 'xpath->button[contains(text(),提币地址管理)]'

# # AddressManager_Button
# AddressManager_Button = 'xpath->span[contains(text(),收起提币地址管理)]'

# Google_Verification
google_verification = 'xpath->span[contains(text(),绑定谷歌验证器)]'

# SMS_Verification
SMS_Verification = 'xpath->span[contains(text(),绑定SMS验证)]'