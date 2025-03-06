import requests
from hytest import *
from cfg.cfg import *
from pprint import pprint

class Student:

    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}: {v}')

        print('')

        body = response.content.decode('utf8')
        print(body)

        try:
            jsonBody = response.json()
            print(f'\n\n---- 消息体json ----\n'  )
            pprint(jsonBody)
        except:
            print('消息体不是json格式！！')

        print('-------- HTTP response * end -------\n\n')

    def list_student(self):

        params = {
            'vcode': g_vcode,
            'action': 'search_with_pagenation'
        }

        res = requests.get(
            g_api_url_student,
            params= params
        )

        self._printResponse(res)

        return res

    def add_student(self,username,realname,gradeid,classid,phonenumber):

        payload  = {
            'vcode'  : g_vcode,
            'action' : 'add',
            'username' : username,
            'realname' : realname,
            'gradeid'  : gradeid,
            'classid'   : classid,
            'phonenumber'  : phonenumber,
        }

        res = requests.post(
            g_api_url_student,
            data= payload
        )

        self._printResponse(res)

        return res

    def alter_student(self,studentid,realname=None,phonenumber=None):

        if realname != None:
            payload['realname'] = realname
        if phonenumber != None:
            payload['phonenumber'] = phonenumber

        payload = {
            'vcode': g_vcode,
            'action': 'modify',
        }
        url = f'{g_api_url_student}/{studentid}'
        res = requests.put(url, data=payload)
        return res

    def delete_student(self,studentid):

        payload  = {
            'vcode'  : g_vcode,
        }
        url = f'{g_api_url_student}/{studentid}'
        res = requests.delete(url,data = payload)

        self._printResponse(res)

        return res

    def delete_all_student(self):
        res = self.list_student()
        retObj = res.json()
        for one in retObj['retlist']:
            self.delete_student(one['id'])

stm = Student()
