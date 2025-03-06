from lib.api.SClass import scm
from hytest import *
start_id = GSTORE['start_id']
start_code = GSTORE['start_code']

class sc_test_2:
    name = '添加班级2 - tc000002'

    def teststeps(self):
        STEP(1, '添加系统中不存在同年级的同名班级')
        res = scm.add_class(2,'白月黑羽3班',55)
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
        self.addclassid = retAdd['id']

        STEP(2,'列出班级API')
        res = scm.list_class(2)
        retList = res.json()

        expected = {
            "gradeid": 2,
            "retlist": [
                {
                    "name": "白月黑羽3班",
                    "grade__name": "八年级",
                    "invitecode": retAdd['invitecode'],
                    "studentlimit": 55,
                    "studentnumber": 0,
                    "id": retAdd['id'],
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        scm.delete_class(self.addclassid)

class sc_test_3:
    name = '添加班级3 - tc000003'

    def teststeps(self):
        start_id = GSTORE['start_id']
        start_code = GSTORE['start_code']
        STEP(1, '添加系统中已经存在同年级的同名班级')
        res = scm.add_class(1, '白月黑羽1班', 55)
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 1)
        STEP(2,'列出班级API')
        res = scm.list_class(1)
        retList = res.json()

        expected = {
            "gradeid": 1,
            "retlist": [
                {
                    "name": "白月黑羽1班",
                    "grade__name": "七年级",
                    "invitecode": start_code,
                    "studentlimit": 50,
                    "studentnumber": 0,
                    "id": start_id,
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

class sc_test_53:
    name = '修改班级3 - tc000053'

    def teststeps(self):
        STEP(1, '修改一个班级，使url中的ID为一个不存在的班级ID号')
        res = scm.alter_class('000000','白月黑羽1班','55')
        retAlter = res.json()
        CHECK_POINT('添加结果检查',
                    retAlter['retcode'] == 404 and retAlter['reason'] == "id 为`000000`的班级不存在")

