#coding=utf-8
import  time
from config import globalparam


# 截图放到report下的image目录下
def get_img(dr, filename):
    today = time.strftime('%Y-%m-%d')
    path = globalparam.img_path + '\\' + today  + '_' + filename
    dr.take_screenshot(path)
