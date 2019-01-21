import time
from multiprocessing import Pool
from testrunner import Testrunner
from config import Config

# Testrunner 多进程 管理入口
class ProcessTestrunner():
    def __init__(self):
        self.main = Config.get_config('main').split(',')
    # 根据配置文件同时运行多少个项目
    def __multi_process(self):
        p = Pool()
        for i in self.main:
            p.apply_async(self, args=(i,))#这里是重点

        p.close()
        p.join()

    def __call__(self,sign):#这里是重点
        return self.__run_test(sign)

    def __run_test(self,sign):
        Testrunner().run(sign)

    # 入口
    def run(self):
        multi_processing = Config.get_config('multiProcessing')
        if multi_processing == 'True':
            self.__multi_process()
        else:
            self.__run_test(self.main[0])

if __name__ == '__main__':
    ProcessTestrunner().run()