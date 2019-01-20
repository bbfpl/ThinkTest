# coding=utf-8
import unittest
from core import Test

class TestUser(Test):
	# 获取公司id
	def _get_company_id(self):
		print('_get_company_id')
		# r = self.request(self.data['url'], type=self.data['mode'])
	# 添加用户
	def test_add_user(self):
		print(1)
		# r = self.request(self.data['url'], type=self.data['mode'], data=self.data['data'], token=False)
	# 修改用户信息
	def test_edit_user(self):
		print(2)
		# r = self.request(self.data['url'], type=self.data['mode'])
	# 删除用户
	def test_del_user(self):
		print(3)
		# r = self.request(self.data['url'], type=self.data['mode'])
# 运行
if __name__ == '__main__':
	unittest.main()