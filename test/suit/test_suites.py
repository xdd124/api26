import unittest,sys
sys.path.append("../..")
from test.case.user.test_user_login import test_user_login
from test.case.user.test_user_reg import test_user_reg

def get_suite(suite_name):#获取TestSuite方法(获取指定测试套件实例)
    suite_name = unittest.TestSuite()  # 自定义TestSuite
    suite_name.addTests([test_user_login('test_login_ok'), test_user_reg('test_reg_ok')])
    return suite_name

# unittest.TextTestRunner(verbosity=2).run(smoke_suite)