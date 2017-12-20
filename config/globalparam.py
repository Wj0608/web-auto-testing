#coding=utf-8

import os
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from public.common.readconfig import ReadConfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# 默认浏览器
# browser = 'safari'
browser = 'chrome'
# DAE首页
environment_address='http://pre-www.dae.org/'

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# Interface_address
Interface_address = 'http://pre-api.dae.org/'