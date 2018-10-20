# coding=utf-8
from core.models.tool import Tool
from core.models.install import Install
from core.models.unittest import Unittest
from core.models.mytest import Mytest


class Core(Tool,Install,Unittest):
	def __init__(self):
		self.__checkInstallFun()

	#私有方法 第一步先检查项目初始化
	def __checkInstallFun(self):
		#调用checkInstall函数 检查是否初始化
		isInstall = self.checkInstall()
		if isInstall == True:
			#print('执行项目Test')
			self.__unittestInit()
		else:
			print('初始化完成')
			
	#执行测试
	def __unittestInit(self):
		print('执行测试')
		self.testRun()


class Tool(Tool):
	pass


class Test(Mytest):
	pass
		