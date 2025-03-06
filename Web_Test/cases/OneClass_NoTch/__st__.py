from lib.api.SClass import scm
from hytest import *

def suite_setup():
    res = scm.add_class(1,'白月黑羽1班', 50)
    retAdd = res.json()
    start_id = retAdd['id']
    GSTORE['start_id'] = start_id
    start_code = retAdd['invitecode']
    GSTORE['start_code'] = start_code

def suite_teardown():
    res = scm.add_class(1,'白月黑羽1班', 50)
    start_id = GSTORE['start_id']
    scm.delete_class(start_id)