import time
from lib.ui.websteps import *
from lib.api.Teacher import tchm
from hytest import *

def suite_setup():
    open_web('teacher')
    STEP(1, '创建一个老师，教授学科为初中数学（ID为1）')
    start_id = GSTORE['start_id']
    res = tchm.add_teacher('wangerbai', '王二百', '1', str(start_id), '13451813456', 'jcysdf@123.com',
                           '3209251983090987899')
    retAdd = res.json()
    CHECK_POINT('添加结果检查',
                retAdd['retcode'] == 0)
    GSTORE['Add_id'] = retAdd['id']

class sc_test_400x:
    ddt_cases = [
        {
            'name': '老师登录1 - tc004001',
            'para': ['wangerbai', '']
        },
        {
            'name': '老师登录2 - tc004002',
            'para': ['wangerbai', '8888888']
        },
        {
            'name': '老师登录3 - tc004003',
            'para': ['wangerbai', '888']
        },
        {
            'name': '老师登录4 - tc004004',
            'para': ['wangerbai', '5d#2d$']
        },
        {
            'name': '老师登录5 - tc004005',
            'para': ['', '888888']
        },
        {
            'name': '老师登录6 - tc004006',
            'para': ['wangerbai7', '888888']
        }
    ]

    def teststeps(self):
        STEP(2, '以创建老师的账号和密码登录 web系统')
        wd = GSTORE['wd']
        username, password = self.para
        login(username,password)
        mes = wd.find_element(By.CSS_SELECTOR,'.bootstrap-dialog-message').text
        CHECK_POINT('提示信息检查',mes == '登录失败 : 用户或者密码错误')

class sc_test_5007:
    name = '老师登录7 - tc004007'
    def teststeps(self):
        STEP(2, '以创建老师的账号和密码登录 web系统')
        wd = GSTORE['wd']
        login('wangerbai','888888')
        time.sleep(1)
        info_list = tch_info_dis()
        CHECK_POINT('检查网页信息', info_list == ['白月学院00002', '王二百', '初中数学', '0', '0', '0'])

def suite_teardown():
    wd = GSTORE['wd']
    Add_id = GSTORE['Add_id']
    wd.quit()
    tchm.delete_teacher(Add_id)