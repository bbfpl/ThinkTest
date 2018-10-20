# coding=utf-8

import os
#导入 unittest 模块
import unittest
#导入 time 模块
import time

from core.models.tool import Tool


#定义Unittest类
class Unittest():


	def testRun(self):
		print('unittest run')

		project_path = os.path.join(os.getcwd(),'project')

		#获取根目录下config.ini
		config = Tool().readBaseConfig()

		projectName = config.get("Config","main")

		#开始时间
		start_time = time.time()

		#项目路径
		projectPath = project_path+'/{}/'.format(projectName)

		discover = unittest.defaultTestLoader.discover(projectPath,pattern='*_st.py',top_level_dir=None)

		# all_case_fun = []
		# for i in str(discover).split('testMethod='):
		# 	for j in i.split('>'):
		# 		if 'test_' in j:
		# 			all_case_fun.append(j)

		runner = unittest.TextTestRunner(verbosity=1)
		result = runner.run(discover)



