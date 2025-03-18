import time
from lib.api.Teacher import tchm
from lib.ui.websteps import *
from hytest import *

def suite_setup():
    open_web('teacher')

class sc_test_5002:
    name = '老师登录2 - tc005002'

    def teststeps(self):
        STEP(1, '创建一个老师，教授学科为初中数学（ID为1）')
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('wangerbai','王二百','1',str(start_id),'13451813456','jcysdf@123.com','3209251983090987899')
        retAdd = res.json()
        CHECK_POINT('添加结果检查',
                    retAdd['retcode'] == 0)
        self.addtchid = retAdd['id']
        STEP(2, '以创建老师的账号和密码（初始密码为888888）登录 web系统')
        wd = GSTORE['wd']
        login('wangerbai','888888')
        time.sleep(2)
        info_list = tch_info_dis()
        INFO(info_list)
        CHECK_POINT('检查网页信息',info_list == ['白月学院00002','王二百','初中数学','0','0','0'])
        STEP(3,'点开学生列表')
        wd.find_element(By.XPATH,"/html/body/div/div[1]/nav/div/div/ul/li[4]/a").click()
        wd.find_element(By.CSS_SELECTOR,'.fa-sitemap+span').click()
        wd.find_element(By.CSS_SELECTOR,'.fa-home').click()
        stu_num = wd.find_element(By.CSS_SELECTOR,'.fa-home+span').text
        time.sleep(1)
        stu_name = wd.find_element(By.XPATH,'//tbody/tr//span[@class="ng-binding"]').text
        CHECK_POINT('学生信息检查',stu_num == '1' and stu_name == '杨三白')

    def teardown(self):
        wd = GSTORE['wd']
        wd.quit()
        tchm.delete_teacher(self.addtchid)