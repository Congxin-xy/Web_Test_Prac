from lib.api.Teacher import tchm
from hytest import *

def suite_setup():
    ClassTwo_id = GSTORE['ClassTwo_id']
    res = tchm.add_teacher('wangerbai','王二百','1',str(ClassTwo_id),'13451813456','jcysdf@123.com','3209251983090987899')
    retAdd = res.json()
    tchTwo_id = retAdd['id']
    GSTORE['tchTwo_id'] = tchTwo_id

def suite_teardown():
    tchTwo_id = GSTORE['tchTwo_id']
    res = tchm.delete_teacher(tchTwo_id)