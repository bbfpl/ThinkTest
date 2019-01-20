from jinja2 import Template
import os
from tool import Tool
from config import Config

class MakeTest(Tool):
    project_path = ''
    def start(self,project_name=''):
        if project_name == '':
            main = Config.get_config('main')
        else:
            main = project_name

        # 获取config.yaml
        data = self.get_yaml('project.models',project_name)
        # 获取项目路径
        self.project_path = self.base_dir + '/project/' + main + '/'
        # 进入处理流程
        self.__process(data)
        # print(self.project_path)

    # 创建config.yaml文件
    def __create_config_yaml(self,filepath):
        # 获取写入路径
        config_path = filepath + '/config.yaml'
        # 获取code路径 
        code_path = os.path.dirname(__file__) + '/maketestTpl/config_yaml.txt'
        # 获取代码
        get_code  = self.open_file(code_path)
        # 写入内容
        self.write_file(config_path,get_code)

    # 创建__init__.py文件
    def __create_init_py(self,filepath):
        # 获取写入路径
        init_path = filepath + '/__init__.py'
        # init 是个空文件
        self.write_file(init_path,'')

    # 开始进入流程
    def __process(self,data):
        # 创建项目
        self.__process_project_name(data)

    # 创建项目目录
    def __process_project_name(self,data):
        # 创建目录
        self.mkdir(self.project_path)
        # 创建config.yaml
        # self.__create_config_yaml(path)
        # 遍历项目获取模块
        for key in data:
            model_path = self.project_path + key
            self.__process_project_model_name(model_path,data[key])

    # 创建项目模块目录
    def __process_project_model_name(self,path,data):
        # 创建模块目录
        self.mkdir(path)
        # 模块目录下面创建__init__.py
        self.__create_init_py(path)
        for key in data:
            filepath = path + '/' + key + '_st.py'
            if os.path.exists(filepath) == False:
                self.__process_project_test_code(filepath,data[key])

    # 创建测试用例文件+代码
    def __process_project_test_code(self,path,data):
        # 获取code路径
        code_path = os.path.dirname(__file__) + '/maketestTpl/test_code.txt'
        # 基础模板文件
        pycode = self.open_file(code_path)

        funs = []
        for key in data['funName']:
            funs.append({
                "name":key,
                "data":data['funName'][key]
            })
        template = Template(pycode)
        pycode = template.render(ClassName=data['className'],funs=funs)

        # 写入内容
        self.write_file(path,pycode)

if __name__ == '__main__':
    MakeTest().start()