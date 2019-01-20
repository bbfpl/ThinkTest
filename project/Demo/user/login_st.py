# coding=utf-8
import unittest
from core import Test

class TestUserLogin(Test):
	
	# 登录
	def test_login(self):
		r = self.request(self.data['url'], type=self.data['mode'], data=self.data['data'], token=False)
		self.assertEqual(1, 1)
	
	# 登录-get测试
	def test_login_get(self):
		r = self.request(self.data['url'], type=self.data['mode'])
		self.assertEqual(1, 1)
	
	# 登录-密码为空
	def test_login_nopsw(self):
		r = self.request(self.data['url'], type=self.data['mode'], data=self.data['data'], token=False)
		self.assertEqual(1, 1)
	

# 运行
if __name__ == '__main__':
	unittest.main()