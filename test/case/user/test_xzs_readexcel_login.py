import unittest,requests,ddt
from lib import read_excel
from lib.case_log import *
from config.config import *

def read():
    r = read_excel.readexcel()
    l = r.excel_to_list(data_file, "test_user_login")
    list1 = []
    # for i in l:
    #     list1.append(i.get("case_name"))
    # return list1
    for i in range(len(l)):
        list1.append(l[i]["case_name"])
    return list1
@ddt.ddt()
class MyTestCase(unittest.TestCase):
    @ddt.data(*read())
    def test_login(self,name):
        r = read_excel.readexcel()
        l = r.excel_to_list(data_file, "test_user_login")
        reg1 = r.get_test_data(l,name)
        url = reg1.get("url")
        args = reg1.get("args")
        res = reg1.get("expect_res")
        a = json.loads(args)
        req = requests.post(url=url, json=a)
        log_case_info(name,url,a,res,req.text)
        self.assertIn(res, req.text)


if __name__ == '__main__':
    unittest.main()
