# coding=utf-8
import unittest
from core import Test

class TestRegSales(Test):
    # 注册
    @unittest.skip('暂时跳过')
    def test_account_reg(self):
        print('测试注册')
        r = self.request(self.data['url'], type=self.data['mode'], data=self.data['data'], token=False)


#运行当前py
if __name__ == '__main__':
    unittest.main()



