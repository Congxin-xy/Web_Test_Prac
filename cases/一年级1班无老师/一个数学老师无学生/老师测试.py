from lib.api.Teacher import tchm
from hytest import *

class sc_test_1081:
    name = '删除老师1 - tc001081'

    def teststeps(self):
        STEP(1, '来删除一个老师，使url中的ID为一个不存在的老师ID号')
        res = tchm.delete_teacher('000000')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 404 and retAdd['reason'] == 'id 为`000000`的老师不存在')

class sc_test_1082:
    name = '删除老师2 - tc001082'

    def teststeps(self):
        STEP(1, '来删除一个老师，使url中的ID为一个存在的老师ID号')
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.delete_teacher(tchOne_id)
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
        STEP(2, '列出老师API')
        res = tchm.list_teacher()
        retList = res.json()

        expected = {
            "retlist": [],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('liyihei','李一黑','1',str(start_id),'13451816543','jcysdf@234.com','3209251985565595')
        retAdd = res.json()
        GSTORE['tchOne_id'] = retAdd['id']