# coding=utf-8
import os
import unittest
import warnings
from request import Request
from tool import Tool
from db import DB
from config import Config

class Test(unittest.TestCase):
    result = {}
    # 在test单独写request 是为了简洁用例代码量
    def request(self, api='', type="post", data={}, token=False):
        r = Request().request(api, type, data, token)
        self.result = r
        return r
    # 获取info
    def _getTestInfo(self):
        # 当前测试用例 class 名称
        class_name = self.__class__.__name__
        # 当前测试用例 方法 名称
        method_name = self._testMethodName
        # 当前测试用例 文件 名称
        file_name = self.__class__.__module__
        file_name = file_name.replace('_st', '')
        # 当前测试用例 路径
        file_path = os.path.basename(os.getcwd())

        # 暂时想到这种解决方法 等以后再来优化这块
        if file_name.find('.') >= 0:
            now_data = 'project.models.' + file_name + '.funName.' + method_name
        else:
            now_data = 'project.models.' +file_path + '.' + file_name + '.funName.' + method_name
        return {
            # 'file_name': file_name,
            'class_name': class_name, # 类名
            'method_name': method_name, # 方法名
            'now_data': now_data    # 当前方法的yaml路径拼接
        }

    # 获取data
    def _getData(self):
        # 获取当前用例class名 方法名 等
        get_test_info = self._getTestInfo()
        # 全局data 用例里可用
        data = Tool.get_yaml(get_test_info['now_data'])
        # 给url添加域名
        if 'url' in data.keys():
            data['url'] = Tool.get_yaml('project.config.domain') + data['url']
        return data

    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        print('run setUpClass\n')

    # 每个测试函数运行前运行
    def setUp(self):
        # 在每个用例里可调用
        self.data = self._getData()
        # print("开始执行用例:1")

    # 每个测试函数运行完后执行
    def tearDown(self):
        # 忽略掉io告警
        warnings.simplefilter("ignore", ResourceWarning)
        # 保存到db
        if self.result:
            get_test_info = self._getTestInfo()
            DB().inster({
                'method_name': get_test_info['method_name'],
                'data': self.data,#
                'result': self.result #返回提交的data的json
            })

            is_interrupt_continue = Config.get_config('interruptContinue')
            if is_interrupt_continue is True:
                # 保存到 结果队列
                DB('temp','complete').inster({
                    'status': 1,
                    'method_name': get_test_info['method_name']
                })

    # 必须使用@classmethod装饰器,所有test运行完后运行一次
    @classmethod
    def tearDownClass(cls):
        #print('测试类运行结束！')
        return


