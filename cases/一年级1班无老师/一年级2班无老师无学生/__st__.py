from lib.api.SClass import scm
from hytest import *

def suite_setup():
    res = scm.add_class(1,'白月黑羽2班', 55)
    retAdd = res.json()
    ClassTwo_id = retAdd['id']
    GSTORE['ClassTwo_id'] = ClassTwo_id
    ClassTwo_code = retAdd['invitecode']
    GSTORE['ClassTwo_code'] = ClassTwo_code

def suite_teardown():
    res = scm.add_class(1,'白月黑羽2班', 55)
    ClassTwo_id = GSTORE['ClassTwo_id']
    scm.delete_class(ClassTwo_id)