# coding=utf-8
import unittest
from core import Test

class TestUsers(Test):
	
	# 获取所有用户
	def test_get_users(self):
	
		r = self.request(self.data['url'], type=self.data['mode'])
	
		print(r)
		self.assertEqual(1, 1)
	

# 运行
if __name__ == '__main__':
	unittest.main()