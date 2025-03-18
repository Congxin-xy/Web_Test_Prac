from lib.api.Student import stm
from hytest import *
from lib.ui.websteps import *


class sc_test_5081:
    name = '学生登录1 - tc005081'

    def setup(self):
        open_web('student')

    def teststeps(self):
        STEP(1, '创建一个学生')
        start_id = GSTORE['start_id']
        res = stm.add_student('yangsanbai', '杨三白', '1', start_id, '13451813456')
        retAdd = res.json()
        self.addstuid = retAdd['id']
        STEP(2,'以创建学生的账号和密码登录web系统')
        wd = GSTORE['wd']
        login('yangsanbai', '888888')
        time.sleep(2)
        info_list = stu_info_dis()
        CHECK_POINT('学生信息显示',info_list == ['杨三白','白月学院00002','0','0'])
        STEP(2,'点击 错题库 菜单')
        wd = GSTORE['wd']
        wd.find_element(By.CSS_SELECTOR, '.main-menu a:nth-last-of-type(2) li').click()
        mes_info = wd.find_element(By.CSS_SELECTOR, '.fa-bug+span').text
        CHECK_POINT('错题库显示信息',mes_info == '您尚未有错题入库哦')

    def teardown(self):
        wd = GSTORE['wd']
        wd.quit()
        stm.delete_student(self.addstuid)

