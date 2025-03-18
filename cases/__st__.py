from lib.api.SClass import scm
from lib.api.Teacher import tchm
from lib.api.Student import stm

def suite_setup():
    stm.delete_all_student()
    tchm.delete_all_teacher()
    scm.delete_all_classes()


