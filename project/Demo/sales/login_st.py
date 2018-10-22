# coding=utf-8
import unittest
from core.core import Test,Tool

class TestLogin_sales(Test,Tool):
	
    # 登录
    def test_login_sales(self):
        # 正常登录
        config_data = self.get_yaml('sales','login')

        r = self.request('https://www.baidu.com/','get')
        print(r.status_code)

        self.result = '1'
        self.assertEqual(1, 1)



#运行当前py
if __name__ == '__main__':
    unittest.main()



