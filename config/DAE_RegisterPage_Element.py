#coding=utf-8
import os
from public.common.readconfig import ReadConfig
click_Free_for_registration='link_text->Free for registration'
NickName_Input = 'name->nickname'
# Email_Input
Email_Input = 'name->email'
# SendVCode_Button
click_Code_Button = 'css->button[type=button]'
# VCode_Input
VCode_Input = 'name->vcode'
# Submit_Button
Submit_Button = 'css->button[type=submit]'
# Password_Input
Password_Input = 'name->password'
# PasswordConfirm_Input
PasswordConfirm_Input = 'name->confirmPassword'
# Register_Button
Register_Button = 'css->button[type=submit]'
# Succeed
Succeed='xpath->//span[contains(text(),"Succeed")] '
#Sign_up_successfully!
Sign_up='xpath->//span[contains(text(),"Sign up successfully!")]'
#existed nickname
existed_nickname='xpath->//span[contains(text(),"existed nickname")]'
#registered email
registered_email='xpath->//span[contains(text(),"registered email, please sign in")]'
#invalid validation code
invalid_code='xpath->//span[contains(text(),\'invalid validation code\')]'
#please enter email
please_email='xpath->//span[contains(text(),"please enter email")]'
#includes invalid characters
includes_invalid='xpath->//span[contains(text(),"includes invalid characters")]'
#please enter correct email
please_correct_email='xpath->//span[contains(text(),"please enter correct email")]'
#please enter validation code
please_code='xpath->//span[contains(text(),"please enter validation code")]'
#please enter login password
please_password='xpath->//span[contains(text(),"please enter login password")]'
#mismatch password
mismatch_password='xpath->//span[contains(text(),"mismatch password")]'