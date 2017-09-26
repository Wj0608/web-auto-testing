#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# BTCDeposite_Link
BTCDeposite_Link = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span[3]/a'

# ETHDeposite_Link
ETHDeposite_Link = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/span[3]/a'

# ETCDeposite_Link
ETCDeposite_Link = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/span[3]/a'

# Deposite_Address
Deposite_Address = 'css->span[class^=address_]>span:nth-child(1)'

# BTCBalance
BTCBalance = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/span[2]'

# ETHBalance
ETHBalance = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/span[2]'

# ETCBalance
ETCBalance = 'xpath->//*[@id="app"]/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/span[2]'

# CopyAddress_Link
CopyAddress_Link = 'css->span[class^=copy_]'

# Copy_Success
Copy_Success = 'css->//*[contains(text(),已复制)]'

# Withdraw_Button
Withdraw_Button = 'link_text->提现'

# Address_Input
Address_Input = 'name->target'

# Amount_Input
Amount_Input = 'name->amount'

# Password_Input
Password_Input = 'name->tradepassword'

# Submit_Button
Submit_Button = 'tag_name->button'