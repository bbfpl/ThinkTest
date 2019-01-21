# coding=utf-8
from install import Install
from processTestrunner import ProcessTestrunner
from httpServer import server_run
class Core():
    # 私有方法 第一步先检查项目初始化
    def __check_install_fun(self):
        # 调用checkInstall函数 检查是否初始化
        if Install().check_install():
            # print('执行项目Test')
            self.__unittest_init()
        else:
            print('初始化完成')

    # 执行测试`
    def __unittest_init(self):
        print('执行测试')
        # 这里开始把多个项目丢给每个独立的进程执行
        ProcessTestrunner().run()
        # 启动http服务
        server_run()

    # 测试开始
    def run(self):
        self.__check_install_fun()
