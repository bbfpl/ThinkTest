import requests

class Xhr:
    def __header(self,token):
        print('headers')
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
    def request(self, api='',type="post", data={}, token=False):
        # 根据token来获取header
        headers = self.__header(token)
        #根据type
        if type is 'get':
            r =  self._get(api,data,headers)
        elif type is 'post':
            r =  self._post(api,data,headers)
        else:
            print('没有找到')
        #
        # 这里可以做个拦截 
        #
        r_data={
            'status':'',
            'data':{},
            'time':0,
            'msg':'' # 错误提示
        }
        if r.status_code is 200:
            r_data['data'] = r.json()
            r_data['status'] = 'success'
            r_data['time'] = r.time
        else:
            print('request error:' + r.status_code)
            r_data['status'] = 'error'
            r_data['msg'] = r.status_code

        return r_data