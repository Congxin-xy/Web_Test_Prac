import time
from lib.ui.websteps import *
from lib.api.Teacher import tchm
from hytest import *

class sc_test_1001:
    name = '添加老师1 - tc001001'

    def teststeps(self):
        STEP(1, '创建一个老师，教授学科为初中数学')
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('wangerbai','王二百','1',str(start_id),'13451813456','jcysdf@123.com','3209251983090987899')
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
                    "username": "wangerbai",
                    "teachclasslist": [start_id],
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


class sc_test_5001:
    name = '老师登录1 - tc005001'

    def setup(self):
        open_web('teacher')

    def teststeps(self):
        STEP(1, '创建一个老师，教授学科为初中数学（ID为1）')
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('wangerbai','王二百','1',str(start_id),'13451813456','jcysdf@123.com','3209251983090987899')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
        self.addtchid = retAdd['id']
        STEP(2, '以创建老师的账号和密码登录 web系统')
        wd = GSTORE['wd']
        login('wangerbai','888888')
        time.sleep(2)
        info_list = tch_info_dis()
        CHECK_POINT('检查网页信息',info_list == ['白月学院00002','王二百','初中数学','0','0','0'])
        STEP(3,'点开学生列表')
        wd.find_element(By.XPATH,"/html/body/div/div[1]/nav/div/div/ul/li[4]/a").click()
        wd.find_element(By.CSS_SELECTOR,'.fa-sitemap+span').click()
        wd.find_element(By.CSS_SELECTOR,'.fa-home').click()
        stu_num = wd.find_element(By.CSS_SELECTOR,'.fa-home+span').text
        CHECK_POINT('学生列表为空',stu_num == '0')

    def teardown(self):
        wd = GSTORE['wd']
        wd.quit()
        tchm.delete_teacher(self.addtchid)

class sc_test_1061:
    name = '列出老师1 - tc001061'

    def teststeps(self):
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('liyihei', '李一黑', '1', str(start_id), '13451816543', 'jcysdf@234.com',
                               '3209251985565595')
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
                    "id": self.addtchid ,
                    "phonenumber": "13451816543",
                    "email": "jcysdf@234.com",
                    "idcardnumber": "3209251985565595"
                }
            ],
            "retcode": 0
        }
        CHECK_POINT('列出结果检查',
                    retList == expected)

    def teardown(self):
        tchm.delete_teacher(self.addtchid)

class sc_test_1081:
    name = '删除老师3 - tc001083'

    def teststeps(self):
        STEP(1, '来删除一个老师，使url中的ID为一个不存在的老师ID号')
        res = tchm.delete_teacher('000000')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 404 and retAdd['reason'] == 'id 为`000000`的老师不存在')