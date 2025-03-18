import time
from lib.api.Teacher import tchm
from lib.ui.websteps import *
from hytest import *

class sc_test_5101:
    name = '老师发布作业1 - tc005101'

    def setup(self):
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('liyihei', '李一黑', '1', str(start_id), '13451816543', 'jcysdf@234.com',
                               '3209251985565595')
        retAdd = res.json()
        tchOne_id = retAdd['id']
        GSTORE['tchOne_id'] = tchOne_id

    def teststeps(self):
        STEP(1, '以数学老师的账号和密码登录 web系统')
        open_web('teacher')
        wd = GSTORE['wd']
        login('liyihei','888888')

        STEP(2,'发布一个作业，包含3道选择题，把这个作业布置给一个学生')
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        wd.find_element(By.CSS_SELECTOR,'.sub-menu-1 #members +a span').click()
        time.sleep(2)
        wd.find_element(By.CSS_SELECTOR,'.col-lg-12 #btn_pick_question').click()
        wd.switch_to.frame('pick_questions_frame')
        time.sleep(3)
        items = wd.find_elements(By.CSS_SELECTOR,'.btn_pick_question')
        i = 0
        for item in items:
            if i < 3:
                item.click()
                i+=1
            else:
                break
        wd.find_element(By.CSS_SELECTOR,'.btn-blue').click()
        wd.switch_to.default_content()
        wd.find_element(By.CSS_SELECTOR,'.pull-left input').click()
        wd.find_element(By.CSS_SELECTOR, '.pull-left input').send_keys('作业1')
        wd.find_element(By.CSS_SELECTOR,'.ng-scope +button').click()
        wd.find_element(By.CSS_SELECTOR,'.bootstrap-dialog-footer-buttons button:nth-child(2)').click()
        switch_win('学习任务')
        wd.find_element(By.CSS_SELECTOR,'.myCheckbox span').click()
        wd.find_element(By.CSS_SELECTOR,'.btn-outlined').click()
        wd.find_element(By.CSS_SELECTOR,'.btn-primary').click()
        mes_info = wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        wd.find_element(By.CSS_SELECTOR, '.btn-default').click()
        CHECK_POINT('作业发布是否成功', '作业已发布' in mes_info)
        wd.quit()

        STEP(3,'以学生账号登录系统，发现有发布作业的通知，点击通知里面的作业，完成该作业')
        open_web('student')
        login('yangsanbai','888888')
        # 刷新wd
        wd = GSTORE['wd']
        time.sleep(2)
        wd.find_element(By.CSS_SELECTOR, '.dropdown .badge-yellow').click()
        wd.find_element(By.CSS_SELECTOR, '.dropdown-slimscroll .ng-binding').click()
        wd.find_element(By.CSS_SELECTOR, '.col-lg-12 td:nth-last-of-type(1) .btn-outlined').click()
        wd.find_element(By.CSS_SELECTOR,'.row .ng-scope .col-lg-12 .fa-check').click()
        wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons .btn-primary').click()
        wd.quit()

        STEP(4,'再次以老师账号登录系统，进入作业任务页面')
        open_web('teacher')
        wd = GSTORE['wd']
        login('liyihei', '888888')
        wd.find_element(By.CSS_SELECTOR, '.fa-pencil-square-o~ .ng-binding').click()
        wd.find_element(By.CSS_SELECTOR, '.tablelink .fa-search').click()
        time.sleep(2)
        grade = wd.find_element(By.CSS_SELECTOR, '.table .ng-scope p:nth-last-of-type(1)').text
        CHECK_POINT('学生成绩检查',grade == '正确率 0 % : 对 0 题， 错 3 题')
        wd.quit()

    def teardown(self):
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.delete_teacher(tchOne_id)

class sc_test_5102:
    name = '老师发布作业2 - tc005102'

    def setup(self):
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('liyihei', '李一黑', '1', str(start_id), '13451816543', 'jcysdf@234.com',
                               '3209251985565595')
        retAdd = res.json()
        tchOne_id = retAdd['id']
        GSTORE['tchOne_id'] = tchOne_id

    def teststeps(self):
        STEP(1, '以数学老师的账号和密码登录 web系统')
        open_web('teacher')
        wd = GSTORE['wd']
        login('liyihei','888888')

        STEP(2,'发布一个作业，作业名称为空字符串')
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        wd.find_element(By.CSS_SELECTOR,'.sub-menu-1 #members +a span').click()
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR,'.col-lg-12 #btn_pick_question').click()
        wd.switch_to.frame('pick_questions_frame')
        time.sleep(3)
        # 发布一道选择题
        wd.find_element(By.CSS_SELECTOR,'.btn_pick_question').click()
        wd.find_element(By.CSS_SELECTOR,'.btn-blue').click()
        wd.switch_to.default_content()
        wd.find_element(By.CSS_SELECTOR,'.ng-scope +button').click()
        mes = wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        CHECK_POINT('检查提示信息',mes == '请输入作业名称')
        STEP(3, '查看已发布作业')
        wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons .btn-default').click()
        wd.find_element(By.CSS_SELECTOR, '.main-menu li').click()
        wd.switch_to.alert.accept()
        wd.find_element(By.CSS_SELECTOR, '.fa-pencil-square-o~ .ng-binding').click()
        hw_info = wd.find_element(By.CSS_SELECTOR, '.col-lg-12>div:nth-child(2) .page-title').text
        CHECK_POINT('作业列表中没有出现新的作业',hw_info == '没有找到作业任务')
        wd.quit()

    def teardown(self):
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.delete_teacher(tchOne_id)

class sc_test_510x:
    ddt_cases = [
        {
            'name': '老师发布作业3 - tc005103',
            'para': '1'
        },
        {
            'name': '老师发布作业4 - tc005104',
            'para': generate_name(100)
        }
    ]

    def setup(self):
        start_id = GSTORE['start_id']
        res = tchm.add_teacher('liyihei', '李一黑', '1', str(start_id), '13451816543', 'jcysdf@234.com',
                               '3209251985565595')
        retAdd = res.json()
        tchOne_id = retAdd['id']
        GSTORE['tchOne_id'] = tchOne_id

    def teststeps(self):
        INFO(self.name)
        hw_name = self.para
        STEP(1, '以数学老师的账号和密码登录 web系统')
        open_web('teacher')
        wd = GSTORE['wd']
        login('liyihei','888888')

        STEP(2, f'发布一个作业，作业名称为{len(hw_name)}个字符串')
        wd.find_element(By.XPATH, '/html/body/div/div[1]/nav/div/div/ul/li[2]/a').click()
        wd.find_element(By.CSS_SELECTOR, '.sub-menu-1 #members +a span').click()
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, '.col-lg-12 #btn_pick_question').click()
        wd.switch_to.frame('pick_questions_frame')
        time.sleep(3)
        # 发布一道选择题
        wd.find_element(By.CSS_SELECTOR, '.btn_pick_question').click()
        wd.find_element(By.CSS_SELECTOR, '.btn-blue').click()
        wd.switch_to.default_content()
        wd.find_element(By.CSS_SELECTOR, '.pull-left input').click()
        wd.find_element(By.CSS_SELECTOR, '.pull-left input').send_keys(hw_name)
        wd.find_element(By.CSS_SELECTOR, '.ng-scope +button').click()
        mes = wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-message').text
        INFO(mes)
        CHECK_POINT('作业发布是否成功',mes == '新建作业成功')

        STEP(4,'查看已发布作业')
        wd.find_element(By.CSS_SELECTOR, '.bootstrap-dialog-footer-buttons button:nth-child(1)').click()
        hw_info = wd.find_element(By.CSS_SELECTOR, '.div-search-result-one .div-search-result-one-text').text
        CHECK_POINT('作业列表中有该作业，并且名称和输入的保持一致',hw_info == hw_name)
        wd.quit()
    def teardown(self):
        tchOne_id = GSTORE['tchOne_id']
        res = tchm.delete_teacher(tchOne_id)