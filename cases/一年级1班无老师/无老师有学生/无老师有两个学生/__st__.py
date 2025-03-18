from lib.api.Student import stm
from hytest import *

def suite_setup():
    start_id = GSTORE['start_id']
    res = stm.add_student('zhaoerbai','赵二白','1',start_id,'13451816543')
    retAdd = res.json()
    stTwo_id = retAdd['id']
    GSTORE['stTwo_id'] = stTwo_id

def suite_teardown():
    stTwo_id = GSTORE['stTwo_id']
    res = stm.delete_student(stTwo_id)