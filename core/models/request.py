# coding=utf-8
import requests

class Request:
    def __header(self,token):
        # print('headers')
        return token

    # get
    def _get(self, api, params, headers):
        r = requests.get(api, params=params, headers=headers, stream=True)
        return r

    # post
    def _post(self, api, data, headers):
        r = requests.post(api, data=data, headers=headers, stream=True)
        return r

    # request
    def request(self, api='', type="post", data={}, token=False):
        # 根据token来获取header
        headers = self.__header(token)

        #根据type
        if type == 'get':
            r =  self._get(api,data,headers)
        elif type == 'post':
            r =  self._post(api,data,headers)
        else:
            print('没有找到')
        #
        # 这里可以做个拦截 
        #
        r_data={
            'code':0,
            'status':'',
            'data':{},
            'time':0,# 时间
            'msg':'' # 错误提示
        }

        if r.status_code is 200:
            r_data['data'] = r.json()
            r_data['status'] = 'success'
        else:
            r_data['status'] = 'error'
            r_data['msg'] = r.text

        r_data['time'] = r.elapsed.total_seconds()
        r_data['code'] = r.status_code

        return r_data


if __name__ == '__main__':
    print('测试模块功能')