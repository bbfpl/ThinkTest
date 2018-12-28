# coding=utf-8
import os
from core.models.tool import Tool
#安装类
class Install:
    def check_install(self):
        #返回最后值
        return self.__check_config() is True and self.__check_project() is True

    def __check_config(self):
        #默认_isInstall 为 False
        _isInstall = False

        # 获取根目录下config.ini
        config_path = os.path.join(os.getcwd(),'config.ini')

        config = Tool().read_base_config()

        #判断config是否存在 不存在就创建
        if os.path.exists(config_path) is False:
            config.add_section("Config")
            config.set("Config","project","[Demo]")
            config.set("Config","main","Demo")
            config.set("Config","log",'False')
            print('创建config.ini')
            #写入配置文件
            config.write(open(config_path, "w"))
        else:
            _isInstall = True
            #扩展config

        return _isInstall

    def __check_project(self):
        _isInstall = False
        #获取project目录
        project_path = os.path.join(os.getcwd(),'project')
        #获取project目录下 Demo
        project_demo_path = project_path + '/Demo'

        if os.path.exists(project_path) is False:
            os.makedirs(project_path)
            os.makedirs(project_demo_path)
            print('创建project目录成功')
        else:
            _isInstall = True

        return _isInstall
