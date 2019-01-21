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
            now_data = 'project.models.' + file_name
        else:
            now_data = 'project.models.' +file_path + '.' + file_name
        return {
            # 'file_name': file_name,
            'class_name': class_name, # 类名
            'method_name': method_name, # 方法名
            'now_data_model': now_data,# 当前模块路径拼接
            'now_data_fun': now_data + '.funName.' + method_name    # 当前方法的yaml路径拼接
        }

    # 获取data
    def _getData(self):
        # 获取当前用例class名 方法名 等
        get_test_info = self._getTestInfo()
        # 全局data 用例里可用
        now_data_model = Tool.get_yaml(get_test_info['now_data_model'])
        data = Tool.get_yaml(get_test_info['now_data_fun'])

        # 模块公共属性 比如 url mode等
        if 'url' in now_data_model:
            pub_url = now_data_model['url']
        else:
            pub_url = None
        if 'mode' in now_data_model:
            pub_mode = now_data_model['mode']
        else:
            pub_mode = None

        if data != '':
            if 'data' not in data:
                data['data'] = {}
            # 如果test_xx接口没有url或者mode就调用全局的
            if 'url' not in data:
                _url = pub_url # 给url添加域名
            else:
                _url = data['url']  # 给url添加域名
            data['url'] = Tool.get_yaml('project.config.domain') + _url

            if 'mode' not in data:
                data['mode'] = pub_mode

            return data
        else:
            return {}
    # 必须使用@classmethod 装饰器,所有test运行前运行一次
    @classmethod
    def setUpClass(cls):
        print('run setUpClass\n')

    # 每个测试函数运行前运行
    def setUp(self):
        # 在每个用例里可调用
        self.data = self._getData()
        # print(self.data)
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
            if is_interrupt_continue == 'True':
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


