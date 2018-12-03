# coding=utf-8
import unittest
from core.core import Test,Tool

class TestLoginSales(Test,Tool):
    base_data = Tool.get_yaml('sales.login')
    # 登录
    def test_login_sales(self):
        # 正常登录
        test_account_login = base_data['funName']['test_account_login']

        data = test_account_login.data
        data['age'] = 12

        r = self.request('https://www.uihtml.com/admin/api_login'+base_data['url'], type='post', data=data, token=False)
        if r['status'] == 'success':
            r_data = r['data'] # json

        self.result = r
        # self.assertEqual(1, 1)

#运行当前py
if __name__ == '__main__':
    unittest.main()



