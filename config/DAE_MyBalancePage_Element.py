#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# PersonalCenter
PersonalCenter = 'xpath->a[href=/user-center/account]'

# Balance_Manage
Balance_Manage = 'xpath->//*[contains(text(),资产管理中心)]'

# MyBalance_BTC_Deposite
MyBalance_BTC_Deposite = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/span/a[1]'

# MyBalance_BTC_Withdraw
MyBalance_BTC_Withdraw = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/span/a[1]'

# MyBalance_ETH_Deposite
MyBalance_ETH_Deposite = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/span/a[1]'

# MyBalance_ETH_Withdraw
MyBalance_ETH_Withdraw = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/span/a[2]'

# MyBalance_ETC_Deposite
MyBalance_ETC_Deposite = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/span/a[1]'

# MyBalance_ETC_Withdraw
MyBalance_ETC_Withdraw = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/span/a[2]'

# TabBar_Deposite
TabBar_Deposite = 'css->div[class=^tabbar]>div:nth_child(1)'

# TabBar_Withdraw
TabBar_Withdraw = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[2]'

# SideBar_BTC
SideBar_BTC = 'css->div[class=^sideBarSection_*]>a:nth-child(1)'

# SideBar_ETH
SideBar_ETH = 'css->div[class=^sideBarSection_*]>a:nth-child(2)'

# SideBar_ETC
SideBar_ETC = 'css->div[class=^sideBarSection_*]>a:nth-child(3)'

# Deposite_Address
Deposite_Address = 'css->span[class^=address_]>span[class^=label_]'

# CopyAddress_Link
CopyAddress_Link = 'css->span[class^=copy_]'

# Copy_Success
Copy_Success = 'xpath->//*[contains(text(),已复制)]'

# Address_Input
Address_Input = 'name->target'

# Amount_Inputs
Amount_Input = 'name->amount'

# Password_Input
Password_Input = 'name->tradepassword'

# Submit_Button
Submit_Button = 'tag_name->button'