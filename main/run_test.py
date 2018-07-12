# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 16:42
# @Author  : Cr
# @File    : run_test.py
import sys
sys.path.append("D:/AutoTest/mkw_ApiTest")
#sys.path.append("E:/AutoTest/Api_Test_Demo/Learn_api_test")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent import DependdentData
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
    #程序执行的
    def go_on_run(self):
        res =None
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run =self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                is_run = self.data.get_is_run(i)
                data = self.data.get_data_for_json(i)
                header = self.data.is_header(i)
                expect = self.data.get_expect_data(i)
                depend_case = self.data.is_depend(i)
                res = self.run_method.run_main(method,url,data,header)
                if depend_case != None:
                    self.depend_data = DependdentData()
                    #获取 响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_filed(i)


                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,"通过")
                else:
                    self.data.write_result(i,"失败")
                print(res)


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
