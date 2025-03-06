from lib.api.Student import stm
from hytest import *

class sc_test_2001:
    name = '添加学生1 - tc002001'

    def teststeps(self):
        STEP(1, '创建一个学生，系统中不存在同登录名的学生')
        start_id = GSTORE['start_id']
        res = stm.add_student('yangsanbai','杨三白','1',start_id,'13451813456')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
        self.addstuid = retAdd['id']
        STEP(2, '列出学生API')
        res = stm.list_student()
        retList = res.json()

        expected = {
            "retlist": [
                {
                    "classid": start_id,
                    "username": "yangsanbai",
                    "realname": "杨三白",
                    "phonenumber": "13451813456",
                    "id": self.addstuid
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        stm.delete_student(self.addstuid)