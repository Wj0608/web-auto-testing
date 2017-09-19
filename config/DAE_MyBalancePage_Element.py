#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# BTCDeposite_Link
BTCDeposite_Link = 'css->div[class^=walletList_]>div:nth-child(1)>div>span:nth-child(3)'

# ETHDeposite_Link
ETHDeposite_Link = 'css->div[class^=walletList_]>div:nth-child(2)>div>span:nth-child(3)'

# ETCDeposite_Link
ETCDeposite_Link = 'css->div[class^=walletList_]>div:nth-child(3)>div>span:nth-child(3)'



# CopyAddress_Link
CopyAddress_Link = 'xpath->//*[contains(text(),充值地址)]'

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