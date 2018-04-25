#coding=utf-8
import  time
from config import globalparam
import sys
import os
import datetime

    # 截图放到report下的image目录下
def get_img(dr, filename):
    today = time.strftime('%Y-%m-%d')
    path = globalparam.img_path + '\\' + today  + '_' + filename
    dr.take_screenshot(path)

   # 清除过期文件
def cleanReportFile(self,day,filetype):
    file_url = ""
    if filetype == "reortfile":
        file_url= globalparam.report_path
    if filetype == "logfile":
        file_url = globalparam.log_path
    if filetype == "imgfile":
        file_url = globalparam.img_path
    f = list(os.listdir(file_url))
    for i in range(len(f)):
        filedate = os.path.getmtime(file_url+f[i])
        time1 = datetime.datetime.fromtimestamp(filedate).strftime('%Y-%m-%d')
        date1 = time.time()
        num1 = (date1-filedate)/60/60/24
        if num1>day:
            try:
                os.remove(file_url+f[i])
            except Exception as e:
                print(e)

