# coding=utf-8
from core.models.tool import Tool
from core.models.install import Install
from core.models.unittest import Unittest
from core.models.mytest import Mytest


class Core(Tool,Install,Unittest):
	def _start(self):
		self.__check_install_fun()

	#私有方法 第一步先检查项目初始化
	def __check_install_fun(self):
		#调用checkInstall函数 检查是否初始化
		if self.check_install():
			#print('执行项目Test')
			self.__unittest_init()
		else:
			print('初始化完成')
			
	#执行测试
	def __unittest_init(self):
		print('执行测试')
		self.test_run()


class Tool(Tool):
	pass


class Test(Mytest):
	pass
		