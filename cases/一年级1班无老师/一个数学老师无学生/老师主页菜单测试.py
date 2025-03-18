import time
from selenium.webdriver import ActionChains
from lib.ui.websteps import *
from lib.api.Teacher import tchm
from hytest import *

def suite_setup():
    open_web('teacher')
    login('liyihei','888888')

class sc_test_5001:
    name = '菜单栏1 - tc005001'

    def teststeps(self):
        wd = GSTORE['wd']
        menu = []
        page = wd.find_element(By.CSS_SELECTOR, '.main-menu a:nth-child(1) li').text
        menu.append(page)
        items = wd.find_elements(By.CSS_SELECTOR, '.main-menu li>a:nth-child(1)')
        for item in items:
            menu.append(item.text)
        CHECK_POINT('菜单内容检查', menu == ['主页','微课','作业','题目','班级情况'])

class sc_test_5002:
    name = '菜单栏2 - tc005002'

    def teststeps(self):
        wd = GSTORE['wd']
        minicl = []
        cl = wd.find_element(By.CSS_SELECTOR, '.main-menu>ul>li>a')
        ActionChains(wd).move_to_element(cl).perform()
        items = wd.find_elements(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(3) span')
        for item in items:
            minicl.append(item.text)
        CHECK_POINT('微课栏检查',minicl == ['创 建 微 课','已创建微课','已发布微课'])

class sc_test_5003:
    name = '菜单栏3 - tc005003'

    def teststeps(self):
        wd = GSTORE['wd']
        homework = []
        hw = wd.find_element(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(5)')
        ActionChains(wd).move_to_element(hw).perform()
        items = wd.find_elements(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(5) span')
        for item in items:
            homework.append(item.text)
        CHECK_POINT('作业栏检查',homework == ['创 建 作 业','已创建作业','已发布作业'])

class sc_test_5004:
    name = '菜单栏4 - tc005004'

    def teststeps(self):
        wd = GSTORE['wd']
        ques = []
        qt = wd.find_element(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(7)')
        ActionChains(wd).move_to_element(qt).perform()
        items = wd.find_elements(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(7) span')
        for item in items:
            ques.append(item.text)
        CHECK_POINT('题目栏检查',ques == ['搜索题目','新建题目'])

class sc_test_5005:
    name = '菜单栏5 - tc005005'

    def teststeps(self):
        wd = GSTORE['wd']
        clStatus = []
        cs = wd.find_element(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(9)')
        ActionChains(wd).move_to_element(cs).perform()
        items = wd.find_elements(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(9) span')
        for item in items:
            clStatus.append(item.text)
        CHECK_POINT('班级情况栏检查',clStatus == ['班级学生','统计分析'])

def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()