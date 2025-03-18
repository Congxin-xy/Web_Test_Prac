import selenium,time,random,string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from hytest import *

def open_web(type):
    INFO('打开网站')
    wd = webdriver.Chrome(service=Service(r'D:\Program Files\Python313\Practice\chromedriver.exe'))
    wd.get(f'http://127.0.0.1/{type}/login/login.html ')
    wd.implicitly_wait(10)
    wd.maximize_window()
    GSTORE['wd']=wd

def open_fgtpwd_web():
    INFO('打开忘记密码网站')
    fgt_pwd = webdriver.Chrome(service=Service(r'D:\Program Files\Python313\Practice\chromedriver.exe'))
    fgt_pwd.get(r'http://127.0.0.1/forgetpwd/forgetpwd.html#/step1')
    fgt_pwd.implicitly_wait(10)
    fgt_pwd.maximize_window()
    GSTORE['fgt_pwd']=fgt_pwd

def login(name,word):
    INFO('登录')
    wd = GSTORE['wd']
    if name is not None:
        username = wd.find_element(By.CLASS_NAME, 'username')
        username.clear()
        username.click()
        username.send_keys(name)
    if word is not None:
        password = wd.find_element(By.CLASS_NAME, 'password')
        password.clear()
        password.click()
        password.send_keys(word)
    wd.find_element(By.ID, 'submit').click()

def switch_win(title):
    wd = GSTORE['wd']
    for handle in wd.window_handles:
        # 先切换到该窗口
        wd.switch_to.window(handle)
        # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
        if title in wd.title:
            # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
            break

def tch_info_dis():
    INFO('显示页面信息')
    wd = GSTORE['wd']
    school_name = wd.find_element(By.CSS_SELECTOR, '.table-striped tr:nth-child(1) .ng-binding').text
    teacher_name = wd.find_element(By.CSS_SELECTOR, '.table-striped tr:nth-child(2) .ng-binding').text
    class_name = wd.find_element(By.CSS_SELECTOR, '.table-striped tr:nth-child(3) .ng-binding').text
    coins = wd.find_element(By.CSS_SELECTOR, '.table-striped tr:nth-child(4) .ng-binding').text
    class_num = wd.find_element(By.CSS_SELECTOR, '.fa-video-camera~ .ng-binding').text
    homework_num = wd.find_element(By.CSS_SELECTOR, '.fa-pencil-square-o~ .ng-binding').text
    info_list = [school_name,teacher_name,class_name,coins,class_num,homework_num]
    return info_list

def stu_info_dis():
    INFO('显示页面信息')
    wd = GSTORE['wd']
    stu_name = wd.find_element(By.CSS_SELECTOR, '.table-striped tr:nth-child(1) .ng-binding').text
    school_name = wd.find_element(By.CSS_SELECTOR, '.table-striped tr:nth-child(2) .ng-binding').text
    class_num = wd.find_element(By.CSS_SELECTOR, '.fa-video-camera~ .ng-binding').text
    homework_num = wd.find_element(By.CSS_SELECTOR, '.fa-pencil-square-o~ .ng-binding').text
    info_list = [stu_name, school_name, class_num, homework_num]
    return info_list

def generate_name(length):
    val = random.randint(0x4E00, 0x9FBF)
    alphabet = string.ascii_letters + string.digits + chr(val)
    name = ''.join(random.choice(alphabet) for i in range(length))
    return name