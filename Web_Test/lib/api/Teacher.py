import json
import requests
from hytest import *
from cfg.cfg import *
from pprint import pprint

class Teacher:

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

    def list_teacher(self,subjectid=None):

        params = {
            'vcode': g_vcode,
            'action': 'search_with_pagenation'
        }

        if subjectid != None:
            params['subjectid'] = subjectid

        res = requests.get(
            g_api_url_teacher,
            params= params
        )

        self._printResponse(res)

        return res

    def add_teacher(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber):

        # 处理参数classlist
        if ',' in classlist:
            idList = classlist.split(',')
            classlist2 = [ {'id':int(cid.strip()) for cid in idList}]
        else:
            classlist2 = [{'id':classlist}]

        payload  = {
            'vcode'  : g_vcode,
            'action' : 'add',
            'username':username,
            'realname':realname,
            'subjectid'  : subjectid,
            'classlist'   : json.dumps(classlist2),
            'phonenumber': phonenumber,
            'email' : email,
            'idcardnumber':idcardnumber,
        }

        res = requests.post(
            g_api_url_teacher,
            data= payload
        )

        self._printResponse(res)

        return res

    def alter_teacher(self,teacherid,realname=None,subjectid=None,classlist=None,
                      phonenumber=None,email=None,idcardnumber=None):

        payload = {}
        # 处理参数classlist
        if realname != None:
            payload['realname'] = realname
        if subjectid != None:
            payload['subjectid'] = subjectid
        if classlist != None:
            if ',' in classlist:
                idList = classlist.split(',')
                classlist2 = [{'id': int(cid.strip()) for cid in idList}]
            else:
                classlist2 = [{'id': classlist}]
        if phonenumber != None:
            payload['phonenumber'] = phonenumber
        if email != None:
            payload['email'] = email
        if idcardnumber != None:
            payload['idcardnumber'] = idcardnumber

        payload = {
            'vcode': g_vcode,
            'action': 'modify',
        }
        url = f'{g_api_url_teacher}/{teacherid}'
        res = requests.put(url,data=payload)
        return res

    def delete_teacher(self,teacherid):

        payload  = {
            'vcode'  : g_vcode,
        }
        url = f'{g_api_url_teacher}/{teacherid}'
        res = requests.delete(url,data = payload)

        self._printResponse(res)

        return res

    def delete_all_teacher(self):
        res = self.list_teacher()
        retObj = res.json()
        for one in retObj['retlist']:
            self.delete_teacher(one['id'])

tchm = Teacher()