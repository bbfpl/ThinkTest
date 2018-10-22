# coding=utf-8
import os
import yaml
import configparser
from core.models.xhr import Xhr
#Tool class
class Tool(Xhr):
	# 获取根目录
	base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

	# 判断数组长度是非为0
	@staticmethod
	def is_list_empty(list_temp):
		if list_temp:
			return True
		else:
			return False

	# 判断是否为空
	@staticmethod
	def is_empty(val):
		print('isEmpty')
		if val is None or val is '' or val is 'null':
			return True
		else:
			return False

	# 获取当前项目下yaml配置文件
	def get_yaml(self,name,subname):
		#获取config
		config = self.read_base_config()
		#读取项目入口
		projectName = config.get("Config","main")

		#每个项目下面有个config.yaml
		path = self.base_dir + '/project/' + projectName + '/config.yaml'
		#yaml的读取
		f = open(path, encoding='utf-8')
		data = yaml.load(f)
		f.close()

		return data[name][subname]

	def read_base_config(self):
		#获取根目录下config.ini
		config_path = os.path.join(self.base_dir,'config.ini')

		#读取配置文件
		config = configparser.ConfigParser()
		config.read(config_path)
		return config


