# coding=utf-8
from unittest import suite,TextTestRunner
import time
from tool import Tool
from testloader import TestLoader
from testWork import WorkManager
from db import DB
from globals import g_set,g_get
from config import Config
from reportHtml import ReporeHtml

#定义 Testrunner 类
class Testrunner:
    def __init__(self):
        self.all_result = []

    # 获取discover里的所以用例 方法名称
    def __get_all_case(self,discover):
        all = []
        for item in discover:
            for i in str(item).split('testMethod='):
                for j in i.split('>'):
                    if 'test_' in j:
                        all.append({
                            'method_name':j,
                            'case':item
                        })
        return all

    # 获取未执行的用例
    def __get_case_incomplete(self,method_names):
        all = []
        # 获取db已经完成的用例
        complete = DB('temp', 'complete').select()
        # 先获取所以method_name用于后面对比
        all_c_mn=[]
        for item in complete:
            all_c_mn.append(item['method_name'])

        # 遍历所有用例
        for mn_item in method_names:
            # method_name 如果不在all_c_mn里面 说明么有测试的
            if mn_item['method_name'] not in all_c_mn:
                all.append(mn_item['case'])

        return all

    # 获取方法名
    def __get_result_name(self,item):
        return str(item[0]).split(' (')[0]

    # 获取所有 discover
    def __get_runner_discover(self):
        # 读取config interruptContinue:中断后开始是否继续开始
        is_interrupt_continue = Config.get_config('interruptContinue')
        # 项目路径
        project_path = Tool.get_project_dir()

        # 重写TestLoader 用于后期队列及报错连续执行
        discover = TestLoader().discover(project_path, pattern='*_st.py', top_level_dir=None)
        # 获取所有用例和方法名
        method_names = self.__get_all_case(discover)

        # 中断后开始是否继续开始
        if is_interrupt_continue == 'True':
            # 拿到方法名和结果队列比较
            discover = self.__get_case_incomplete(method_names)
        return discover,method_names

    def __runner_run(self,item):
        # 开始run test
        test_suites = suite.TestSuite(item)
        runner = TextTestRunner(verbosity=1)
        result = runner.run(test_suites)
        self.all_result.append(result)

    # 第一步获取 result
    def __get_runner_result(self):
        discover,method_names = self.__get_runner_discover()
        print('进入线程')
        work_manager = WorkManager(thread_num=10)
        for i in discover:
            work_manager.add_job(self.__runner_run(i),'')
        work_manager.wait_allcomplete()
        print('出来线程')
        # 循环 discover
        # threads = []
        # for i in discover:
        #     # 创建一个线程
        #     t = threading.Thread(target=self.__runner_run, args=(i,))
        #     threads.append(t)
        #     # 启动线程
        #     t.start()
        #     # t.join()
        #
        # for i in threads:
        #     i.join()

        DB().inster_all(g_get('db_all_insters'))
        DB('temp','complete').inster_all(g_get('db_complete_insters'))

        return {
            'method_names':method_names,
            'result':self.all_result
        }

    # 第二步获取用例返回的各种数据
    def __get_case_return_data(self,method_names,results):
        db = DB().select()
        all_data = []
        # 遍历所有用例方法
        for name in method_names:
            info = {
                'status_type':'success'
            }
            for result in results:
                # 匹配db里对应的方法
                for item in db:
                    if name['method_name'] in item['method_name']:
                        info['name'] = item['data']['name']
                        info['url'] = item['data']['url']
                        info['mode'] = item['data']['mode']
                        info['submit_data'] = item['data']['data']
                        info['code'] = item['result']['status_code']
                        info['status'] = item['result']['status']
                        # 状态类型 正确：success 错误：error 跳过：skipped
                        info['status_type'] = item['result']['status']
                        info['data'] = item['result']['response']
                        info['time'] = item['result']['time']
                        info['msg'] = item['result']['msg']

                # 获取跳过的
                for item in result.skipped:
                    if name['method_name'] in self.__get_result_name(item):
                        info['status_type'] = 'skipped'

                # 获取失败的
                for item in result.failures:
                    if name['method_name'] in self.__get_result_name(item):
                        info['status_type'] = 'error' # failures

                # 获取错误的
                for item in result.errors:
                    if name['method_name'] in self.__get_result_name(item):
                        info['status_type'] = 'error'

            all_data.append(info)
        return all_data

    #第三步生成报告
    def __build_report(self,start_time,end_time,case_data):
        ReporeHtml(start_time,end_time,case_data).build()

    # 先处理一下db文件
    def __db_clean(self):
        DB().remove_db()
        # 中断后开始是否继续开始
        is_interrupt_continue = Config.get_config('interruptContinue')
        if is_interrupt_continue == 'False':
            DB('temp', 'complete').remove_db()

    def run(self,main):
        # 先设置一下全局项目名称
        g_set('main',main)
        g_set('db_all_insters', [])
        g_set('db_complete_insters', [])
        # 清除db
        self.__db_clean()
        # 开始时间
        start_time = time.time()
        # 执行所有用例
        get_result = self.__get_runner_result()

        # 结束时间
        end_time = time.time()

        # # 获取用例返回的各种数据
        get_case_data = self.__get_case_return_data(get_result['method_names'], get_result['result'])
        # # 生成报告
        self.__build_report(start_time,end_time,get_case_data)
        print('------------------------')
        print(end_time-start_time)

if __name__ == '__main__':
    Testrunner().run('Demo')
