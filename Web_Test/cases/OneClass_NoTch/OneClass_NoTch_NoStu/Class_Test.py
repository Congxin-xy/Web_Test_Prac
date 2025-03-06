from lib.api.SClass import scm
from hytest import *
ClassTwo_id = GSTORE['ClassTwo_id']
ClassTwo_code = GSTORE['ClassTwo_code']

class sc_test_51:
    name = '修改班级1 - tc000051'

    def teststeps(self):
        STEP(1, '修改一个班级，使班级名为一个不重名的新的名字')
        ClassTwo_id = GSTORE['ClassTwo_id']
        ClassTwo_code = GSTORE['ClassTwo_code']
        start_id = GSTORE['start_id']
        start_code = GSTORE['start_code']
        res = scm.alter_class(ClassTwo_id,'白月黑羽3班','55')
        retAlter = res.json()
        CHECK_POINT('添加结果检查',
                    retAlter['retcode'] == 0)

        STEP(2,'列出班级API')
        res = scm.list_class(1)
        retList = res.json()
        INFO(retList)

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
                },
                {
                    "name": "白月黑羽3班",
                    "grade__name": "七年级",
                    "invitecode": ClassTwo_code,
                    "studentlimit": 55,
                    "studentnumber": 0,
                    "id": ClassTwo_id,
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        scm.alter_class(ClassTwo_id,'白月黑羽2班','55')

class sc_test_52:
    name = '修改班级2 - tc000052'

    def teststeps(self):
        STEP(1, '修改一个班级，使班级名为一个重名的新的名字')
        ClassTwo_id = GSTORE['ClassTwo_id']
        ClassTwo_code = GSTORE['ClassTwo_code']
        start_id = GSTORE['start_id']
        start_code = GSTORE['start_code']
        res = scm.alter_class(ClassTwo_id,'白月黑羽1班','55')
        retAlter = res.json()
        INFO(retAlter)
        CHECK_POINT('添加结果检查',
                    retAlter['retcode'] == 1 and retAlter['reason'] == "duplicated class name")

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
                },
                {
                    "name": "白月黑羽2班",
                    "grade__name": "七年级",
                    "invitecode": ClassTwo_code,
                    "studentlimit": 55,
                    "studentnumber": 0,
                    "id": ClassTwo_id,
                    "teacherlist": []
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

class sc_test_82:
    name = '删除班级2 - tc000082'

    def teststeps(self):
        STEP(1, '删除一个班级，使url中的ID为一个存在的班级ID号')
        ClassTwo_id = GSTORE['ClassTwo_id']
        start_id = GSTORE['start_id']
        start_code = GSTORE['start_code']
        res = scm.delete_class(ClassTwo_id)
        retDelete = res.json()
        INFO(retDelete)
        CHECK_POINT('添加结果检查',
                    retDelete['retcode'] == 0)
        STEP(2, '列出班级API')
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
    def teardown(self):
        res = scm.add_class(1, '白月黑羽2班', 55)
        retAdd = res.json()
        GSTORE['ClassTwo_id'] = retAdd['id']
        GSTORE['ClassTwo_code'] = retAdd['invitecode']