import time
from multiprocessing import Pool
from testrunner import Testrunner
from config import Config

# Testrunner 多进程 管理入口
class ProcessTestrunner():

    # 根据配置文件同时运行多少个项目
    def __multiProcess(self):
        p = Pool()
        for i in Config.get_config('main').split(','):
            p.apply_async(self, args=(i,))#这里是重点

        p.close()
        p.join()

    def __call__(self,sign):#这里是重点
        return self.__runTest(sign)

    def __runTest(self,sign):
        Testrunner().run(sign);

    # 入口
    def run(self):
        self.__multiProcess();