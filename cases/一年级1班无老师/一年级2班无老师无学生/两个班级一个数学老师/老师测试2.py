from lib.api.Teacher import tchm
from hytest import *

class sc_test_1002:
    name = '添加老师2 - tc001002'

    def teststeps(self):
        STEP(1, '创建一个老师，系统中不存在同登录名的老师')
        start_id = GSTORE['start_id']
        ClassTwo_id = GSTORE['ClassTwo_id']
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.add_teacher('wangerbai','王二百','1',str(ClassTwo_id),'13451813456','jcysdf@123.com','3209251983090987899')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
        self.addtchid = retAdd['id']
        STEP(2, '列出老师API')
        res = tchm.list_teacher()
        retList = res.json()

        expected = {
            "retlist": [
                {
                    "username": "liyihei",
                    "teachclasslist": [start_id],
                    "realname": "李一黑",
                    "id": tchOne_id,
                    "phonenumber": "13451816543",
                    "email": "jcysdf@234.com",
                    "idcardnumber": "3209251985565595"
                },
                {
                    "username": "wangerbai",
                    "teachclasslist": [ClassTwo_id],
                    "realname": "王二百",
                    "id": self.addtchid,
                    "phonenumber": "13451813456",
                    "email": "jcysdf@123.com",
                    "idcardnumber": "3209251983090987899"

                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)
    def teardown(self):
        tchm.delete_teacher(self.addtchid)

class sc_test_1003:
    name = '添加老师3 - tc001003'

    def teststeps(self):
        STEP(1, '创建一个老师，系统中存在同登录名的老师')
        start_id = GSTORE['start_id']
        ClassTwo_id = GSTORE['ClassTwo_id']
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.add_teacher('liyihei','王二百','1',str(ClassTwo_id),'13451813456','jcysdf@123.com','3209251983090987899')
        retAdd = res.json()
        INFO(retAdd)
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 1 and retAdd['reason'] == '登录名 liyihei 已经存在')
        STEP(2, '列出老师API')
        res = tchm.list_teacher()
        retList = res.json()

        expected = {
            "retlist": [
                {
                    "username": "liyihei",
                    "teachclasslist": [start_id],
                    "realname": "李一黑",
                    "id": tchOne_id,
                    "phonenumber": "13451816543",
                    "email": "jcysdf@234.com",
                    "idcardnumber": "3209251985565595"
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

class sc_test_1004:
    name = '添加老师4 - tc001004'

    def teststeps(self):
        STEP(1, '创建一个老师，系统中同班级同学科的老师')
        start_id = GSTORE['start_id']
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.add_teacher('wangerbai','王二百','1',str(start_id),'13451813456','jcysdf@123.com','3209251983090987899')
        retAdd = res.json()
        CHECK_POINT('添加结果检查', retAdd['retcode'] == 1 and retAdd['reason'] == '任课信息冲突')

        STEP(2, '列出老师API')
        res = tchm.list_teacher()
        retList = res.json()
        INFO(retList)

        expected = {
            "retlist": [
                {
                    "username": "liyihei",
                    "teachclasslist": [start_id],
                    "realname": "李一黑",
                    "id": tchOne_id,
                    "phonenumber": "13451816543",
                    "email": "jcysdf@234.com",
                    "idcardnumber": "3209251985565595"
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

class sc_test_1051:
    name = '修改老师1 - tc001051'

    def teststeps(self):
        STEP(1, '修改一老师，使url中的ID为一个不存在的老师ID号')
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.alter_teacher('000000')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 1 and retAdd['reason'] == 'id 为`000000`的老师不存在')

class sc_test_1052:
    name = '修改老师2 - tc001052'

    def teststeps(self):
        STEP(1, '修改一个老师，同时修改真实名和授课班级。授课班级原来是1个班，改为两个班')
        tchOne_id = GSTORE['tchOne_id']
        start_id = GSTORE['start_id']
        ClassTwo_id = GSTORE['ClassTwo_id']
        res = tchm.alter_teacher(tchOne_id,realname='李一白',classlist=f'{start_id},{ClassTwo_id}')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
    def teardown(self):
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.alter_teacher(tchOne_id, realname='李一黑', classlist='start_id')

