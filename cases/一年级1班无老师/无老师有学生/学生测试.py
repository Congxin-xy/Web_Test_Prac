from lib.api.Student import stm
from hytest import *

class sc_test_2011:
    name = '修改学生1 - tc002011'

    def teststeps(self):
        STEP(1,'创建学生的API，来修改一个学生的手机号')
        stOne_id = GSTORE['stOne_id']
        start_id = GSTORE['start_id']
        res = stm.alter_student(stOne_id,phonenumber='13451813789')
        retAlter = res.json()
        CHECK_POINT('手机号是否修改成功',retAlter['retcode'] == 0)

        STEP(2,'列出学生')
        retList = stm.list_student().json()

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

    def teardown(self):
        stOne_id = GSTORE['stOne_id']
        stm.alter_student(stOne_id, phonenumber='13451813456')

class sc_test_2011:
    name = '修改学生4 - tc002014'

    def teststeps(self):
        STEP(1,'修改一个id不存在的学生的手机号')
        res = stm.alter_student('000000',phonenumber='13451813789')
        retAlter = res.json()
        CHECK_POINT('手机号是否修改成功',retAlter['retcode'] == 404 and retAlter['reason'] == "id 为`000000`的学生不存在")