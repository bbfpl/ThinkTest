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
        if r.status_code is 200:
            return r
        else:
            print('request error:' + r.status_code)