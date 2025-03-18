from lib.api.SClass import scm
from hytest import *

class sc_test_01:
    name = '添加班级1 - tc000001'

    # 测试用例步骤
    def teststeps(self):

        STEP(1,'添加班级')

        res = scm.add_class(1,'白月黑羽1班', 55)
        retAdd = res.json()

        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)

        self.addclassid = retAdd['id']

        STEP(2,'列出班级')

        res = scm.list_class(1)
        retList = res.json()

        expected = {
            "gradeid": 1,
            "retlist": [
                {
                    "name": "白月黑羽1班",
                    "grade__name": "七年级",
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


    #清除方法
    def teardown(self):
        scm.delete_class(self.addclassid)

class sc_test_11:
    name = '列出班级1 - tc000011'

    def teststeps(self):
        STEP(1, '列出班级')
        res = scm.list_class(1)
        retList = res.json()

        expected = {
            "gradeid": 1,
            "retlist": [],
            "retcode": 0
        }

        CHECK_POINT('列出结果检查',
                    retList == expected)

class sc_test_81:
    name = '删除班级1 - tc000081'

    def teststeps(self):
        STEP(1, '删除一个班级，使url中的ID为一个不存在的班级ID号')
        res = scm.delete_class('000000')
        retDelete = res.json()
        CHECK_POINT('添加结果检查',
                    retDelete['retcode'] == 404 and retDelete['reason'] == "id 为`000000`的班级不存在")