from lib.api.Teacher import tchm
from hytest import *

def suite_setup():
    start_id = GSTORE['start_id']
    res = tchm.add_teacher('liyihei','李一黑','1',str(start_id),'13451816543','jcysdf@234.com','3209251985565595')
    retAdd = res.json()
    tchOne_id = retAdd['id']
    GSTORE['tchOne_id'] = tchOne_id

def suite_teardown():
    tchOne_id = GSTORE['tchOne_id']
    res = tchm.delete_teacher(tchOne_id)