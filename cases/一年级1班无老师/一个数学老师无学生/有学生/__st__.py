from lib.api.Student import stm
from hytest import *

def suite_setup():
    start_id = GSTORE['start_id']
    res = stm.add_student('yangsanbai','杨三白','1',start_id,'13451813456')
    retAdd = res.json()
    stOne_id = retAdd['id']
    GSTORE['stOne_id'] = stOne_id

def suite_teardown():
    stOne_id = GSTORE['stOne_id']
    res = stm.delete_student(stOne_id)