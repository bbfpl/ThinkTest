# coding=utf-8
import unittest
from core import Test

class TestUserLogin(Test):
    
    # 登录
    def test_login(self):

        data = {
            'form_data':
                {
                    'member_id': 0,
                    'member_name': "新增员工78",
                    'mobile': "15000005530",
                    'email': "15000005530@163.com",
                    'password': "Aa123456",
                    'department_id': "4198",
                    'role': "30",
                    'sex': [{"value": "1", "option": "男"}]
                },
            'form_tpl_id': 8
        }
        r = self.request(self.data['url'], type=self.data['mode'])
    
        self.assertEqual(1, 1)
    

# 运行
if __name__ == '__main__':
    unittest.main()