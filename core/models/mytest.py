
import unittest

class Mytest(unittest.TestCase):

    # 计算测试用例的个数，用于显示在测试报告中
    @classmethod
    def setUpClass(self):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('测试类运行结束！')
        return

    def setUp(self):
        print("开始执行用例:1")


    def tearDown(self):
        print("用例执行结束。。。")
        # self.result
