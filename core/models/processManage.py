import time
from multiprocessing import Pool
from testrunner import Testrunner
from config import Config
from httpServer import server_run
# ProcessManage 多进程 管理入口
class ProcessManage:
    def __init__(self):
        self.main = Config.get_config('main').split(',')
    # 根据配置文件同时运行多少个项目
    def __multi_process(self):
        p = Pool()
        p.apply_async(self, args=('HTTPSERVER',))
        for i in self.main:
            p.apply_async(self, args=(i,))#这里是重点

        p.close()
        p.join()

    def __call__(self,sign):#这里是重点
        return self.__run_server(sign)

    def __run_server(self,sign):
        if sign == 'HTTPSERVER':
            # 启动http服务
            server_run()
        else:
            Testrunner().run(sign)

    # 入口
    def run(self):
        multi_processing = Config.get_config('multiProcessing')
        if multi_processing == 'True':
            self.__multi_process()
        else:
            self.__run_server(self.main[0])
            # 启动http服务
            # server_run()
if __name__ == '__main__':
    ProcessManage().run()