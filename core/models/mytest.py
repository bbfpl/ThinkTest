import os
import unittest
from core.models.tool import Tool
from core.models.xhr import Xhr

class Mytest(unittest.TestCase,Tool,Xhr):
    # 获取info
    def _getTestInfo(self):
        class_name = self.__class__.__name__
        method_name = self._testMethodName
        model_name = os.path.basename(os.getcwd())
        file_name = self.__class__.__module__
        file_name = file_name.replace('_st', '')
        return {
            'model_name':model_name,
            'file_name': file_name,
            'class_name': class_name,
            'method_name': method_name,
            'now_data': 'project.models.' + model_name + '.' + file_name + '.funName.' + method_name
        }

    # 获取data
    def _getData(self):
        # 获取当前用例class名 方法名 等
        get_test_info = self._getTestInfo()

        # 全局data 用例里可用
        data = self.get_yaml(get_test_info['now_data'])
        # 给url添加域名
        data['url'] = self.get_yaml('project.config.domain') + data['url']
        return data

    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        print('setUpClass.......')

    # 每个测试函数运行前运行
    def setUp(self):
        self.data = self._getData()



        print("开始执行用例:1")

    # 每个测试函数运行完后执行
    def tearDown(self):
        print("用例执行结束。。。")
        # self.result

    # 必须使用@classmethod装饰器,所有test运行完后运行一次
    @classmethod
    def tearDownClass(cls):
        print('测试类运行结束！')
        return


