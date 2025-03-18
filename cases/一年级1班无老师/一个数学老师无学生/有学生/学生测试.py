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

class sc_test_2003:
    name = '添加学生3 - tc002003'

    def teststeps(self):
        STEP(1, '创建一个学生，系统中存在同登录名的学生')
        start_id = GSTORE['start_id']
        stOne_id = GSTORE['stOne_id']
        res = stm.add_student('yangsanbai','赵二白','1',start_id,'13451816543')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 1 and retAdd['reason'] == "登录名`yangsanbai`已经存在，请换一个登录名")
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
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

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

class sc_test_2082:
    name = '删除学生2 - tc002082'

    def teststeps(self):
        STEP(1, '删除一个学生，使url中的ID为一个不存在的学生ID号')
        res = stm.delete_student('000000')
        retDelete = res.json()
        CHECK_POINT('添加结果检查',
                    retDelete['retcode'] == 404 and retDelete['reason'] == "id 为`000000`的学生不存在")

class sc_test_2015:
    name = '修改学生5 - tc002015'

    def teststeps(self):
        STEP(1,'创建学生的API，来修改一个学生的手机号')
        stOne_id = GSTORE['stOne_id']
        start_id = GSTORE['start_id']
        res = stm.alter_student(stOne_id,phonenumber='13451813789')
        retAlter = res.json()
        CHECK_POINT('手机号是否修改成功',retAlter['retcode'] == 0)

        STEP(2,'列出学生')
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
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)