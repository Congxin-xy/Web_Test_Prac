import time
from selenium.webdriver import ActionChains
from lib.ui.websteps import *
from lib.api.Teacher import tchm
from hytest import *

def suite_setup():
    open_web('teacher')
    login('liyihei','888888')

class sc_test_6001:
    name = '创建微课1 - tc006001'

    def teststeps(self):
        wd = GSTORE['wd']
        cl = wd.find_element(By.CSS_SELECTOR, '.main-menu>ul>li>a')
        ActionChains(wd).move_to_element(cl).perform()
        wd.find_element(By.CSS_SELECTOR, '.main-menu>ul>li:nth-child(3) .fa-plus+span').click
        title = wd.find_element(By.CSS_SELECTOR, '.page-title').text
        CHECK_POINT('标题检查',title == '新建微课 初中数学')

def suite_teardown():
    wd = GSTORE['wd']
    wd.quit()