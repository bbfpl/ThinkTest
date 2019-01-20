# coding=utf-8
import os
import time
import warnings
import yaml
from globals import g_get,base_dir
# Tool class
class Tool:
    base_dir = base_dir()

    def get_time(self,timestamp):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

    # 判断数组长度是非为0
    @staticmethod
    def is_list_empty(list_temp):
        if list_temp:
            return True
        else:
            return False

    # 判断是否为空
    @staticmethod
    def is_empty(val):
        if val is None or val is '' or val is 'null':
            return True
        else:
            return False

    # 获取 project 目录
    @classmethod
    def get_project_dir(cls,dir=''):
        # 读取项目入口
        if dir == '':
            project_name = g_get('main') # Config.get_config('main')
        else:
            project_name = dir

        path = cls.base_dir + '/project/' + project_name
        return path

    # 获取当前项目下yaml配置文件
    @classmethod
    def get_yaml(cls,name='',dir=''):
        # 忽略掉yaml告警
        warnings.simplefilter("ignore", DeprecationWarning)

        # 每个项目下面有个config.yaml
        config_path = cls.get_project_dir(dir) + '/config.yaml'
        #yaml的读取
        f = open(config_path, encoding='utf-8')
        data = yaml.load(f)
        f.close()
        if name != '':
            try:
                for item in name.split('.'):
                    data = data[item]
            except Exception as e:
                data = ''
        return data

    # 创建目录
    def mkdir(self,path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)

            print(path+' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            # print(path+' 目录已存在')
            return False

    # 读取文件
    def open_file(self, path):
        file_object = open(path, 'r',encoding='utf-8')
        try:
            ftext = file_object.read()
        finally:
            file_object.close()

        return ftext

    # 写入文件
    def write_file(self, path, code):
        if os.path.exists(path) is False:
            file = open(path, 'w',encoding='utf-8')
            file.write(code)
            file.close()

    # 删除文件
    def remove_file(self, path):
        print(path)
        if os.path.exists(path) is True:
            os.remove(path)

if __name__ == '__main__':
    # print(Tool.get_yaml('project.models.sales'))
    print(base_dir())

