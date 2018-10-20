# coding=utf-8
import os
import yaml
import configparser
#Tool class
class Tool():
	#获取根目录
	base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

	#判断是否是数组
	def isArray(self):
		print('isArray')
	#判断是否是字符串
	def isStr(self):
		print('isStr')
	#判断是否为空
	def isEmpty(self):
		print('isEmpty')

	def getYaml(self,name,subname):
		#获取config
		config = self.readBaseConfig()
		#读取项目入口
		projectName = config.get("Config","main")

		#每个项目下面有个config.yaml
		path = self.base_dir + '/project/' + projectName + '/config.yaml'
		#yaml的读取
		f = open(path, encoding='utf-8')
		data = yaml.load(f)
		f.close()

		return data[name][subname]

	def readBaseConfig(self):
		#获取根目录下config.ini
		config_path = os.path.join(self.base_dir,'config.ini')

		#读取配置文件
		config = configparser.ConfigParser()
		config.read(config_path)
		return config


