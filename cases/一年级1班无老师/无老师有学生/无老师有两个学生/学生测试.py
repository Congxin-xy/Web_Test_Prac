from lib.api.Student import stm
from hytest import *

class sc_test_2012:
    name = '修改学生2 - tc0020122'

    def teststeps(self):
        STEP(1,'修改一个学生的姓名，系统中未有重名学生')
        start_id = GSTORE['start_id']
        stOne_id = GSTORE['stOne_id']
        stTwo_id = GSTORE['stTwo_id']
        res = stm.alter_student(stTwo_id,realname='李四白')
        retAlter = res.json()
        CHECK_POINT('姓名是否修改成功',retAlter['retcode'] == 0)

        STEP(2, '列出学生')
        retList = stm.list_student().json()
        INFO(retList)

        expected = {
            "retlist": [
                {
                    "classid": start_id,
                    "username": "yangsanbai",
                    "realname": "杨三白",
                    "phonenumber": "13451813789",
                    "id": stOne_id
                },
                {
                    "classid": start_id,
                    "username": "zhaoerbai",
                    "realname": "李四白",
                    "phonenumber": "13451816543",
                    "id": stTwo_id
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        stTwo_id = GSTORE['stTwo_id']
        res = stm.alter_student(stTwo_id, realname='赵二白')

class sc_test_2013:
    name = '修改学生3 - tc0020123'

    def teststeps(self):
        STEP(1,'修改一个学生的姓名，系统中有重名学生')
        start_id = GSTORE['start_id']
        stOne_id = GSTORE['stOne_id']
        stTwo_id = GSTORE['stTwo_id']
        res = stm.alter_student(stTwo_id,realname='杨三白')
        retAlter = res.json()
        CHECK_POINT('姓名是否修改成功',retAlter['retcode'] == 0)

        STEP(2, '列出学生')
        retList = stm.list_student().json()

        expected = {
            "retlist": [
                {
                    "classid": start_id,
                    "username": "yangsanbai",
                    "realname": "杨三白",
                    "phonenumber": "13451813789",
                    "id": stOne_id
                },
                {
                    "classid": start_id,
                    "username": "zhaoerbai",
                    "realname": "杨三白",
                    "phonenumber": "13451816543",
                    "id": stTwo_id
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        stTwo_id = GSTORE['stTwo_id']
        res = stm.alter_student(stTwo_id, realname='赵二白')