#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# MyBalance_BTC_Deposite
MyBalance_BTC_Deposite = 'css->div[class^=wallet_\w* eth_\w*]>div>span>a:nth-child(1)'

# MyBalance_BTC_Withdraw
MyBalance_BTC_Withdraw = 'link_text->提现'

# MyBalance_ETH_Deposite
MyBalance_ETH_Deposite = 'css->div[class^=wallet_\w* eth_\w*]>div>a:nth-child(1)'

# MyBalance_ETH_Withdraw
MyBalance_ETH_Withdraw = 'css->div[class=^wallet_\w* eth_\w*]>div>a:nth-child(2)'

# MyBalance_ETC_Deposite
MyBalance_ETC_Deposite = 'css->div[class=^wallet_\w* eth_\w*]>div>a:nth-child(1)'

# MyBalance_ETC_Withdraw
MyBalance_ETC_Withdraw = 'css->div[class=^wallet_\w* eth_\w*]>div>a:nth-child(2)'

# TabBar_Deposite
TabBar_Deposite = 'css->div[class=^tabbar_]>div:nth:child(1)'

# TabBar_Withdraw
TabBar_Withdraw = 'css->div[class=^tabbar_]>div:nth:child(2)'

# SideBar_BTC
SideBar_BTC = 'css->div[class=^sideBarSection_*]>a:nth-child(1)'

# SideBar_ETH
SideBar_ETH = 'css->div[class=^sideBarSection_*]>a:nth-child(2)'

# SideBar_ETC
SideBar_ETC = 'css->div[class=^sideBarSection_*]>a:nth-child(3)'

# Deposite_Address
Deposite_Address = 'css->span[class^=address_]>span:nth-child(2)'

# CopyAddress_Link
CopyAddress_Link = 'css->span[class^=copy_]'

# Copy_Success
Copy_Success = 'css->//*[contains(text(),已复制)]'

# Address_Input
Address_Input = 'name->target'

# Amount_Inputs
Amount_Input = 'name->amount'

# Password_Input
Password_Input = 'name->tradepassword'

# Submit_Button
Submit_Button = 'tag_name->button'