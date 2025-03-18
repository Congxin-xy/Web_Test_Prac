import time
from lib.ui.websteps import *
from lib.api.Teacher import tchm
from hytest import *

def suite_setup():
    open_fgtpwd_web()

class sc_test_400x:
    ddt_cases = [
        {
            'name': '忘记密码1 - tc004011',
            'para': ['','请输入用户名']
        },
        {
            'name': '忘记密码2 - tc004012',
            'para': ['wdfuei','用户名不存在或未绑定手机号']
        },
        {
            'name': '忘记密码3 - tc004013',
            'para': ['wangerbai','验证码已发送']
        }
    ]

    def teststeps(self):
        STEP(2, '以创建老师的账号和密码登录 web系统')
        fgt_pwd = GSTORE['fgt_pwd']
        info, mes = self.para
        fgt_pwd.find_element(By.CSS_SELECTOR,'.border-o').click()
        fgt_pwd.find_element(By.CSS_SELECTOR,'.border-o').send_keys(info)
        fgt_pwd.find_element(By.CSS_SELECTOR, '.subtijiao input').click()
        time.sleep(1)
        message = fgt_pwd.find_element(By.CSS_SELECTOR,'.ng-binding').text
        CHECK_POINT('提示信息检查',mes == message)

def suite_teardown():
    fgt_pwd = GSTORE['fgt_pwd']
    fgt_pwd.quit()