from lib.api.Student import stm
from hytest import *

class sc_test_2002:
    name = '添加学生2 - tc002002'

    def teststeps(self):
        STEP(1, '创建一个学生，系统中不存在同登录名的学生')
        start_id = GSTORE['start_id']
        stOne_id = GSTORE['stOne_id']
        res = stm.add_student('zhaoerbai','赵二白','1',start_id,'13451816543')
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
                    "id": stOne_id
                },
                {
                    "classid": start_id,
                    "username": "zhaoerbai",
                    "realname": "赵二白",
                    "phonenumber": "13451816543",
                    "id": self.addstuid
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        stm.delete_student(self.addstuid)

class sc_test_2081:
    name = '删除学生1 - tc002081'

    def teststeps(self):
        STEP(1, '删除一个学生，使url中的ID为一个存在的学生ID号')
        stOne_id = GSTORE['stOne_id']
        res = stm.delete_student(stOne_id)
        retDelete = res.json()
        CHECK_POINT('添加结果检查',
                    retDelete['retcode'] == 0)
        STEP(2, '列出学生API')
        res = stm.list_student()
        retList = res.json()

        expected = {
            "retlist": [],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        start_id = GSTORE['start_id']
        res = stm.add_student('yangsanbai', '杨三白', '1', start_id, '13451813456')
        retAdd = res.json()
        stOne_id = retAdd['id']
        GSTORE['stOne_id'] = stOne_id