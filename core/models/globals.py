# coding=utf-8
import os

# 根目录
def base_dir():
	return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

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
		return None