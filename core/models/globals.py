# coding=utf-8
from config import Config
global _global_dict
_global_dict = {}
# 设置全局变量
def g_set(key,val):
	_global_dict[key] = val

# 获取全局变量
def g_get(key):
	try:
		return _global_dict[key]
	except KeyError:
		return Config.get_config('main').split(',')[0]