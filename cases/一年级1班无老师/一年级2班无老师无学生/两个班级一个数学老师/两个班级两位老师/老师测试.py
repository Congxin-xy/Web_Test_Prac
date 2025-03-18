from lib.api.Teacher import tchm
from hytest import *

class sc_test_1053:
    name = '修改老师3 - tc001053'

    def teststeps(self):
        STEP(1, '来修改一个老师的授课班级,授课班级该科目已有其他老师')
        start_id = GSTORE['start_id']
        tchTwo_id = GSTORE['tchTwo_id']
        res = tchm.alter_teacher(tchTwo_id,realname='王二百',classlist=str(start_id))
        retAdd = res.json()
        INFO(retAdd)
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 1 and retAdd['reason'] == '任课信息冲突')

    def teardown(self):
        ClassTwo_id = GSTORE['ClassTwo_id']
        tchTwo_id = GSTORE['tchTwo_id']
        tchm.alter_teacher(tchTwo_id,classlist=str(ClassTwo_id))