# coding=utf-8
import unittest
from core.core import Test

class TestLoginSales(Test):

    # 登录
    def test_account_login(self):
        # 正常登录
        r = self.request(self.data['url'], type=self.data['mode'], data=self.data['data'], token=False)
        # 添加判断等代码
        if r['status'] == 'success':
            r_data = r['data'] # json

        self.result = r

#运行当前py
if __name__ == '__main__':
    unittest.main()



