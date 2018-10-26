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
	def get_yaml(self,name=''):
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

		if name != '':
			for item in name.split('.'):
				data = data[item]

		return data

	def read_base_config(self):
		#获取根目录下config.ini
		config_path = os.path.join(self.base_dir,'config.ini')

		#读取配置文件
		config = configparser.ConfigParser()
		config.read(config_path)
		return config

	# 创建目录
	def mkdir(self,path):
	    # 去除首位空格
	    path = path.strip()
	    # 去除尾部 \ 符号
	    path = path.rstrip("\\")
	 
	    # 判断路径是否存在
	    # 存在     True
	    # 不存在   False
	    isExists=os.path.exists(path)
	 
	    # 判断结果
	    if not isExists:
	        # 如果不存在则创建目录
	        # 创建目录操作函数
	        os.makedirs(path) 
	 
	        print(path+' 创建成功')
	        return True
	    else:
	        # 如果目录存在则不创建，并提示目录已存在
	        # print(path+' 目录已存在')
	        return False

