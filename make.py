# coding=utf-8
from core.core import Core

# 根据config 生成测试用例
class Make(Core):
    def __init__(self):
        print('生成测试用例')
        # core._makestart
        self._makestart()


if __name__ == '__main__':
    Make()
